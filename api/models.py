from django.contrib.auth.models import User
from django.db import models

class Script(models.Model):
    name = models.SlugField(primary_key=True, max_length=30)
    admins = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name

class Version(models.Model):
    script = models.ForeignKey(Script)
    version = models.CharField(max_length=30)
    
    def __unicode__(self):
        return u'%s %s' % (self.script, self.version)
