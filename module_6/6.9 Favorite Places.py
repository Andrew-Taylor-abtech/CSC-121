favorite_places = { 
    'will': ['Asheville', 'Japan'],
    'marc': ['Vietnam'],
    'edwin': ['Calgary', 'Wilmington', 'Hawaii'],
    }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"{place.title()}")