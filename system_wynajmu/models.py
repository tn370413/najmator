from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = (
    ('m', 'mieszkanie'),
    ('p', 'pokój'),
    ('d', 'dom'),
)

class Estate(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    area = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Contract(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    price = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)

def estate_photo_path(instance, filename):
    print(instance)
    return 'estate_photos/{0}/{1}'.format(instance.estate_id, filename)

class Photograph(models.Model):
    photograph = models.ImageField(upload_to=estate_photo_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    estate_id = models.ForeignKey(Estate, on_delete=models.CASCADE)
