from django.shortcuts import render
from new_app.models import Topic,webpage,Record
from new_app import forms

# Create your views here.
def index(request):
    dic={'insert index':'FIRST APP'}#it will be passed to template
    webpage_list= Record.objects.order_by('date')
    date_dic={'records':webpage_list}

    return render(request,'first_app/index.html',context=date_dic)
#requet is for http firs_app/index.html.and context will be passed onto the template

def form_name_view(request):
    form=forms.FormName()
    if request.method =='POST':
        form=forms.FormName(request.POST)# if it post the data the data will be displayed on the terminal
        if form.is_valid():
            print("validate")
            print('name',form.cleaned_data['name'])
            print('EMAIL', form.cleaned_data['email'])
            print('TEXT', form.cleaned_data['text'])
            print('bot', form.cleaned_data['botcatcher'])
    return render(request,'first_app/forms.html',{'form':form})

def other(request):
    return render(request, 'first_app/other.html')
def url(request):
    return render(request, 'first_app/url.html')