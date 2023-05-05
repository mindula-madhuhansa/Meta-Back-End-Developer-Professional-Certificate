# cast coffee, sandwich, cake types to float
coffee = float(input('1 coffee @: $ '))
sandwich = float(input('1 sandwich @: $ '))
cake = float(input('1 cake @: $ '))

bill_total = coffee + sandwich + cake

# print rounded total
print(f'Your total bill is $', round(bill_total, 2))
