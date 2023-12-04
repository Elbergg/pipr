class Hospital():
    def __init__(self, city, covid_patients_beds, covid_patients_beds_oiom, norm_patients_beds, norm_patients_beds_oiom):
        self.city = city
        if not isinstance(self.city, str):
            raise ValueError
        self.covid_patients_beds = covid_patients_beds
        self.covid_patients_beds_oiom = covid_patients_beds_oiom
        if self.covid_patients_beds_oiom > self.covid_patients_beds:
            raise ValueError
        self.normal_patients_beds = norm_patients_beds
        self.normal_patients_beds_oiom = norm_patients_beds_oiom
        if self.normal_patients_beds_oiom > self.normal_patients_beds:
            raise ValueError
class NoMoreBedsError(Exception):
    def __init__(self):
        super().__init__('There are no more valid beds in the mazovian hospitals')
class Patient():
    def __init__(self, home, has_covid, oiom_required):
        self.home = home
        self.has_covid = has_covid
        self.oiom_required = oiom_required
        if self.home == 'warszawa':
            self.nearest_hospitals = ['warszawa', 'siedlce', 'radom']
        elif self.home == 'siedlce':
            self.nearest_hospitals = ['siedlce', 'warszawa', 'radom']
        elif self.home == 'radom':
            self.nearest_hospitals = ['radom', 'warszawa', 'siedlce']
    def where_to_put(self, hospital_list):   
        for hospital_name in self.nearest_hospitals:
            for hospital in hospital_list:
                if hospital_name == hospital.city:
                    if self.requirements_met(hospital):
                        return hospital.city 
        raise NoMoreBedsError
    def requirements_met(self, hospital):
        if self.has_covid is True and self.oiom_required is True:
            if hospital.covid_patients_beds_oiom > 0:
                hospital.covid_patients_beds_oiom -= 1
                hospital.covid_patients_beds -= 1
                return True
        elif self.has_covid is True and self.oiom_required is False:
            if hospital.covid_patients_beds > 0:
                if hospital.covid_patients_beds > hospital.covid_patients_beds_oiom:
                    hospital.covid_patients_beds -= 1
                else:
                    hospital.covid_patients_beds_oiom -= 1
                    hospital.covid_patients_beds -= 1
                return True
        elif self.has_covid is False and self.oiom_required is True:
            if hospital.normal_patients_beds_oiom > 0:
                hospital.normal_patients_beds_oiom -= 1
                hospital.normal_patients_beds -= 1
                return True
        elif self.has_covid is False and self.oiom_required is False:
            if hospital.normal_patients_beds > 0:
                if hospital.normal_patients_beds > hospital.normal_patients_beds_oiom:
                    hospital.normal_patients_beds -= 1
                else:
                    hospital.normal_patients_beds_oiom -= 1
                    hospital.normal_patients_beds -= 1
                return True
    # def next_nearest_hospital(self, hospital_list):
    #     for hospital_name in self.nearest_hospitals:
    #         for hospital in hospital_list:
    #             if hospital_name == hospital.city:
    #                 if self.requirements_met(hospital):
    #                     return hospital.city       


