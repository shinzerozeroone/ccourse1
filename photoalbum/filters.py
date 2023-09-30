import django_filters
from .models import Category

class CategotyFilter(django_filters.FilterSet):

     class Meta:
         model = Category
         fields = ('name', 'max_length')
