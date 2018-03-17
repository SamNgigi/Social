from django.contrib import admin
from . import models
# Register your models here.

"""
This is tabular inline class that allows us to utilize the admin interface with
the ability to edit models in the same page as the parent model.

Kinda like what we have learnt previously with Tribune Tags and Article models.

So below we are connecting the HoodMember class to the Hood class so
hat we can edit hood members on the Hood model page.
"""


class HoodMemberInLine(admin.TabularInline):
    model = models.HoodMember


admin.site.register(models.Hood)
