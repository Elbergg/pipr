from post import Package
import pytest

def test_create_package():
    package = Package("tomek", "zuzia", (1, 2, 3), 5)
    assert package.sender() == "tomek"
    assert package.recipient() == "zuzia"
    assert package.size() == (1, 2, 3)
    assert package.weigth() == 5

def test_size_negative():
    with pytest.raises(ValueError):
        package = Package("tomek", "zuzia", (1, -2, 3), 5)

def test_size_smallest():
    package = Package("tomek", "zuzia", (1, 2, 3), 5)
    assert package.smallest_size_parameter() == 1

def test_size_biggest():
    package = Package("tomek", "zuzia", (1, 2, 3), 5)
    assert package.biggest_size_parameter() == 3

def test_disct():
    package = Package("tomek", "zuzia", (1, 2, 3), 5)
    assert str(package) == 'The package was sent by tomek to zuzia. Its size is 1 length, 2 width, and 3 height. It weighs 5 kg.'


