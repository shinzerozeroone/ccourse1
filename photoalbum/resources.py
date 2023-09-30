from import_export import resources
from .models import Contact, Category


class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category