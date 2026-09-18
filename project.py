import os


class ProgramBase:
    def start(self):
        print("კალკულატორი")


class Calculator(ProgramBase):

    def __init__(self, name):
        self.__name = name

    def start(self):
        print(self.__name)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


def save_result(number1, operation, number2, result):
    text = f"{number1} {operation} {number2} = {result}\n"

    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(text)


def show_results():
    if os.path.exists("results.txt"):
        with open("results.txt", "r", encoding="utf-8") as file:
            results = file.read()

        if results.strip() == "":
            print("შედეგები არ არის.")
        else:
            print("\nშედეგები:")
            print(results)
    else:
        print("ფაილი ჯერ არ არსებობს.")


def delete_results():
    if os.path.exists("results.txt"):
        os.remove("results.txt")
        print("შედეგები წაიშალა.")
    else:
        print("ფაილი არ არსებობს.")


def main():
    calculator = Calculator("ჩემი კალკულატორი")

    calculator.start()

    operations = ["+", "-", "*", "/"]

    running = True

    while running:
        print()
        print("1 - შეკრება")
        print("2 - გამოკლება")
        print("3 - გამრავლება")
        print("4 - გაყოფა")
        print("5 - შედეგების ნახვა")
        print("6 - შედეგების წაშლა")
        print("7 - გამოსვლა")

        choice = input("აირჩიე: ")

        if choice == "7":
            running = False
            print("პროგრამა დასრულდა.")
            continue

        if choice == "5":
            show_results()
            continue

        if choice == "6":
            delete_results()
            continue

        if choice not in ["1", "2", "3", "4"]:
            print("არასწორი არჩევანია.")
            continue

        try:
            number1 = float(input("შეიყვანე პირველი რიცხვი: "))
            number2 = float(input("შეიყვანე მეორე რიცხვი: "))
        except ValueError:
            print("არასწორი რიცხვია.")
            continue

        result = 0
        operation = ""

        if choice == "1":
            operation = operations[0]
            result = calculator.add(number1, number2)

        elif choice == "2":
            operation = operations[1]
            result = calculator.subtract(number1, number2)

        elif choice == "3":
            operation = operations[2]
            result = calculator.multiply(number1, number2)

        elif choice == "4":
            if number2 == 0:
                print("ნულზე გაყოფა არ შეიძლება.")
                continue

            operation = operations[3]
            result = calculator.divide(number1, number2)

        print("შედეგი:", result)

        save_result(number1, operation, number2, result)


main()