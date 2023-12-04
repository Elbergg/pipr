import pytest
from price import Price

def test_convert():
    price = Price(100, 'usd')
    price.convert('eur')
    assert price.currency == 'eur'
    assert price.value == 80

def test_conver_eur_to_pln():
    price = Price(100, 'eur')
    price.convert('pln')
    assert price.currency == 'pln'
    assert price.value == 500

def test_add_in_eur():
    price = Price(50, 'pln')
    price2 = Price(50, 'pln')
    assert price.add(price2,'eur').value == 20

def test_sub_in_eur():
    price = Price(200, 'pln')
    price2 = Price(100, 'pln')
    assert price.sub(price2,'eur').value == 20

def test_mul():
    price = Price(100, 'pln')
    price*2
    assert price.value == 200

def test_rmul():
    price = Price(100, 'pln')
    price*2
    assert price.value == 200

def test_str():
    price = Price(100, 'pln')
    assert str(price) == '1.00 pln'