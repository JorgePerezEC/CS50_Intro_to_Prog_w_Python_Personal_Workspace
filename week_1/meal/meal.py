def main():
    hour = input("What time is it? ")
    hour_formated = convert(hour)
    evaluate_meal(hour_formated)



def convert(time):
    time = time.replace(":"," ")
    # if time
    hour, min = time.split(" ")
    min_f = float(min)
    min_f = round(float(min_f),1)/60
    return float(hour) + min_f

def evaluate_meal(time):

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


if __name__ == "__main__":
    main()
