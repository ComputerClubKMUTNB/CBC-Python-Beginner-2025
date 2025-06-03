def noodle_price(sen, nam, nuea, size):
    price = 0

    # noodle type
    if sen == "sen lek" or sen == "woon sen":
        price += 0
    elif sen == "sen mee khaow":
        price += 10
    elif sen == "sen yai":
        price += 15
    elif sen == "sen mee leuang":
        price += 20

    # soup
    if nam == "haeng" or nam == "nam tok":
        price += 0
    elif nam == "nam sai":
        price += 10
    elif nam == "tom yum" or nam == "yen ta fo":
        price += 20

    # meat
    if nuea == "mhoo toon":
        price += 10
    elif nuea == "nuea toon":
        price += 20

    # size
    if size == "tam mada":
        price += 0
    elif size == "piset":
        price += 10

    return price

def drink_price(drink, sweet, cup):
    price = 0

    # drink type
    if drink == "cha thai" or drink == "o liang":
        price += 0
    elif drink == "nom chompoo":
        price += 20
    elif drink == "nam plao":
        price += 10
        sweet = "mai mee"  # no sweetness for water

    # cup size
    if cup == "kaew lek":
        price += 0
    elif cup == "kaew yai":
        price += 10

    return price, sweet

def main():
    orders = []

    while True:
        print("\nChoose menu type: (1) guay tiew (2) drink (0 to stop)")
        choice = input("Choose: ")
        if choice == "0":
            break

        elif choice == "1":
            print("\nGuay Tiew Menu")
            sen = input("Choose noodle (sen): sen lek / woon sen / sen mee khaow / sen yai / sen mee leuang: ")
            nam = input("Choose soup (nam): haeng / nam tok / nam sai / tom yum / yen ta fo: ")
            nuea = input("Choose meat: mhoo toon / nuea toon: ")
            size = input("Choose size: tam mada / piset: ")
            price = noodle_price(sen, nam, nuea, size)
            orders.append(f"Guay Tiew {sen} {nam} {nuea} size {size} = {price}฿")

        elif choice == "2":
            print("\nDrink Menu")
            drink = input("Choose drink: cha thai / o liang / nom chompoo / nam plao: ")
            if drink != "nam plao":
                sweet = input("Sweetness: waan noi / bpakati / maak: ")
            else:
                sweet = "mai mee"
            cup = input("Choose cup size: kaew lek / kaew yai: ")
            price, sweet = drink_price(drink, sweet, cup)
            orders.append(f"Drink {drink} sweet: {sweet} cup: {cup} = {price}฿")

        else:
            print("Please choose a valid option")

    # show order summary
    print("\nOrder Summary")
    total = 0
    for i, order in enumerate(orders, start=1):
        print(f"{i}. {order}")
        total += int(order.split("=")[-1].replace("฿", "").strip())
    print(f"\nTotal: {total} baht")

main()