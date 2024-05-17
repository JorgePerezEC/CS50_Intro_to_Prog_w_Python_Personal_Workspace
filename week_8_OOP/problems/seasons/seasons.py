from datetime import date
import re
import inflect
import sys

p = inflect.engine()

def main():
    try:
        date_birth = validate(input("Date of Birth: "))
        resul = res_dates(date_birth)
        print(resul)
    except ValueError as err:
        sys.exit("Invalid")

def res_dates(d):
    try:
        yyyy, mm, dd = d.split("-")
        birthday = date(int(yyyy), int(mm), int(dd))
        diff =  (date.today() - birthday).days *24*60
        # print(diff)
        res = p.number_to_words(diff, andword="").capitalize()
        return f"{res} minutes"
    except:
        raise ValueError("Invalid date")


def validate(date_b):
    if matches := re.search(r"^(\d{4})-(\d{2})-(\d{2})$",date_b):
        if int(matches.group(2)) > 12:
            raise ValueError("Invalid date")
        if int(matches.group(3)) > 31:
            raise ValueError("Invalid date")
        if matches.group(2) == "02" and int(matches.group(3)) > 29:
            raise ValueError("Invalid date")
        return date_b

    else:
        raise ValueError("Invalid date")


if __name__ == "__main__":
    main()
