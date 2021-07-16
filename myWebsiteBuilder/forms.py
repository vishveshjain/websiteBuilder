from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    phone = forms.CharField(max_length=12, required=False)
    sender = forms.EmailField()


category_choice=[
    ('art','Art'),
    ('blog','Blog'),
    ('technology','Technology'),
    ('music','Music'),
    ('food','Food'),
    ('photography','Photography'),
    ('education','Education'),
    ('real estate', 'Real Estate'),
    ('consulting service','Consulting Service'),
    ('podcast','Podcast'),
    ('legal','Legal'),
    ('finance', 'Finance'),
    ('animal','Animal'),
    ('news','News'),
    ('healthcare','Healthcare')
]
class websiteDetailForm(forms.Form):
    category = forms.CharField(label='Select website catogory',widget=forms.Select(choices=category_choice))
    websiteName = forms.CharField(label='Enter name of website', max_length=100)
    fbLink = forms.CharField(label='Enter Facebook link', max_length=250, required=False)
    twittterLink = forms.CharField(label='Enter twitter link', max_length=250, required=False)
    googleLink = forms.CharField(label='Enter google link', max_length=250, required=False)
    gitLink  = forms.CharField(label='Enter github link', max_length=250, required=False)
    linkedinLink = forms.CharField(label='Enter linkedIn link', max_length=250, required=False)
    InstaLink = forms.CharField(label='Enter Instagram link', max_length=250, required=False)
    homepageContent = forms.CharField(label='Enter homepage content', widget=forms.Textarea, required=False)
    title = forms.CharField(label='Enter about us heading', max_length=100, required=False)
    body = forms.CharField(label='Enter about us content', widget=forms.Textarea, required=False)