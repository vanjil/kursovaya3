from develop import utils

def main():
    filename = 'operations.json'

    try:
        amount_of_operations = int(input("Введите количество операций: "))
        data = utils.get_data(filename)
        operations_executed = utils.get_operations_executed(data)
        last_operations = utils.get_last_operations(operations_executed, amount_of_operations)
        operations_formatted = utils.get_operations_formatted(last_operations)

        if operations_formatted:
            print("Последние операции:")
            for string in operations_formatted:
                print(f"{string}\n")
        else:
            print("Нет данных о последних операциях.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except ValueError:
        print("Ошибка: Введите корректное число операций.")

if __name__ == "__main__":
    main()
