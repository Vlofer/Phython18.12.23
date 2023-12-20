while True:
    user_number = input("Write a number")
    #якщо ввести х прекратить роботу
    if user_number == "x":
        break
    #закидуємо це в трай щоб якщо введеться не число або не х ошибка не ламала код
    try:
        #пробуємо перетворити строку в число
        num = int(user_number)
    except ValueError:
        # якщо це не число то виводимо текст, і починаємо цикл заново continue
        print("not a number or not x")
        continue
    if num == -500 or num < -500:
            print("your number is less than or equal to -500 ")
    elif num == -100 or num < -100:
            print("your number is equals or more than -100, but less than -500")
    elif num < 0 :
        print("your number is less 0 or more to -100")
    elif num == 0 or num < 100:
        print("your number is equals or more than 0, but less than 100")
    elif num == 100 or num < 500:
        print("your number is equals or more than 100, but less than 500")
    elif num == 500 or num > 500:
        print("your number is equals or more then 500")