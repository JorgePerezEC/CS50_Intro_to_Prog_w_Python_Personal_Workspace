from validator_collection import validators, checkers, errors

email_address = input("What's your email address? ")
is_email_address = checkers.is_email(email_address)

if is_email_address:
    print("Valid")
else:
    print("Invalid")
