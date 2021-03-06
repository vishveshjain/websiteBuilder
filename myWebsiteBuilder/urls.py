from django.urls import path
from . import views

urlpatterns = [
    path('',views.websiteDetails, name='website-details'),
    path('index/',views.index, name='index-page'),
    path('gallery/',views.gallery, name='gallery'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('blog/',views.blog,name='blog'),
    path('success',views.submit_success,name='submit-success'),
    path('api/',views.UserViewSet),
    path('api/<int:id>',views.UserViewSet),
]
