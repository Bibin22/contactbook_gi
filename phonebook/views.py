from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages
from datetime import datetime
from .models import *
from .forms import *


def contact_add(request):
    template_name = 'phonebook/contact_add.html'
    form = ContactForm()
    context = {'form': form}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.created_user = str(request.user)
            data.save()
            messages.success(request, 'Contact Details Successfully Added.', 'alert-success')
            return redirect('contact_list')
        else:
            context = {'form': form}
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)


def contact_list(request):
    template_name = 'phonebook/contact_list.html'
    contact_list = ContactBook.objects.all()
    context = {'contact_list':contact_list}
    return render(request, template_name, context)


def contact_details(request, pk):
    template_name = 'phonebook/contact_details.html'
    contact_details = ContactBook.objects.get(contact_id=pk)
    context = {'contact':contact_details}
    return render(request, template_name, context)


def contact_delete(request):
    pk = request.GET.get('delete_id')
    ContactBook.objects.get(contact_id=pk).delete()
    messages.success(request, 'Contact details are deleted..', 'alert-success')
    return redirect('contact_list')


def contact_edit(request, pk):
    template_name = 'phonebook/contact_edit.html'
    contact = ContactBook.objects.get(contact_id=pk)
    form = ContactForm(instance=contact)
    context = {'form': form, 'contact': contact}
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            data = form.save(commit=False)
            data.updated_user = str(request.user)
            data.updated_at = datetime.now()
            data.save()
            messages.success(request, 'Contact Details Successfully Updated.', 'alert-success')
            return redirect('contact_list')
        else:
            context = {'form': form}
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            return render(request, template_name, context)
    return render(request, template_name, context)
