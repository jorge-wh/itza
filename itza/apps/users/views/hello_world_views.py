from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django import forms
from django.shortcuts import render, reverse
from django.conf import settings


def index(request):

    form = IndexForm(request.POST or None, initial={'room': 'pycun'})

    if request.POST:
        if form.is_valid():
            username = form.cleaned_data['username']
            room = form.cleaned_data['room']
            return HttpResponseRedirect(F"{reverse('room', args=[room])}?username={username}")

    return render(request, 'chat/index.html', {
        'form': form,
    })


class IndexForm(forms.Form):

    username = forms.CharField(label='Usuario', max_length=50)
    room = forms.CharField(label='Sala', max_length=50)


