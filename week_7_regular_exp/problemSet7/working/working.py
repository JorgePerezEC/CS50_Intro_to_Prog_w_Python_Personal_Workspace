import re
import sys
#Author Jorge Perez

def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)


def convert(s):
    if matches:=re.search(r"^([0-9]+)(?::?([0-9]+))?\s(AM|PM)\s?(to)?\s?([0-9]+)(?::([0-9]+))?\s(AM|PM)$", s):
        if len(matches.groups())>1:
            # print(matches.groups())

            if int(matches.group(1)) >24 or int(matches.group(5)) > 24:
                raise ValueError()
            if (matches.group(2) != None and int(matches.group(2))) >59 or (matches.group(6) != None and int(matches.group(6)) > 59):
                raise ValueError()
            #MINUTES FORMAT
            if matches.group(2) == None:
                minIni = '00'
            else:
                minIni = matches.group(2)
            if matches.group(6) == None:
                minEnd = '00'
            else:
                minEnd = matches.group(6)
                #HOURS FORMAT
            if matches.group(3) == "PM":
                h = int(matches.group(1))+12
                if h == 24:
                    h = 12
                    hIni = str(h)
                else:
                    hIni = str(h)
            else:
                hIni = matches.group(1)
                if hIni == "12":
                    hIni = "00"
            if len(hIni) == 1 and matches.group(3) == "AM":
                hIni = f"0{matches.group(1)}"
            if matches.group(7) == "PM":
                h = int(matches.group(5))+12
                if h == 24:
                    h = 12
                    hEnd = str(h)
                else: hEnd = str(h)
            else:
                hEnd = matches.group(5)
                if hEnd == "12":
                    hEnd = "00"
            if len(hEnd) == 1 and matches.group(7) == "AM":
                hEnd = f"0{matches.group(5)}"
            formated_hour = f"{hIni}:{minIni} to {hEnd}:{minEnd}"
        return formated_hour
    else:
        raise ValueError("Value Error")

if __name__ == "__main__":
    main()
