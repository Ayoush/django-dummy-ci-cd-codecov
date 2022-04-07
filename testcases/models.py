from django.db import models
from django.template.defaultfilters import slugify

class Org(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    slug = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Org, self).save(*args, **kwargs)