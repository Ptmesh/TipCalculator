print("Welcome to the tip calculator by Ptmesh😸\n")

bill = float(input("What is the amount of bill? \n₹"))
tip = int(input("How much % of tip do you wanna include?\n"))
numOfPeople = int(input("How many people do you wanna split bill with? \n"))

tip_per = tip/100
total_tip = bill * tip_per
total_bill = bill + total_tip
individualBill = (total_bill/numOfPeople)
finalBillAmount=round(individualBill, 5)

print(f"Received Bill: ₹{bill}\nTip Percentage: {tip}%\nRevised Bill: ₹{total_bill} \nNumber of people to split with: {numOfPeople}\nBill Per Person: ₹{finalBillAmount} ")

