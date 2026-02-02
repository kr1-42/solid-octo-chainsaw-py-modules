from sys import argv


def main() -> int:
    if len(argv) == 1:
        print("=== inventory system ===\n")
        print("No items in inventory.\n")
        return 1
    print("=== Inventory System Analysis ===")
    try:
        items = [item.split(':', 1) for item in argv[1:]]
    except ValueError:
        print("Error: Invalid command line arguments for inventory items.")
        return 1
    inv = dict(items)
    tot_len = 0
    for _, quantity in items:
        try:
            tot_len += int(quantity)
        except ValueError:
            print(f"Warning: Non-integer quantity '{quantity}' ignored.")
    print(
        f"Total items in inventory: {tot_len}\n"
        f"Unique item types: {len(inv.keys())}"
    )
    print("\n=== Current Inventory ===")
    indexed_items = []
    idx = 0
    for name, quantity in items:
        indexed_items.append([idx, name, quantity])
        idx += 1

    ordered_items = []
    while indexed_items:
        best_pos = 0
        best_count = -1
        best_idx = indexed_items[0][0]
        pos = 0
        for entry in indexed_items:
            entry_idx, _, entry_qty = entry
            try:
                entry_count = int(entry_qty)
            except ValueError:
                entry_count = -1
            if (entry_count > best_count) or (
                entry_count == best_count and entry_idx < best_idx
            ):
                best_count = entry_count
                best_idx = entry_idx
                best_pos = pos
            pos += 1
        ordered_items.append(indexed_items.pop(best_pos))

    for _, item, quantity in ordered_items:
        try:
            count = int(quantity)
        except ValueError:
            print(f"{item}: {quantity} units (n/a)")
            continue
        percentage = (count / tot_len * 100) if tot_len else 0.0
        print(f"{item}: {count} units ({percentage:.1f}%)")

    print("\n=== Inventory Statistics ===")
    print(
            "most abundant:",
            f"{ordered_items[0][1]}",
            f"({ordered_items[0][2]} units)"
        )
    print(
            "least abundant:",
            f"{ordered_items[-1][1]}",
            f"({ordered_items[-1][2]} units)"
        )
    print("\n=== Item Categories ===")
    print(
            "moderate:",
            {ordered_items[0][2], ordered_items[0][1]}
    )
    print(
            "scarce:",
            {f"{item[1]}: {int(item[2])}" for item in ordered_items[1:]}
        )
    print("\n=== Management Suggestions ===")
    print(
            "restock needed: ",
            {
                f"{item[1]}"
                for item in ordered_items
                if int(item[2]) == 1
            }
    )
    print("\n=== Dictionary Properties Demo ===")
    print(
        f"dictionary keys: {list(inv.keys())}\n"
        f"dictionary values: {list(inv.values())}\n"
        f"Sample lookup - sword in inventory: {'sword' in inv}"
    )


if __name__ == "__main__":
    main()
