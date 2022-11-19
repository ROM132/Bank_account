import csv


class Bank_Account:

    def __init__(self):
        self.check_phone_number = False
        self.num = 0
        self.amount_to_transfer = 0

    def Login_Option(self):
        while True:
            print("Welcome to my Bank!")
            print("1. Login\n"
                  "2. Create new account")
            qus = input("Enter you choice: ")
            if qus == "1":
                b.Login_To_Your_Account()
            elif qus == "2":
                b.create_account()
            else:
                print("Invalid input try again!!")
                continue

    def Login_To_Your_Account(self):
        email_checker = ""
        control_when_to_Exit_the_loop = 0

        email = input("Enter your email here: ")
        passwords = input("Enter your passwords here: ")

        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row[0] and passwords in row[1]:
                    email_checker = row[0]
                    control_when_to_Exit_the_loop += 1

            if email == "" or passwords == "" or email_checker != email:
                qus = input("Your email or Password is Incorrect try again! To rest your password press (r) or enter to go back: ")
                if qus == "r":
                    b.rest_Password()
                else:
                    b.Login_Option()
            else:
                print("You logged in successfully!")

            b.After_Login(email)

    def create_account(self):
        email = input("Enter the email of the account: ")
        email = f"{email}@gmail.com"
        if len(email) < 16:
            print("Your email is to short try again!"), b.create_account()
        b.check_if_account_is_already_used(email)
        if self.num > 0:
            b.create_account()

        input(f"Your email is {email}\nPress enter to continue: ")
        while True:
            password = input("Enter the password of the account: ")
            if len(password) < 8:
                print("Your password is to short try again!")
                continue
            break

        while True:
            phone_number = input("Enter Your phone number: ")
            if phone_number.isdigit():
                pass
            else:
                print("Pls enter a number!!")
                continue

            if len(phone_number) != 10:
                print("Phone number must have 10 digit exactly!!")
                continue
            else:
                b.check_if_phone_number_is_already_used(phone_number)
                if self.check_phone_number is True:
                    self.check_phone_number = False
                    continue
                else:
                    break
        add_account = f"{email}, {password}, {phone_number}, 0"
        with open("Account details.csv", "a") as append_file:
            append_file.write(f"\n{add_account}")
            input("\nYour account added successfully!\nPress enter to go back: ")
        b.Login_Option()

    def check_if_account_is_already_used(self, email_to_check):
        self.num = 0
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email_to_check not in row[0]:
                    pass
                else:
                    input("This email is already used try again!\nPress enter to go back: ")
                    self.num += 1

    def check_if_phone_number_is_already_used(self, phone_number_to_check):
        self.num = 0
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if phone_number_to_check not in row[2]:
                    pass
                else:
                    input("This phone number is already used try again!\nPress enter to go back: ")
                    self.check_phone_number = True
                    self.num += 1

    def rest_Password(self):
        lines = list()
        num2 = 0
        num = 0
        email = input("Enter your email: ")

        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                row_zero = row[0].split()
                if email in row_zero:
                    num += 1
                else:
                    pass


        if num <= 0:
            print("This email does not exists! Try again"), b.rest_Password()
        else:
            phone_number = input("Ok enter your phone number so we can be sure its you: ")
            with open("Account details.csv", "r") as readfile_:
                reader_ = csv.reader(readfile_)
                for line in reader_:
                    row_two = line[2].split()
                    if phone_number in row_two:
                        num2 += 1
                    else:
                        pass
            if num2 <= 0:
                print("This is not the phone number your block! forever!"), exit()
            else:
                while True:
                    new_Password = input("Enter your new Password: ")
                    if len(new_Password) < 8:
                        print("You Passwrd must have at least 8 character")
                        continue
                    break
                with open("Account details.csv", "r") as writefile:
                    read = csv.reader(writefile)
                    for row in read:
                        phone_num = row[2].split()
                        if phone_number in phone_num:
                            row[1] = f" {new_Password}"
                        lines += f"{','.join(row)}\n"
                    string = ''.join(lines)

                    with open("Account details.csv", "w") as w:
                        w.write(string)
                        input("\nYour password change successfully!\nPress enter to go back: ")
                    b.Login_Option()

    def After_Login(self, email):
        print("1.Add amount")
        print("2.Check Balance")
        print("3.Transfer amount")
        print("4.Edit profile")
        print("5.Logout")
        qus = input("Enter your choice: ")
        if qus == "1":
            b.add_Amount(email)
        if qus == "2":
            b.check_balance(email)
        if qus == "3":
            b.transfer_money(email)
        if qus == "4":
            b.edit_Profile(email)
        if qus == "5":
            print("You logged out!"), b.Login_Option()
        else:
            print("Invalid input!"), b.After_Login(email)

    def check_balance(self, email):
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row:
                    balance = row[3]
                    input(f"Your balance is{balance} dollar\nPress enter to go back: "), b.After_Login(email)

    def add_Amount(self, email):
        lines = list()
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row:
                    add_amount = input("How much money do you like to add to your account: ")
                    if add_amount.isdigit():
                        row[3] = int(row[3]) + int(add_amount)
                        row[3] = f" {row[3]}"
                        row[3] = str(row[3])
                    else:
                        print("Pls enter a number next time!"), b.add_Amount(email)
                    money = row[3]
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row:
                    row[3] = money
                lines += f'{",".join(row)}\n'
            string = "".join(lines)
        with open("Account details.csv", "w") as writefile:
            writefile.write(string)
            input("Your amount has been added!\nPress enter to go back: ")
        b.After_Login(email)

    def edit_Profile(self, email):
        lines = list()
        qus = input("What you want to edit in your profile?\nYour (e)email or your (p)password or your (n)phone number: ")
        if qus == "e" or qus == "p" or qus == "n":
            with open("Account details.csv", "r") as readfile:
                if qus == "e":
                    choice = "email"
                    num = 0
                elif qus == "p":
                    choice = "password"
                    num = 1
                elif qus == "n":
                    choice = "phone number"
                    num = 2

                reader = csv.reader(readfile)
                for row in reader:
                    if email in row:
                        while True:
                            qus = input(f"Enter your new {choice}: ")
                            if num == 0:
                                row[num] = f"{qus}@gmail.com"
                                check = row[num]
                                b.check_if_account_is_already_used(row[num])
                                if self.num > 0:
                                    continue
                                break
                            elif num == 1:
                                if len(qus) < 8:
                                    print(f"The {choice} is to short try again!")
                                    continue
                                row[num] = qus
                                check = row[num]
                                break
                            elif num == 2:
                                if qus.isdigit():
                                    if len(qus) != 10:
                                        print("Phone number need to be exactly 10 number!")
                                        continue
                                    row[num] = qus
                                    check = row[num]
                                    b.check_if_phone_number_is_already_used(row[num])
                                    if self.num > 0:
                                        continue
                                    break
                                else:
                                    print("Pls enter a number next time!")
                                    continue

            with open("Account details.csv", "r") as readfile:
                reader = csv.reader(readfile)
                for row in reader:
                    if email in row:
                        row[num] = f" {check}"
                    lines += f'{",".join(row)}\n'
                string = "".join(lines)
            with open("Account details.csv", "w") as writefile:
                writefile.write(string)
                input("Your account has been changed!\nPress enter to go back: ")
            b.After_Login(email)

        else:
            print("Invalid input try again!"), b.edit_Profile(email)

    def transfer_money(self, email):
        check = False
        email_to_transfer = input("Enter the email you want to transfer to: ")
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email_to_transfer not in row[0]:
                    pass
                else:
                    check = True
            if check is True:
                if email == email_to_transfer:
                    print("You can't transfer to your self money!"), b.transfer_money(email)
                else:
                    b.transfer_money_from_account_to_another(email_to_transfer, email)
            else:
                print("This email does not exist try again!"), b.transfer_money(email)

    def transfer_money_from_account_to_another(self, email_to_transfer, email):
        lines = list()
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row:
                    add_amount = input("How much money do you like to transfer to this account: ")
                    if add_amount.isdigit():
                        row[3] = int(row[3])
                        add_amount = int(add_amount)
                        if row[3] >= add_amount:
                            self.amount_to_transfer = add_amount
                            row[3] = int(row[3]) - int(add_amount)
                            row[3] = f" {row[3]}"
                            row[3] = str(row[3])
                        else:
                            print("You dont have enough money")
                            b.transfer_money_from_account_to_another(email_to_transfer, email)
                    else:
                        print("Pls enter a number next time!"), b.add_Amount(email)
                    money = row[3]
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row:
                    row[3] = money
                lines += f'{",".join(row)}\n'
            string = "".join(lines)
        with open("Account details.csv", "w") as writefile:
            writefile.write(string)
            input("Your amount has been transfer!\nPress enter to go back: ")
        b.transfer(email_to_transfer, email)

    def transfer(self, email, email_to_move):
        lines = list()
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email in row:
                    self.amount_to_transfer = int(row[3]) + self.amount_to_transfer
                    row[3] = f" {str(self.amount_to_transfer)}"
                lines += f'{",".join(row)}\n'
            string = "".join(lines)
        with open("Account details.csv", "w") as writefile:
            writefile.write(string)
        b.After_Login(email_to_move)


b = Bank_Account()
b.Login_Option()
