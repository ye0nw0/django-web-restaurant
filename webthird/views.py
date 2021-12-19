from django.core import paginator
from django.forms.widgets import NullBooleanSelect
from django.shortcuts import redirect, render, get_object_or_404
from webthird.models import Restaurant, Review
from django.core.paginator import Paginator
from webthird.forms import RestaurantForm, ReviewForm, RestaurantUpdateForm
from django.http import HttpResponseRedirect
from django.db.models import Count, Avg


def list(request):
    restaurants = Restaurant.objects.all().annotate(reviews_count=Count('review')).annotate(average_point=Avg('review__point'))
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
        password = request.POST.get('password', '')
        form = RestaurantUpdateForm(request.POST, instance=item)
        if form.is_valid() and password == item.password:
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


def delete(request,id):
    item = get_object_or_404(Restaurant, pk = id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')
        return redirect('restaurant-detail', id=id)
    return render(request, 'webthird/delete.html', { 'item' : item })


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('restaurant-detail', id = restaurant_id)

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant' : item})
    return render(request, 'webthird/review_create.html', {'form' : form, 'item' : item})


def review_delete(reqeust, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()

    return redirect('restaurant-detail', id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-created_at')
    paginator = Paginator(reviews, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews' : items
    }
    return render(request, 'webthird/review_list.html', context)