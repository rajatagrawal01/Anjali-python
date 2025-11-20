Username = "Anj"
Current_pass = 987
Current_Balance = int(100000)

Name = input("Enter your name:-")
Password = int(input("Enter the password:-"))

if Name != Username and Password != Current_pass:
    print("Entered wrong username and Password")
    exit()

if Name == Username and Password != Current_pass:
    print("Entered wrong Password")
    exit()

if Password == Current_pass and Name == Username: 
    print("Your current Balance is : ", Current_Balance)

    Withdraw = int(input("How much amount you wants to withdraw:-"))
    Withdrawn_amount = Withdraw

    if Withdraw>Current_Balance:
        print("Can't Withdrawn this much amount becuase your withdrawn amount is greater than the current balance i.e.", Current_Balance)
        exit()

    if Withdraw <= 0 or Withdraw % 100 != 0:
        print("Invalid amount, please enter amount in multiple of 100, 200, or 500")
        exit()

    notesOf500=0
    notesOf200=0
    notesOf100=0

    if Withdraw >= 500:
        notesOf500 = Withdraw // 500
        Withdraw %= 500
    if Withdraw >= 200:
        notesOf200 = Withdraw // 200
        Withdraw %= 200
    if Withdraw >= 100:
        notesOf100 = Withdraw // 100
        Withdraw %= 100

    New_B = Current_Balance - Withdrawn_amount
    print("Notes of 500 : ",notesOf500)
    print("Notes of 200 : ",notesOf200)
    print("Notes of 100 : ",notesOf100)
    print("Total you have withdrawn", Withdrawn_amount , "and your new balance is:-", New_B )