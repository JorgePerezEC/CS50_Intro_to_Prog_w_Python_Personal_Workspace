def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    float_money = float(d.replace("$",""))
    return float_money


def percent_to_float(p):
    int_percent = int(p.replace("%",""))
    return int_percent/100
main()
