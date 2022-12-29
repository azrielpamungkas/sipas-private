from django.contrib import admin
from .models import IncomingMail, OutgoingMail
# Register your models here.
admin.site.register(IncomingMail)
admin.site.register(OutgoingMail)
