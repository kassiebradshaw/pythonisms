import pytest

from pythonisms import Favorite

def test_favorite_str():
    favorites = Favorite()
    actual = str(favorites)
    expected = "Favorites"

def test_favorite_collection():
    favorites = Favorite()
    favorites.add("coffee")
    favorites.add("netflix")
    favorites.add("books")
    actual = len(favorites)
    expected = 3
    assert actual == expected

def test_for_in():
    favorites = Favorite()
    favorites.add("coffee")
    favorites.add("netflix")
    favorites.add("books")
    list = []
    for favorite in favorites:
        list.append(favorite)
    
    assert list == ["coffee", "netflix", "books"]

def test_length():
    favorites = Favorite()
    favorites.add("coffee")
    favorites.add("netflix")
    favorites.add("books")
    assert len(favorites) == 3

def test_list_comprehension():
    favorites = Favorite()
    favorites.add("coffee")
    favorites.add("netflix")
    favorites.add("books")

    uppercase = [favorite.upper() for favorite in favorites]
    assert uppercase == ["COFFEE", "NETFLIX", "BOOKS"]