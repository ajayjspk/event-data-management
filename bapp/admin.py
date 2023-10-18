from django.contrib import admin
from .models import Events, feedback
from .models import Register, eve_register, RegisterOrganizer

# Register your models here.
admin.site.register(Events)
admin.site.register(Register)
admin.site.register(eve_register)
admin.site.register(feedback)
admin.site.register(RegisterOrganizer)
