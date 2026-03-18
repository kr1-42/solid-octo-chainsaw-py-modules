import os
import re
from importlib.metadata import PackageNotFoundError
from importlib.metadata import version


def normalize_name(name: str) -> str:
    return name.strip().lower().replace("_", "-")


def parse_constraints(spec: str) -> list[tuple[str, str]]:
    operators = ["==", ">=", "<=", ">", "<"]
    constraints = []
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        for op in operators:
            if token.startswith(op):
                constraints.append((op, token[len(op):].strip()))
                break
    return constraints


def parse_dependency_string(entry: str) -> tuple[str, str]:
    match = re.match(r"^([A-Za-z0-9_.-]+)(.*)$", entry.strip())
    if not match:
        return "", ""
    name = normalize_name(match.group(1))
    spec = match.group(2).strip()
    return name, spec


def read_requirements(path: str) -> dict[str, str]:
    dependencies: dict[str, str] = {}
    if not os.path.exists(path):
        return dependencies

    with open(path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            name, spec = parse_dependency_string(line)
            if name:
                dependencies[name] = spec
    return dependencies


def read_poetry_dependencies(path: str) -> dict[str, str]:
    dependencies: dict[str, str] = {}
    if not os.path.exists(path):
        return dependencies

    in_project = False
    in_dependencies = False

    with open(path, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.strip()

            if line.startswith("[") and line.endswith("]"):
                in_project = line == "[project]"
                in_dependencies = False
                continue

            if not in_project:
                continue

            if line.startswith("dependencies") and "[" in line:
                in_dependencies = True
                quoted = re.findall(r'"([^"]+)"', line)
                for entry in quoted:
                    name, spec = parse_dependency_string(entry)
                    if name:
                        dependencies[name] = spec
                if "]" in line:
                    in_dependencies = False
                continue

            if in_dependencies:
                quoted = re.findall(r'"([^"]+)"', line)
                for entry in quoted:
                    name, spec = parse_dependency_string(entry)
                    if name:
                        dependencies[name] = spec
                if "]" in line:
                    in_dependencies = False

    return dependencies


def to_version_tuple(value: str) -> tuple[int, ...]:
    parts = []
    for token in value.replace("-", ".").split("."):
        number = ""
        for char in token:
            if char.isdigit():
                number += char
            else:
                break
        if number:
            parts.append(int(number))
        else:
            parts.append(0)
    return tuple(parts)


def compare_versions(installed: str, required: str, operator: str) -> bool:
    left = to_version_tuple(installed)
    right = to_version_tuple(required)
    if operator == "==":
        return left == right
    if operator == ">=":
        return left >= right
    if operator == "<=":
        return left <= right
    if operator == ">":
        return left > right
    if operator == "<":
        return left < right
    return False


def is_version_satisfied(installed: str, spec: str) -> bool:
    if not spec:
        return True
    constraints = parse_constraints(spec)
    if not constraints:
        return True
    for operator, required in constraints:
        if not compare_versions(installed, required, operator):
            return False
    return True


def compare_dependency_sources(
    pip_deps: dict[str, str],
    poetry_deps: dict[str, str],
) -> None:
    pip_only = sorted(set(pip_deps) - set(poetry_deps))
    poetry_only = sorted(set(poetry_deps) - set(pip_deps))
    common = sorted(set(pip_deps) & set(poetry_deps))
    spec_differences = [
        package
        for package in common
        if pip_deps[package] != poetry_deps[package]
    ]

    print("\nPIP VS POETRY COMPARISON:")
    print("  - pip: line-based requirements file (requirements.txt)")
    print("  - Poetry: project metadata + dependency list (pyproject.toml)")

    if pip_only:
        print(f"  - only in pip: {', '.join(pip_only)}")
    else:
        print("  - only in pip: none")

    if poetry_only:
        print(f"  - only in Poetry: {', '.join(poetry_only)}")
    else:
        print("  - only in Poetry: none")

    if spec_differences:
        print("  - version spec differences:")
        for package in spec_differences:
            pip_spec = pip_deps[package]
            poetry_spec = poetry_deps[package]
            print(
                f"    * {package}: "
                f"pip('{pip_spec}') vs Poetry('{poetry_spec}')"
            )
    else:
        print("  - version spec differences: none")


def compare_installed_versions(
    pip_deps: dict[str, str],
    poetry_deps: dict[str, str],
) -> bool:
    ok = True
    all_packages = sorted(set(pip_deps) | set(poetry_deps))

    print("\nINSTALLED VERSION CHECK:")
    for package in all_packages:
        pip_spec = pip_deps.get(package, "")
        poetry_spec = poetry_deps.get(package, "")

        try:
            installed = version(package)
        except PackageNotFoundError:
            print(
                f"  - {package}: NOT INSTALLED | "
                f"pip('{pip_spec or '-'}') | Poetry('{poetry_spec or '-'}')"
            )
            ok = False
            continue

        pip_ok = is_version_satisfied(installed, pip_spec)
        pip_state = "OK" if pip_ok else "MISMATCH"
        poetry_state = (
            "OK"
            if is_version_satisfied(installed, poetry_spec)
            else "MISMATCH"
        )

        if pip_state == "MISMATCH" or poetry_state == "MISMATCH":
            ok = False

        print(
            f"  - {package}: installed {installed} | "
            f"pip('{pip_spec or '-'}' -> {pip_state}) | "
            f"Poetry('{poetry_spec or '-'}' -> {poetry_state})"
        )

    return ok


def check_dependencies() -> int:
    req_path = os.path.join(os.getcwd(), "requirements.txt")
    pyproject_path = os.path.join(os.getcwd(), "pyproject.toml")

    pip_deps = read_requirements(req_path)
    poetry_deps = read_poetry_dependencies(pyproject_path)

    if not pip_deps:
        print("  - warning: requirements.txt missing or empty")
    if not poetry_deps:
        print("  - warning: pyproject.toml dependencies missing or empty")

    compare_dependency_sources(pip_deps, poetry_deps)
    return 0 if compare_installed_versions(pip_deps, poetry_deps) else 1


def visualization() -> None:
    try:
        import matplotlib.pyplot as plt
        import numpy
        import pandas
    except ModuleNotFoundError as error:
        print(f"Cannot create visualization: missing module {error.name}")
        return

    obj = []
    for i in range(50):
        i = i * 3.14
        obj.append(pandas.DataFrame(
            {
                "A": i * 1.0,
                "B": pandas.Timestamp("20130102") + pandas.Timedelta(days=i),
                "C": pandas.Series(i, index=list(range(4)), dtype="float32"),
                "D": numpy.array([i] * 4, dtype="int32"),
                "E": pandas.Categorical(["test", "train", "test", "train"]),
                "F": "foo",
            }))

    processed_data = pandas.concat(
        obj, keys=range(len(obj)), names=["i", "row"])
    processed_data = processed_data.reset_index()
    processed_data = processed_data.drop(columns=["row"])
    png_path = os.path.join(os.getcwd(), "visualization.png")
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis("off")
    table = ax.table(
        cellText=processed_data.astype(str).values,
        colLabels=processed_data.columns,
        cellLoc="center",
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.2)
    fig.savefig(png_path, dpi=200, bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)
    print("visualization complete. Displaying results...")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("checking dependencies from pip and Poetry files:")
    if check_dependencies() == 0:
        print("\nAll dependencies are up to date. Loading complete.\n")
    else:
        print("\nPlease resolve the above issues and try again.")
        print("Tips:")
        print("  - pip: pip install -r requirements.txt")
        print("  - Poetry: poetry install\n")
        return

    print("processing 1000 data points...")
    visualization()


if __name__ == "__main__":
    main()
