
from django.urls import path
from webs import views

urlpatterns = [
    path('',views.test),
    path('data/', views.data_view, name='data'),
]
