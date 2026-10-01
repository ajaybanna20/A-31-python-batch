request = input("enter your request for bank :")

balance = 1000 

if request == "checkbalance" :
    print("your Total balance is :" ,balance)
elif request == "deposit" :
    deposite = int(input("enter your deposit money : "))
    print("your deposite money is : ", balance + deposit )
elif request == "withdraw" :
    withdraw = int(input("enter your withdrawal money : "))
    
    if withdraw < balance :
        print("your withdraw money is : ", balance - withdraw )
    else:
        print("insufficient balance")
else:
     print("invalid input")
