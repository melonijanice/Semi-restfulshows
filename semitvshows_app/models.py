import datetime
from django.db import models
from datetime import datetime
from pytz import timezone
from time import strftime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        fmt = "%Y-%m-%d"
        now_Eastern = datetime.now(timezone('UTC')).astimezone(timezone('US/Eastern'))
        source_date = now_Eastern.strftime(fmt)
        source_date=datetime.strptime(source_date, "%Y-%m-%d")
        dt_object = datetime.strptime(postData['release_date'], "%Y-%m-%d")
        all_shows=Show.objects.all()
        for show in all_shows:
            if postData['title']== show.title:
                errors["title_unique"]="show title should be unique"
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show Network should be at least 3 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show Network should be at least 3 characters"
        if dt_object >= source_date:
            errors["release_date"]="Show release date should be in the past"
        if len((postData['description'].strip())) >0:
            if len(postData['description'])<10:
                errors["description"] = "Show Description is optional, If provided then atleast provide 10 characters"
        return errors
class Show(models.Model):
    title = models.CharField(max_length=50,unique=True)
    network = models.CharField(max_length=50)
    release_date=models.DateTimeField()
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = ShowManager()


