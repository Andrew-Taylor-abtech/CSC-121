def describe_city(city, country='Canada'):
    """Display information about a city."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('vancouver')
describe_city('toronto')
describe_city('Asheville', country='the United States')