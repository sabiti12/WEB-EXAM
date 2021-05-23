from django.contrib import admin
from .models import participant,program,Contact

# Register your models here.
admin.site.register(participant)
admin.site.register(program)
admin.site.register(Contact)