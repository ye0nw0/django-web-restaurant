from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from django import forms
from webthird.models import Restaurant, Review
from django.utils.translation import gettext_lazy as _

REVIEW_POINT_CHOICES =(
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['point', 'comment', 'restaurant']
        labels = {
            'point' : _('평점'),
            'comment' : _('댓글'),
        }
        help_texts = {
            'name' : _('평점을 입력하세요.'),
            'comment' : _('댓글을 입력하세요.'),
        }
        widgets = {
            'restaurant' : forms.HiddenInput(),
            'point' : forms.Select(choices=REVIEW_POINT_CHOICES)
        }


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']
        labels = {
            'name' : _('이름'),
            'address' : _('주소'),
        }
        help_texts = {
            'name' : _('이름을 입력하세요.'),
            'address' : _('주소를 입력하세요.'),
        }
        error_messages = {
            'name' : {
                'max_length' : _('이름이 너무 깁니다.')
            }
        }