from django.urls import path
from Volunt import views
urlpatterns = [
    path('about/',views.about,name='abot'),
    path('Index/', views.index, name='Ind'),
    path('vol_add/', views.vol_add, name='add'),
    path('vol_list/', views.vol_list, name='list'),
    path('vol_list/', views.vol_list, name='list'),
    path('vol_list/<int:id>',views.stddetails, name='stddetails'),
    path('edit/<int:id>', views.edit, name='edit'),

]
