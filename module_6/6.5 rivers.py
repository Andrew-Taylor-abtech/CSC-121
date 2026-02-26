rivers = {
    'Nile': 'Egypt', 
    'Amazon': 'Brazil', 
    'French Broad': 'the United States',
    }
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
print()    
for river in rivers:
    print(river)
print() 
for country in rivers.values():
    print(country.title())
