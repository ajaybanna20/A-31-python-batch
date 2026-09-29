price = int(input("enter your purchase value :"))

if price > 1000 :
    print("your final price ",price * 0.9)
elif 500 <= price <= 1000 :
    print("your final price", price *0.95)
else :
    print("final price without discount")