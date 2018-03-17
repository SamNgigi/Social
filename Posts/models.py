# POST APP MODELS
from django.db import models
from django.core.urlresolvers import reverse
# from django.conf import settings

import misaka

from Hood.models import Hood

from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    content.html = models.TextField(editable=False)
    hood = models.ForeignKey(Hood, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.content

    # Method saves a user's post and handles the markdown
    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',
                       kwargs={'username': self.user.username,
                               'pk': self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'content']
