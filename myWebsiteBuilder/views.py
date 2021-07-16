from django.shortcuts import redirect, render
from rest_framework.fields import NullBooleanField, empty
from rest_framework.views import APIView
from .models import aboutMe, contactForm, websiteDetail,socialLink
from .forms import ContactForm, websiteDetailForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import websiteSerializer


# Create your views here.
def websiteDetails(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = websiteDetailForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            category = form.cleaned_data['category']
            websiteName = form.cleaned_data['websiteName']
            fbLink = form.cleaned_data['fbLink']
            twittterLink = form.cleaned_data['twittterLink']
            googleLink = form.cleaned_data['googleLink']
            gitLink  = form.cleaned_data['gitLink']
            linkedinLink = form.cleaned_data['linkedinLink']
            InstaLink = form.cleaned_data['InstaLink']
            homepageContent = form.cleaned_data['homepageContent']
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            reg1 = websiteDetail(category=category, websiteName=websiteName, homepageContent=homepageContent)
            reg1.save()
            reg2 = socialLink(fbLink=fbLink, twittterLink=twittterLink, googleLink=googleLink, gitLink=gitLink, linkedinLink=linkedinLink, InstaLink=InstaLink)
            reg2.save()
            reg3 = aboutMe(title=title, body=body)
            reg3.save()
            return redirect('index-page')
    else:
        form=websiteDetailForm()
    return render(request,'websiteDetails.html',{
        'form':form
    })
def index(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all().last()
    dataCount=data.count()
    baseUrl='https://source.unsplash.com/'
    lastIndex = data[dataCount-1]
    return render(request,'index.html',{
        'baseUrl':baseUrl,
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData,
        'checkBlink':data.last().homepageContent
    })
    

def gallery(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all().last()
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
    socialLinkData = socialLink.objects.all().last()
    aboutme = aboutMe.objects.all().last()
    dataCount=data.count()
    lastIndex = data[dataCount-1]
    return render(request,'about.html',
    {
        'websiteData': data,
        'lastIndex': lastIndex,
        'socialLink':socialLinkData,
        'aboutMe': aboutme,
    })
def contact(request):
    data = websiteDetail.objects.all()
    socialLinkData = socialLink.objects.all().last()
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
    socialLinkData = socialLink.objects.all().last()
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
    socialLinkData = socialLink.objects.all().last()
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
