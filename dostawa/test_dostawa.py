import pytest
from dostawa import Delivery

def test_delivery():
    delivery = Delivery()
    delivery.submit_order('Kraków')
    assert delivery.target == 'Kraków'
    assert delivery.distance == 290
    delivery.drive(1)
    assert delivery.distance == 210
    str(delivery)
    delivery.drive(2)
    delivery.rest(3)
    delivery.drive(1)
    delivery.drive(2)
    assert delivery.target == 'Warszawa'