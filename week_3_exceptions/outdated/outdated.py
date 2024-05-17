# (MM/DD/YYYY)

def main():
    get_dateFormated()

def get_dateFormated():

    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12"
    }

    while True:
        try:
            date_in = input("Date: ").strip().lower()
            if '/' in date_in:
                mm, dd, yyyy = date_in.split("/")
                m = int(mm)
                d = int(dd)
                if m > 12:
                    continue
                if d > 31:
                    continue
                if mm in months:
                    continue
                mm = mm.zfill(2)
                dd = dd.zfill(2)
                print(yyyy + "-" + mm + "-" + dd)
                return
            elif ',' in date_in:
                date_in = date_in.replace(",","").title()
                # print(date_in)
                month, dd, yyyy = date_in.split(" ")
                month = month.lower()
                month = month.capitalize()
                d = int(dd)
                dd = dd.zfill(2)
                if d > 31:
                    continue
                # if mm in months:
                #     continue
                if month in months:
                    mm = months[month]
                    print(yyyy + "-" + mm + "-" + dd)
                    return
                else:
                    pass
            else:
                pass

        except ValueError:
            pass

        # else:
        #     return
main()
