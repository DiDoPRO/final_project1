from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tables/', views.TableListView.as_view(), name='tables'),
    path('table/<int:pk>', views.TableDetailView.as_view(), name='table-detail'),
    path('foods/', views.FoodListView.as_view(), name='foods'),
    path('food/<int:pk>', views.FoodDetailView.as_view(), name='food-detail'),
    path('drinks/', views.DrinkListView.as_view(), name='drinks'),
    path('drink/<int:pk>', views.DrinkDetailView.as_view(), name='drink-detail'),
]
urlpatterns += [   
    path('book/<uuid:pk>/renew/', views.renew_table_restoran, name='renew-table-restoran'),
]