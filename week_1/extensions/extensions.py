file = input("File name: ").lower().strip()
file = file.replace("."," ")
file_words = file.split()

match file_words[-1]:
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "pdf":
        print("application/pdf")
    case "gif":
        print("image/gif")
    case "png":
        print("image/png")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
