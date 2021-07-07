from django.contrib import admin
from .models import aboutMe, contactForm, socialLink, websiteDetail

# Register your models here.
admin.site.register(websiteDetail)
admin.site.register(socialLink)
admin.site.register(aboutMe)
admin.site.register(contactForm)