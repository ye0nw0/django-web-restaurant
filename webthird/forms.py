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
        fields = ['name', 'address', 'image', 'password']
        labels = {
            'name' : _('이름'),
            'address' : _('주소'),
            'image' : _('이미지 url'),
            'password' : _('게시물 비밀번호'),
        }
        help_texts = {
            'name' : _('이름을 입력하세요.'),
            'address' : _('주소를 입력하세요.'),
            'image' : _('이미지의 url을 입력해주세요.'),
            'password' : _('게시물 비밀번호를 입력해주세요.'),
        }
        widgets = {
            'password' : forms.PasswordInput()
        }
        error_messages = {
            'name' : {
                'max_length' : _('이름이 너무 깁니다.')
            },
            'image' : {
                'max_length' : _('이미지 주소가 너무 깁니다. 500자 이하로 입력해주세요.')
            },
            'password' : {
                'max_length' : _('비밀번호가 너무 깁니다. 20자 이하로 설정해주세요.')
            },
        }

class RestaurantUpdateForm(RestaurantForm):
    class Meta:
        model = Restaurant
        exclude = ['password']