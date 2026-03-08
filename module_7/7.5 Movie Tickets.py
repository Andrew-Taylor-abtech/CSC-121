tickets = int(input("How many movie tickets would you like to buy? "))
cost = 0
tickets_processed = 0

while tickets_processed < tickets:
    
    age = int(input(f"Enter the age of person {tickets_processed + 1}: "))
    
    if age < 3:
        price = 0
        print("Ticket is free!")
    elif age <= 12:  
        price = 10
        print("Ticket is $10")
    else:  
        price = 15
        print("Ticket is $15")
        
    cost += price
    
    tickets_processed += 1

print(f"\nYour total cost for {tickets} movie tickets is ${cost}.")