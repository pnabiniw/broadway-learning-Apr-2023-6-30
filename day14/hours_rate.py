hours = float(input("Enter hours "))
rate = float(input("Enter rate "))

if hours <= 40:
    pay = hours * rate
else:
    ot = hours - 40
    pay = 40 * rate
    pay = pay + ot * rate * 1.5
print("Payment received is ", pay)
