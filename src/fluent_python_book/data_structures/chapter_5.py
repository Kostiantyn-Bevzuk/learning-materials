from typing import NamedTuple


class City(NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City("Asia", "Tokyo", "JP"),
    City("Asia", "Delhi", "IN"),
    City("North America", "Mexico City", "MX"),
    City("North America", "New York", "US"),
    City("South America", "São Paulo", "BR"),
]

# Keyword matching


def match_asian_cities() -> list[City]:
    results = []
    for city in cities:
        match city:
            case City(continent="Asia"):
                results.append(city)
    return results


def match_asian_countries() -> list[str]:
    results = []
    for city in cities:
        match city:
            case City(
                continent="Asia", country=cc
            ):  # here we can assign any var, for example country=country
                results.append(cc)
    return results


# Positional matching


def match_asian_cities_pos() -> list[City]:
    results = []
    for city in cities:
        match city:
            case City("Asia"):
                results.append(city)
    return results


def match_asian_countries_pos() -> list[str]:
    results = []
    for city in cities:
        match city:
            case City("Asia", _, country):
                results.append(country)
    return results
