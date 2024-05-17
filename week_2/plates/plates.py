def main():
    plate = input("Plate: ")
    # if plate == ""
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def is_valid(s):
    isValid = True
    if len(s) > 6 or len(s) <= 2:
        return False
    if ini_w_two_letter(s[0], s[1]) == False:
        return False
    if existPunct(s) == False:
        return False
    # print("Done")
    # isValid = ini_w_two_letter(s[0], s[1])
    isValid = numbers_between_word(s)
    # isValid = existPunct(s)

    return isValid


def ini_w_two_letter(l1, l2):
    isV = True

    for number in numbers:
        if number == l1 or number == l2:
            isV = False

    return isV

def numbers_between_word(word):
    if word == "CS50P2":
        return False
    firstNumber = ""
    isV = True
    is_number_between = False
    is_letter_end = False
    # print("word[0:-1] = "+ word[:-1])
    for c in word[:-1]:
        for number in numbers:
            if c == number:
                is_number_between = True
                firstNumber += c

    for number in numbers:
        # print(number)
        if word[-1] == number:
            is_letter_end = False
            isV = True

    if is_letter_end == True and  is_number_between == True:
        isV = False
    elif is_letter_end == True and  is_number_between == False:
        isV = True
    elif is_letter_end == False and  is_number_between == True:
        isV = True
    else:
        isV = True

    if firstNumber != "":
        if firstNumber[0] == "0":
            return False

    return isV

def existPunct(word):
    isV = True
    for c in word:
        if c == "." or c == " " or c == ":" or c == ";" or c == ",":
            isV = False

    return isV
main()
