import csv


class Bank_Account:

    def __init__(self):
        self.check_phone_number = False


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

            if email_checker == "":
                qus = input("Your email or Password is Incorrect try again! To rest your password press (r) or enter to go back: ")
                if qus == "r":
                    b.rest_Password()
                else:
                    b.Login_Option()
            else:
                print("You logged in successfully!")
                print("Come back later to add a place to move to after the logging"), exit()

    def create_account(self):
        email = input("Enter the email of the account: ")
        email = f"{email}@gmail.com"
        if len(email) < 16:
            print("Your email is to short try again!"), b.create_account()
        b.check_if_account_is_already_used(email)
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
        add_account = f"{email}, {password}, {phone_number}"
        with open("Account details.csv", "a") as append_file:
            append_file.write(f"\n{add_account}")
            input("\nYour account added successfully!\nPress enter to go back: ")
        b.Login_Option()

    def check_if_account_is_already_used(self, email_to_check):
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if email_to_check not in row[0]:
                    pass
                else:
                    input("This email is already used try again!\nPress enter to go back: "), b.create_account()

    def check_if_phone_number_is_already_used(self, phone_number_to_check):
        with open("Account details.csv", "r") as readfile:
            reader = csv.reader(readfile)
            for row in reader:
                if phone_number_to_check not in row[2]:
                    pass
                else:
                    input("This phone number is already used try again!\nPress enter to go back: ")
                    self.check_phone_number = True

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


b = Bank_Account()
b.Login_Option()
