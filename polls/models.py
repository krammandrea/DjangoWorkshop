from django.db import models
import datetime
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0) 

    # whenever an Author object is printed 
    def __unicode__(self):
        return self.name


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return timezone.now() > self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    # sorting self defined methods is not support, this is workaround
    # if you try to sort by was_published .. it will sort by pub_date
    was_published_recently.admin_order_field = 'pub_date'  
    was_published_recently.short_description = "Published recently?" #changes name of header from function name to defined string
    was_published_recently.boolean = True 


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField('choice', max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return "%s   votes:%s   quest:%s" %(self.choice_text, self.votes, self.poll.question)

