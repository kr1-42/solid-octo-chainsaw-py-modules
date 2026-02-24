# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: chrilomb <chrilomb@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/24 14:16:28 by chrilomb          #+#    #+#              #
#    Updated: 2026/02/24 16:27:03 by chrilomb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt
import pandas
import matplotlib
import numpy
import os
from importlib.metadata import requires, version


def check_dependencies() -> int:
    dependencies = {
        "pandas": "2.1.0",
        "requests": "2.31.0",
        "matplotlib": "3.7.2"
    }
    for package, required_version in dependencies.items():
        try:
            installed_version = version(package)
            if installed_version < required_version:
                print(
                    f"  - {package} (installed: {installed_version},",
                    f"required: {required_version}) - OUTDATED\n"
                    "please update with pip install --upgrade {package}"
                    )
                return 1
            else:
                print(f"  - {package} (installed: {installed_version}) - OK")
        except Exception as e:
            print(f"  - {package} - NOT INSTALLED")
            print("please use pip -r requirements.txt on bash")
            return 1
    return 0

def visualitation() -> None:
    obj = []
    for i  in range(50):
        i * 3.14
        obj.append(pandas.DataFrame(
            {
                "A": i * 1.0,
                "B": pandas.Timestamp("20130102") + pandas.Timedelta(days=i),
                "C": pandas.Series(i, index=list(range(4)), dtype="float32"),
                "D": numpy.array([i] * 4, dtype="int32"),
                "E": pandas.Categorical(["test", "train", "test", "train"]),
                "F": "foo",
                }))
    processed_data = pandas.concat(obj, keys=range(len(obj)), names=["i", "row"])
    processed_data = processed_data.reset_index()
    processed_data = processed_data.drop(columns=["row"])
    png_path = os.path.join(os.getcwd(), "visualization.png")
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis("off")
    tbl = ax.table(
        cellText=processed_data.astype(str).values,
        colLabels=processed_data.columns,
        cellLoc="center",
        loc="center"
            )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(8)
    tbl.scale(1, 1.2)
    fig.savefig(png_path, dpi=200, bbox_inches="tight", pad_inches=0.1)
    matplotlib.pyplot.close()
    print("visualization complete. Displaying results...")
    plt.close(fig)


def main():
    print("\nLOADING STATUS: Loading programs...\n")
    print("checking dependencies:")
    if check_dependencies() == 0:
        print("\nAll dependencies are up to date. Loading complete.\n")
    else:
        print("\nPlease resolve the above issues and try again.\n")
        return
    print("processing 1000 data points...")
    visualitation()


if __name__ == "__main__":
    main()
