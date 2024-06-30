def login(signInCSV):
    for tries in range(6):
        username = input("Enter a username:\n")
        password = input("Enter a password:\n")
        if tries == 5:
            print("too many tries!")
            exit()
        else:
            for person in signInCSV:
                if person[1] == username and person[2] == password:
                    return True;
