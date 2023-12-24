# def get_name_user(get_recipient_name):
#     return input("Ім'я одержувача: ")
#
#
# def change_name_user(
#         mail,
#         recipient_name
# ):
#     recipient_name = get_name_user()
def test(mail):
    name = input("Enter his name: ")
    surname = input("Enter his surname: ")
    your_name = input("Enter your name: ")
    your_surname = input("Enter your surname: ")
    your_position = input("Enter your position: ")

    return f"""   
    Dear {name} {surname},

    We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulm in faucibus
massa. Suspendisse at ex varius, portitior eros sit amet, sagittis nibh. In vel est a
tortor tempor luctus a.

    _________________
    {your_name} {your_surname} 
    {your_position}"""



mail = """   
    Dear *Ім'я одержувача* *Прізвище одержувача*,

    We are lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulm in faucibus
massa. Suspendisse at ex varius, portitior eros sit amet, sagittis nibh. In vel est a
tortor tempor luctus a.

    _________________
    *Ім'я відправника* *Прозвище відправника* 
    *Посада відправника*"""
print(mail)
mail = test(mail)
print(mail)
