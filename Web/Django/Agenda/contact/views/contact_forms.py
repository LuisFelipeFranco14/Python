from django.shortcuts import render, redirect
from contact.models import Contact
from contact.forms import ContactForm
from django.urls import reverse

# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context
        )
    else:
        context = { 
                'form': ContactForm()
            }

        return render(
            request,
            'contact/create.html',
            context
        )