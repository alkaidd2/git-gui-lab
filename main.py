# Python pr: "Hello, World!"
def main():
    name = input("Enter your name: ")
    print(f"length = {len(name)}")  # строка для отладки
    name = name.strip()  # удаляет символ новой строки (и пробелы) в конце

if __name__ == "__main__":
    main()