from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from  .forms import ContactForm
# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import RegisterForm 
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('contact')
    else:
        form = RegisterForm()

    return render(request, 'register.html',{'form':form})    
@login_required
def contact_view(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            # Process the data
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            message=form.cleaned_data['message']
            # Normally, you would sate to a database or send to an email
            return render(request,'thanks.html',{'name': name})
    else:
        form=ContactForm()
    return render(request,'contact.html',{'form': form})