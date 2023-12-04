from art import Artist
import pytest

def test_create_artist():
    artist = Artist('tomek', 2004)
    assert artist.name() == 'tomek'
    assert artist.bday() == 2004

def test_crate_artist_name_not_str():
    with pytest.raises(ValueError):
        artist = Artist(2003, 2004)

def test_create_artist_bday_not_int():
    with pytest.raises(ValueError):
        artist = Artist('tomek', 'zuzia')


def test_set_artist_name():
    artist = Artist('tomek', 2004)
    assert artist.name() == 'tomek'
    artist.set_name('pawel')
    assert artist.name() == 'pawel'

def test_set_name_not_new_name():
    with pytest.raises(ValueError):
        artist = Artist('tomek', 2004)
        artist.set_name("")

def test_set_bday():
    artist = Artist('tomek', 2004)
    assert artist.bday() == 2004
    artist.set_birthday(2003)
    assert artist.bday() == 2003

    
