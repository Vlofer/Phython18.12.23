def get_numbers():
    numbers = []
    while True:
        number = input('Введите число:')
        if number == 'sum':
            break
        try:
            number = float(number)
        except ValueError:
            print("ЧИСЛО или SUM")
            continue
        numbers.append(number)
    return numbers

def sum_numbers():
    numbers = get_numbers()
    num = round(sum(numbers), 2)

    print(num)


sum_numbers()
