def main():
    fichier = str(input("File name: "))
    print(get_type(fichier))

def get_type(n):
    n = n.lower().strip()
    n = n.rsplit('.', 1)
    match n[1]:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"

main()