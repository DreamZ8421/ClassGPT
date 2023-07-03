from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'
#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #major = models.TextField(max_length=500, blank=True)
    #ID = models.IntegerField(max_length=9, blank=True)
    #graduation_year = models.IntegerField(max_length=4, blank=True)
    #school = models.TextField(max_lenght=30,blank=True)
    

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
   # instance.profile.save()