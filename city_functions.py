# 11.1
print("\n11.1")


def print_name(city, country, population=None):
    if population:
        formatted_name = f"{city}, {country} - populacja {population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()

