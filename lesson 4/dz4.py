uah = 0.025
usd = 40
def uah_usd():
    global usd
    money_ukr = float(input("Enter your hrn"))
    print(f"{round(money_ukr / usd, 2)} USD")

def usd_uah():
    global uah
    money_dollar = float(input("Enter your dollar"))
    print(f'{round(money_dollar / uah, 2)} UAH')

while True:
    print('''
    1. uah to usd
    2. usd to uah
    3. Exit     
        ''')
    user_chose = input("What you need to do")
    if user_chose == "1":
        uah_usd()
    elif user_chose == "2":
        usd_uah()
    elif user_chose == "3":
        break
    else:
        print("NOOOOOOOO NOOOOOOO NOOOOOOO NOOOO")


