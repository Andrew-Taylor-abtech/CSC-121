while True:
    name = input("Please enter your name or 'q' to quit ")
    if name.lower() == 'q':
        break
    
    print(f"Howdy, {name}!")
    
    with open('guest_book.txt', 'a') as path:
        path.write(name + "\n")