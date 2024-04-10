from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dogs/', views.dogs_index, name='index'),
    path('dogs/<int:dog_id>', views.dogs_detail, name='detail'),
    path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
    path('dogs/<int:pk>/delete/', views.DogDelete.as_view(), name='dogs_delete'),
    path('dogs/<int:pk>/update/', views.DogUpdate.as_view(), name='dogs_update'),
    path('accounts/signup/', views.signup, name='signup'),
    path('dogfood/create/', views.DogFoodCreate.as_view(), name='dogfood_create'),
    path('dogfood/<int:pk>', views.dogfood_detail, name='dogfood_detail'),
    path('dogfood/', views.DogFoodList.as_view(), name='dogfood_index'),
    path('dogfood/<int:pk>/update/', views.DogFoodUpdate.as_view(), name='dogfood_update'),
    path('dogfood/<int:pk>/delete/', views.DogFoodDelete.as_view(), name='dogfood_delete'),
    path('dogs/<int:dog_id>/assoc_dogfood/<int:dogfood_id>/', views.assoc_dogfood, name='assoc_dogfood'),
    path('dogs/<int:dog_id>/unassoc_dogfood/<int:dogfood_id>/', views.unassoc_dogfood, name='unassoc_dogfood'),
    path('foodtrans/create/', views.FoodTransCreate.as_view(), name='foodtrans_create'),
    path('foodtrans/<int:pk>', views.foodtrans_detail, name='foodtrans_detail'),
    path('foodtrans/', views.FoodTransList.as_view(), name='foodtrans_index'),
    path('foodtrans/<int:pk>/update/', views.FoodTransUpdate.as_view(), name='foodtrans_update'),
    path('foodtrans/<int:pk>/delete/', views.FoodTransDelete.as_view(), name='foodtrans_delete'),
    path('myvet/create/', views.MyVetCreate.as_view(), name='myvet_create'),
    path('myvet/', views.MyVetList.as_view(), name='myvet_index'),
    path('myvet/<int:pk>', views.myvet_detail, name='myvet_detail'),


]