from app import greet


def test_greet():
    assert greet("Ahmed") == "Hello Ahmed"