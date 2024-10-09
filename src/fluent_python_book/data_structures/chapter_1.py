import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

# print(len(suit_values))


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(f"rank_value: {rank_value}")
    print(suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]


# print(spades_high(Card("A", "spades")))

# for card in sorted(deck, key=spades_high):
#     print(card)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(3, 4)
v2 = Vector(3, 5)


# print(__name__)
# x = "ABC"
# codes = [ord(x) for x in x]

# codes = [last := ord(x) for x in x]
# print(last)

metro_areas = [
    ("Tokyo", "JP", 36.933, (35.689722, 139.691667)),
    ("Delhi NCR", "IN", 21.935, (28.613889, 77.208889)),
    ("Mexico City", "MX", 20.142, (19.433333, -99.133333)),
    ("New York-Newark", "US", 20.104, (40.808611, -74.020386)),
    ("São Paulo", "BR", 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f"{name:15} | {lat:9.4f} | {lon:9.4f}")


# if __name__ == "__main__":
#     main()


def match_phone_number(phone):
    match tuple(phone):
        case ["1", *rest]:  # North America and Caribbean
            # handle North America and Caribbean case
            print("North America and Caribbean")
        case ["2", *rest]:  # Africa and some territories
            # handle Africa and some territories case
            print("Africa and some territories")
        case ["3" | "4", *rest]:  # Europe
            # handle Europe case
            print("Europe")
        case _:  # Default case for other regions
            # handle other cases
            ...


# Example usage
# phone_number = '3234567890'
# match_phone_number(phone_number)


# Slicing

slice_1 = slice(0, 2)

custom_list = [1, 2, 3, 4, 5]

# print(custom_list[slice_1])
# print(custom_list.__getitem__(slice_1))
