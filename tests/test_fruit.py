import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


def my_fruit():
    return Fruit("apple")


def fruit_basket(my_fruit):
    print([Fruit("banana").name, my_fruit])
    return [Fruit("banana"), my_fruit]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
