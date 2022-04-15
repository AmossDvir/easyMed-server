from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField


class User(AbstractUser):
    pass
    
class Hospital(models.Model):
    class ER_TYPE(models.IntegerChoices):
        ALL = 0, "All Institutes"
        HOS = 1, "Hospital"
        BIKUR = 2, "Bikur Rofe"
        TEREM = 3, "Terem"
    
    class CARE_CHOICES(models.IntegerChoices):
        ALL = 0, "All Types"
        BROKEN_BONE = 1, "Broken bone"
        CUT = 2, "Cut"
        RASH = 3, "Rash"
        ALLERGY = 4, "Non lethal allergy"
        BREATH = 5, "Shortness of breath"
        CHEST = 6, "Chest pain"
        FLU = 7, "Flu"

    class DISTRICTS(models.IntegerChoices):
        NORTH = 1, "North",
        CENTER = 2, "Center",
        JERUSALEM = 3, "Jerusalem"
        SOUTH = 4, "South"


    # our variables:
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=12)
    north_loc = models.IntegerField()
    east_loc = models.IntegerField()
    district = models.IntegerField(choices=DISTRICTS.choices, default=DISTRICTS.JERUSALEM)
    min_till_doctor = models.IntegerField()
    is_private = models.BooleanField()
    er_type = models.PositiveSmallIntegerField(choices=ER_TYPE.choices, default=ER_TYPE.ALL)
    care_fields = MultiSelectField(choices=CARE_CHOICES.choices, default=CARE_CHOICES.ALL)
