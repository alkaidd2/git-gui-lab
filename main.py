# Python pr: "Hello, World!"
def main():
    name = input("Enter your name: ")
    print(f"length = {len(name)}")  # ������ ��� �������
    name = name.strip()  # ������� ������ ����� ������ (� �������) � �����

if __name__ == "__main__":
    main()