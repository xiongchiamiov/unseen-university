from django.contrib.auth.models import User
from django.db import models

from semantic_version import django_fields as semVer

class Script(models.Model):
    name = models.SlugField(primary_key=True, max_length=30)
    admins = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name
    
    def humanReadable(self):
        return {
            'name': self.name,
            'version': unicode(self.latest_version().version),
            'admins': [unicode(user) for user in self.admins.all()],
        }
    
    def latest_version(self):
        return sorted(self.version_set.all())[-1]

class Version(models.Model):
    script = models.ForeignKey(Script)
    version = semVer.VersionField(coerce=True, max_length=30)
    
    def __unicode__(self):
        return u'%s %s' % (self.script, self.version)
    
    def __cmp__(self, other):
        # Take advatage of semantic_version's sorting logic.
        return self.version.__cmp__(other.version)

