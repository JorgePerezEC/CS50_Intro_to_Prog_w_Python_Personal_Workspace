import re

url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

if matches:= re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
    print(f"Username:",matches.group(1))

# if "/" in url:
#     items = url.split("/")

# print(f"Username is: {items[-1]}")


# re.split(pattern, string, maxsplit=0, flags=0)
# re.findall(pattern, string, flag=0)
