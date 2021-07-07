from django import forms
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from .models import aboutMe, contactForm, websiteDetail,socialLink
from .forms import ContactForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import websiteSerializer


# Create your views here.
def index(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    baseUrl='https://source.unsplash.com/'
    return render(request,'index.html',{
        'baseUrl':baseUrl,
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData

    })
def gallery(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    baseUrl='https://source.unsplash.com/'
    return render(request,'gallery.html',
    {
        'numbers':range(1,10),
        'baseUrl':baseUrl,
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData
    })

def about(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all()
    aboutme = aboutMe.objects.all()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    return render(request,'about.html',
    {
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData,
        'aboutMe': aboutme
    })
def contact(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            recipients = ['info@example.com']
            reg = contactForm(name=name, phone=phone, subject=subject,message=message,sender=sender)
            reg.save()
            # send_mail(subject, message, sender, recipients)
            return redirect('submit-success')
        # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()
    return render(request,'contact.html',
    {
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData,
        'form': form
    })
def blog(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    return render(request,'blog.html',
    {
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData
    })

def submit_success(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    return render(request,'form-success.html',
    {
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData
    })

class UserViewSet(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get(self, request):
        queryset = websiteDetail.objects.all()
        serializer_class = websiteSerializer(queryset, many=True)
        return Response(serializer_class.data)
    def post(self):
        pass