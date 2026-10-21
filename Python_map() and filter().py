#Q30. Order pipelin Keep paid orders, add 18% tax (round with round()), then keep only totals above 1000. Return dicts with id nd total
from tokenize import Ignore


orders = [
 {"id": 1, "amount": 500, "paid": True},
 {"id": 2, "amount": 1200, "paid": False},
 {"id": 3, "amount": 900, "paid": True},
 {"id": 4, "amount": 2000, "paid": True},
]

def amount_increaser(dict1):
    dict1["amount"] = dict1["amount"] *1.18
    return dict1

res = list (map(amount_increaser ,orders))
print(res)

final =list(filter(lambda x:x["amount"]>=1000 and x["paid"] == True,res))
print(final)

#29. Count per category or each category, return a dictionary with the type and how many items belong to it.

items = [
 {"name": "Apple", "type": "fruit"},
 {"name": "Carrot", "type": "veg"},
 {"name": "Banana", "type": "fruit"},
 {"name": "Pea", "type": "veg"},
 {"name": "Mango", "type": "fruit"},
]
types = ["fruit", "veg"]

veg_count = len(list(filter(lambda x: x["type"] == "veg", items)))
fruit_count = len(list(filter(lambda x: x["type"] == "fruit", items)))
type = ["fruit", "veg"]
count = [fruit_count, veg_count]
res =[{"type": type[x], "count": count[x]} for x in range(2)] # x=0,1
print(res)
      
#Q24. Email domains Ignore invalid emails (no "@", or nothing before it). Return the domain of each valid one.

emails = ["a@gmail.com", "bad-email", "b@yahoo.com",
          "c@gmail.com", "@x.com"]

res = list(filter(lambda x: "@" in x and x.index("@") > 0, emails))
res = list(map(lambda x: x.split("@")[1], res))
print(res)
