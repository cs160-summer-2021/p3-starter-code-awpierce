from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction/', views.new_interaction, name='new_interaction'),
    path('account/', views.account, name='account'),
    path('setting/', views.setting, name='setting'),
    path('reference/', views.reference, name='reference'),
    path('asreference/', views.reference, name='asreference'),
    path('sketch/', views.sketch, name='sketch'),
    path('mandela/', views.mandela, name='mandela'),
    path('sketch_as_reference/', views.sketch_as_reference, name='sketch_as_reference'),
    path('sketch_with_reference/', views.sketch_with_reference, name='sketch_with_reference')
]
