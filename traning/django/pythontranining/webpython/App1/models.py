from django.db import models
import uuid
# Create your models here.

class table(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null = True, blank = True)
    demo_link = models.CharField(max_length = 2000, null=True, blank=True)
    source_link = models.CharField(max_length = 2000, null=True, blank=True)
    tags = models.ManyToManyField('Tags', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default = 0, null = True, blank=True)
    created = models.TimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable = False)
    

    def __str__(self):
        return self.title

class reviews(models.Model):
    VOTE = (
        ('up', 'up vote'),
        ('down', 'down vote'),
    )
    project = models.ForeignKey(table, on_delete = models.CASCADE)
    body=models.TextField(null =True, blank =True)
    value = models.CharField(max_length=200, choices =VOTE)
    created =  models.TimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True )

    def __str__(self):
        return self.value

class Tags(models.Model):
    name = models.CharField(max_length= 200)
    created =  models.TimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True )
    
    def __str__(self):
        return self.name