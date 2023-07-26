from django.shortcuts import render, redirect

from.models import Information
from.forms import InformationForm

# Create your views here.

def home(request):
    return render(request, 'reg/home.html')

def info(request, information_id):
    info = Information.objects.by(id=information_id)
    entries =info.entry_set.order_by('-date_added')
    context = {"info": info , 'entries':entries}
    return render(request, "reg/info.html" ,context)
   
""" A context is a
dictionary in which the keys are names well use in the template to access
the data, and the values are the data we need to send to the template."""

def new_info(request):
    if request.method != 'POST':
        form=InformationForm()
        #No data submitted; create a blank form.
       
    
    else:
        # POST data submitted; process data
        form = InformationForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('reg:info')

    context = {'form' : form}
    return render(request, 'reg/new_info.html',context )



   



