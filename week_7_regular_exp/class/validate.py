import sys
import re

email = input("Email: ").strip()
"""
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
^ matches the start of the string
$ matches the end of the string
[] set of characters
[^] complementing the set  for ex: [@^] it means whatever unless @
..*@..* === .+@.+
\w means any word character, can replace ^[a-zA-Z0-9_]
\s whitespace characters
\S not a whitespace character
\d decimal digit
\D not a decimal digit
A|B  either A or B
(...) a group
(?:...) non-capturing version
"""
# if re.search(r"^.+@.+\.edu$+\.ec", email):
# if re.search(r"^.+/.+/.+", email): #Date expression
# if re.search(r"^[a-zA-Z0-9_]+@\w+\.edu$", email):
#Adding 3th expression
# if re.search(r"^[a-zA-Z0-9_]+@\w+\.edu$", email, re.IGNORECASE):
# if re.search(r"^(/w|\.)+@\w+\.edu$", email, re.IGNORECAS E):
if re.search(r"^[a-z0-9_\.]+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")


# try:
#     username, domain = email.split("@")
#     if "." in domain:
#         print("Valid")
#     else:
#         print("Invalid")
# except ValueError:
#     sys.exit("Bad answer")

# First method
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")
