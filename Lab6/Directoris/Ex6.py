import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"{letter}.txt")

def main():
    generate_files()

if __name__ == "__main__":
    main()