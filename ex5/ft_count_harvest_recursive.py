def ft_recursive(day):
    if (day != 1):
        ft_recursive(day - 1)
    print("Day", day)


def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    ft_recursive(day)
    print("Harvest time!")
