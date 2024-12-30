from django.urls import path
from . import views

urlpatterns = [
    path('balcony.html', views.balcony, name='balcony'),
    path('bathroom.html', views.bathroom, name='bathroom'),
    path('bedroom.html', views.bedroom, name='bedroom'),
    path('dining.html', views.dining, name='dining'),
    path('dressing.html', views.dressing, name='dressing'),
    path('kitchen.html', views.kitchen, name='kitchen'),
    path('living.html', views.living, name='living'),
    path('office.html', views.office, name='office'),
    path('pooja.html', views.pooja, name='pooja'),
    path('design/list', views.design_list, name='design_list'),
    path('design/<int:pk>/', views.design_detail, name='design_detail'),
    path('design/<int:pk>/edit/', views.design_edit, name='design_edit'),
    path('design/<int:pk>/delete/', views.design_confirm_delete, name='design_confirm_delete'),
    path('design/<int:design_id>/add_favorite/', views.add_favorite, name='add_favorite'),
    path('design/<int:pk>/edit/', views.design_edit, name='design_edit'),
    path('design/create/', views.design_create, name='design_create'),
    path('', views.login_view, name='login'),
    path('home.html'
         '', views.home_view, name='home'),
]