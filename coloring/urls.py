from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction/', views.new_interaction, name='new_interaction'),
    path('account/', views.account, name='account'),
    path('setting/', views.setting, name='setting'),
    path('reference/', views.reference, name='reference')
]
