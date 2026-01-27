def ft_harvest_total():
    x = 1
    tot_len = 0
    while x <= 3:
        len = int(input(f"day {x} harvest: "))
        tot_len += len
        x += 1
    print("total harvest: ", tot_len)
