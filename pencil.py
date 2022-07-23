import random

def is_correct(user_number, flag):
    if not user_number.isdigit() and flag != False:
        print("The number of pencils should be numeric")
        return False
    elif flag != False and int(user_number) <= 0:
        print("The number of pencils should be positive")
        return False
    elif flag:
        return True
    elif user_number != '1' and user_number != '2' and user_number != '3':
        print("Possible values: '1', '2', '3'")
        return False
    else:
        return True

def ask_and_correct(answer, flag):
    while True:
        if not is_correct(answer, flag):
            answer = input()
        else:
            return answer

def main():
    print("How many pencils would you like to use: ")
    userchoice = input()
    userchoice = int(ask_and_correct(userchoice, True))

    person = True
    print("Who will be the first (John, Jack): ")
    who_first = input()
    if who_first == "Jack":
        person = False
    while who_first != "John" and who_first != "Jack":
        print("Choose between John and Jack")
        who_first = input()
        if who_first == "John":
            person = True
        elif who_first == "Jack":
            person = False
    print(userchoice * "|")
    while userchoice > 0:
        if not person:
            print("Jack's turn")
    # bot strategy
    # winning strategy
            if userchoice % 4 == 0:
                to_delete = 3
            elif userchoice % 4 == 3:
                to_delete = 2
            elif userchoice % 4 == 2:
                to_delete = 1
            else:
                to_delete = random.randint(1,3)
                while to_delete > userchoice:
                    to_delete = random.randint(1,3)
            print(to_delete)
        else:
            print("John's turn")
            to_delete = input()
            to_delete = int(ask_and_correct(to_delete, False))
        person = not person
        while to_delete > userchoice:
            print("too many pencils")
            to_delete = input()
            to_delete = int(ask_and_correct(to_delete, False))
        userchoice = userchoice - to_delete
        if userchoice > 0:
            print(userchoice * "|")
    else:
        if not person:
            print("Jack won!")
        else:
            print("John won!")

if __name__ == '__main__':
    main()

