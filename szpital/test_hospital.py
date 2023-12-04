from hospital import Hospital, Patient, NoMoreBedsError
import pytest


def test_create_hospital():
    hospital = Hospital('warsaw', 1800, 400, 2200, 200)

def test_patient_where_to_put():
    warszawa = Hospital('warszawa', 1800, 400, 2200, 200)
    siedlce = Hospital('siedlce', 335, 110, 455, 40)
    radom = Hospital('radom', 300, 90, 200, 25)
    patient = Patient('siedlce', True, False)
    assert patient.where_to_put([warszawa, radom, siedlce]) == 'siedlce'

def test_patient_where_to_put_not_enough_beds():
    warszawa = Hospital('warszawa', 1800, 400, 2200, 200)
    siedlce = Hospital('siedlce', 0, 0, 455, 40)
    radom = Hospital('radom', 300, 90, 200, 25)
    patient = Patient('siedlce', True, False)
    assert patient.where_to_put([warszawa, radom, siedlce]) == 'warszawa'

def test_beds_decrease():
    warszawa = Hospital('warszawa', 1800, 400, 2200, 200)
    siedlce = Hospital('siedlce', 335, 110, 455, 40)
    radom = Hospital('radom', 300, 90, 200, 25)
    patient = Patient('siedlce', True, False)
    patient.where_to_put([warszawa, radom, siedlce])
    assert siedlce.covid_patients_beds == 334
    assert siedlce.covid_patients_beds_oiom == 110
def test_beds_decrease_only_oiom_left():
    warszawa = Hospital('warszawa', 1800, 400, 2200, 200)
    siedlce = Hospital('siedlce', 10, 10, 455, 40)
    radom = Hospital('radom', 300, 90, 200, 25)
    patient = Patient('siedlce', True, False)
    patient.where_to_put([warszawa, radom, siedlce])
    assert siedlce.covid_patients_beds == 9
    assert siedlce.covid_patients_beds_oiom == 9

def test_no_beds():
    with pytest.raises(NoMoreBedsError):
        warszawa = Hospital('warszawa', 0, 0, 2200, 200)
        siedlce = Hospital('siedlce', 0, 0, 455, 40)
        radom = Hospital('radom', 0, 0, 200, 25)
        patient = Patient('siedlce', True, False)
        patient.where_to_put([warszawa, radom, siedlce])

