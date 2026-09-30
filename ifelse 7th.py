month = input ("enter a  month : ")

a = "jan","mar","may","july","aug","oct","dec"
b = "apr", "jun","sep","nov"
c = "feb"

if (month in a):
    print("this month have 31 days")
elif(month in b):
    print("this month have 30 days")
elif(month in c):
    print("this month have 29 days")
else:
    print("invalid input")
else: