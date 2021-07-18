from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from rest_framework.parsers import JSONParser
from .models import aboutMe, contactForm, websiteDetail,socialLink
from .forms import ContactForm, websiteDetailForm
from .serializers import websiteSerializer
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def UserViewSet(request, id=0):
    if request.method == 'GET':
        queryset = websiteDetail.objects.all()
        serializer_class = websiteSerializer(queryset, many=True)
        return JsonResponse(serializer_class.data, safe=False)

    elif request.method == 'POST':
        websiteData = JSONParser.parse(request)
        serializer_class = websiteSerializer(data = websiteData)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse('Added Successfully!', safe=False) 
        return JsonResponse('Failed to Add', safe=False)

    elif request.method == 'PUT':
        websiteData = JSONParser.parse(request)
        website = websiteDetail.objects.get(id = websiteData['id'])
        serializer_class = websiteSerializer(website, data = websiteData)
        if serializer_class.is_valid():
            serializer_class.save()
            return JsonResponse('Updated Successfully!', safe=False) 
        return JsonResponse('Failed to Update', safe=False)
        
    elif request.method == 'DELETE':
        website = websiteDetail.objects.get(id = id)
        website.delete()
        return JsonResponse('Deleted Successfully!', safe=False) 
