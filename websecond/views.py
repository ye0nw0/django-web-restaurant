from django.shortcuts import render
from websecond.models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
# Create your views here.

def list(request):
    context = {
        'items' : Post.objects.all()
    }
    return render(request, 'websecond/list.html', context)


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            new_item = form.save()
        return HttpResponseRedirect('/websecond/list/')

    form = PostForm()
    return render(request, 'websecond/create.html', {'form' : form})


def confirm(request):
    form = PostForm(request.POST)
    if form.is_valid():
        return render(request, 'websecond/confirm.html', {'form' : form})
    return HttpResponseRedirect('/websecond/create/')