def solution(ings, menu, sell):
    answer = 0

    menu_name = []
    menu_ings = []
    menu_price = []

    ings_name = []
    ings_price = []

    for i in range(len(menu)):
        a = menu[i].split()
        menu_name.append(a[0])
        menu_ings.append(a[1])
        menu_price.append(a[2])

    for i in range(len(ings)):
        ing = ings[i].split()
        ings_name.append(ing[0])
        ings_price.append(ing[1])

    for record in sell:
        item, num = record.split()
        num = int(num)

        i = menu_name.index(item)
        price = int(menu_price[i])
        ingredient = menu_ings[i]

        ready_price = 0

        for g in ingredient:
            i = ings_name.index(g)
            ready_price += int(ings_price[i])

        answer += num * (price - ready_price)

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"],
               ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45",
                "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
