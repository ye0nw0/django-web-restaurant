from django.forms.widgets import NullBooleanSelect
from django.shortcuts import redirect, render, get_object_or_404
from webthird.models import Restaurant, Review
from django.core.paginator import Paginator
from webthird.forms import RestaurantForm, ReviewForm
from django.http import HttpResponseRedirect
# Create your views here.

def list(request):
    restaurants = Restaurant.objects.all()
    paginator = Paginator(restaurants, 5)

    page = request.GET.get('page')
    items = paginator.get_page(page)
    context = {
        'restaurants' : items
    }
    return render(request, 'webthird/list.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/webthird/list/')
    form = RestaurantForm()
    return render(request, 'webthird/create.html', {'form' : form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        #item = Restaurant.objects.get(pk = request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk = request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
    elif request.method == 'GET':
        item = get_object_or_404(Restaurant, pk = request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'webthird/update.html', {'form' : form})
    return HttpResponseRedirect('/webthird/list/')


def detail(request, id):
    if 'id' is not None:
        item = get_object_or_404(Restaurant, pk = id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'webthird/detail.html', {'item' : item, 'reviews' : reviews})
    return HttpResponseRedirect('/webthird/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk = request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/webthird/list/')


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id = restaurant_id)

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant' : item})
    return render(request, 'webthird/review_create.html', {'form' : form, 'item' : item})