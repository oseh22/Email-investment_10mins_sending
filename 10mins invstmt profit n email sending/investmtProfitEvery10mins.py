import time

# input investment amount 
amount = float(input("Enter amount:N "))
# 10 percent convert to decimal
percentage = 0.10  # 

while True:
    # multiply amount and percentage
    total = amount * percentage
    
    # Update the total investment amount
    amount += total
    
    # Print the current investment amount with addition of 10%
    print(f" 10% add to amount: N{amount:,.2f}")
    
    # Wait for 5 minutes and add 10%
    time.sleep(60)  # 5 minutes