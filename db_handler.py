from math import sqrt, pow
import functools
from api.models import Hospital


def add_hospital(hosp_dict):
    h = Hospital(**hosp_dict)
    h.save()


def get_by_field(field, value):
    """" 
    Return all hospitals with field: value
    """
    hospitals = Hospital.objects.filter(**{field: value})
    return hospitals

def get_all():
    hospitals = Hospital.objects.all()
    return hospitals


def get_nearest_places(n_loc, e_loc, num):
    """" 
    Return nearest num hospitals to the given location
    """
    hospitals = get_all()
    def compare_hospitals(h1, h2):
        h1_dist = cal_distance(n_loc, e_loc, h1.north_loc, h1.east_loc)
        h2_dist = cal_distance(n_loc, e_loc, h2.north_loc, h2.east_loc)
        return h1_dist - h2_dist
    hospitals = sorted(hospitals, key=functools.cmp_to_key(compare_hospitals))
    return hospitals[:num]


def get_by_radius(north_loc, east_loc, radius):
    """" 
    Return all hospitals inside the given radius from the given location
    """
    nearest_hospitals = []
    hospitals = get_all()
    for h in hospitals:
        if cal_distance(north_loc, east_loc, h.north_loc, h.east_loc) <= int(radius):
            nearest_hospitals.append(h)
    print(nearest_hospitals)
    return nearest_hospitals


def get_er_types():
    return Hospital.ER_TYPE.choices


def get_care_choices():
    return Hospital.CARE_CHOICES.choices


def get_district_choices():
    return Hospital.DISTRICTS.choices


def cal_distance(n_loc, e_loc, other_n_loc, other_e_loc):
    print(other_n_loc)
    print(n_loc)

    print(sqrt(pow(int(n_loc) - int(other_n_loc), 2) + pow(int(e_loc) - int(other_e_loc), 2))/100000000)
    return sqrt(pow(int(n_loc) - int(other_n_loc), 2) + pow(int(e_loc) - int(other_e_loc), 2))/100000000


