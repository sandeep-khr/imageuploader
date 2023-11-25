from django.urls import path
from .views import api_image_list, api_image_create, api_image_detail 

urlpatterns = [
    path('images/', api_image_list, name='image-list-view'),
    path('images/create/', api_image_create, name='image-list-create'),
    path('images/<int:pk>/', api_image_detail, name='image-detail')
]
