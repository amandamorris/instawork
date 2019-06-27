from django.db import models
from django.utils.timezone import now


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10) # maybe want to implement this as PhoneNumberField
    role = models.CharField(max_length=20)
    created = models.DateTimeField('date created', default=now)
    last_modified = models.DateTimeField('date last modified', default=now)

    def __str__(self):
        return self.first_name + " " + self.last_name

# TODO: want to implement role as enumeration
# TODO: want to implement teamId?
