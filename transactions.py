transactions = [
    {"id": 201, "amount": 500},
    {"id": 202, "amount": 2000},
    {"id": 203, "amount": 6000}
]

for item in transactions:
    if item["amount"] > 3000:
        print(item["id"], "very high transaction")
    elif item["amount"] > 1000:
        print(item["id"], "high transaction")
    else:
        print(item["id"], "normal transaction")

with open("amounts.txt", "r") as file:
    for line in file:
        amount = int(line.strip())

        if amount > 3000:
            print(amount, "very high")
        elif amount > 1000:
            print(amount, "high")
        else:
            print(amount, "normal")
import json

with open("transaction.json", "r") as file:
    transaction = json.load(file)

print(transaction["amount"])
print(transaction["status"])
print(type(transaction))

new_transaction = {
    "id": 202,
    "amount": 5000,
    "status": "pending"
}

with open("new_transaction.json", "w") as file:
    json.dump(new_transaction, file)
import math
number = 25
result = math.sqrt(number)
print(result)

import calculator

result = calculator.add(10,20)
print(result)


class Transaction:
	def __init__(self,id,amount,status):
		self.id=id
		self.amount=amount
		self.status=status
	def show_details(self):
    		print(self.id, self.amount, self.status)


transaction1 = Transaction(101, 2500, "approved")
transaction2 = Transaction(102, 700, "pending")

print(transaction1.id)
print(transaction1.amount)
print(transaction1.status)

transaction1.show_details()
transaction2.show_details()

print("Transaction program completed")
print("Thank you")