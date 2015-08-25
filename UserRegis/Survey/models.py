from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms
from django.utils import timezone



# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    #user = models.ForeignKey(User)
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
        #return unicode(self.user)

    def save(self, *args, **kwargs):
     try:
        existing = UserProfile.objects.get(user=self.user)
        self.id = existing.id #force update instead of insert
     except UserProfile.DoesNotExist:
        pass
     models.Model.save(self, *args, **kwargs)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    from django.template.defaultfilters import slugify


   # User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Survey(models.Model):
    survey_name = models.CharField(max_length=200)
    end_date = models.DateTimeField('Complete by')
    survey_description=models.CharField(max_length=700)
    def __str__(self):              # __unicode__ on Python 2
        return self.survey_name

class SurveyFields(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=500)
    response = models.CharField(max_length=5000,default="NA")
    def __str__(self):              # __unicode__ on Python 2
        return self.question