def create_atm_account(password, balance):

    def get_balance(pwd):
        if pwd == password:
            return balance
        else:
            return "Wrong password."

    def deposit(pwd, amount):
        nonlocal balance

        if pwd == password:
            balance += amount
            return f"Внесено '{amount}' средств. Новый баланс: {balance}"
        else:
            return "Wrong password."

    def withdraw(pwd, amount):
        nonlocal balance

        if pwd == password:
            if amount <= balance:
                balance -= amount
                return f"Снято '{amount}' средств. Новый баланс: {balance}"
            else:
                return "Недостаточно средств."
        else:
            return "Wrong password."

    return get_balance(), deposit, withdraw

a,b,c= create_atm_account(
    password="QWErty123456",
    balance=1000
)
print(a("QWErty123456"))