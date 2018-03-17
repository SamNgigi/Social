# HOOD MODELS
from django.db import models
"""
Slugify takes a string and makes it usable as part of a url.
For example a string with spaces would be joined with dashes and
transformed to lowercase.
"""
from django.utils.text import slugify
import misaka

from django.contrib.auth.models import User

# from django.urls import reverse
from django.core.urlresolvers import reverse
from django import template
register = template.Library()
# Create your models here.


class Hood(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='Hoodmember')

    # String representation of the Hood object
    def __str__(self):
        return self.name

    # Our save hood method.
    def save(self, *args, **kwargs):
        """
        Here we want to take in neighbourhood names  and make them
        usable as part of our urls.
        """
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hood:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class HoodMember(models.Model):
    """
    Remember the;

    from django import template
    register = template.Library()

    This allows us to connect a post to a group member using the related
    name'user_hood'
    """

    hood = models.ForeignKey(Hood, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_hood')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('hood', 'user')
