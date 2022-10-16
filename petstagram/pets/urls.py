from django.urls import path, include

from petstagram.pets import views
from petstagram.pets.views import add_pet, details_pet, edit_pet, delete_pet

urlpatterns = [
    path('add/', add_pet, name = 'add pet'),
    path('<username>/pet/<slugname>/', include([
        path('', details_pet, name= 'details pet'),
        path('edit/', edit_pet, name = 'edit pet'),
        path('delete/', delete_pet, name= 'delete pet')
    ]))
]