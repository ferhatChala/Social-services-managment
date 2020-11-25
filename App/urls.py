from django.urls import path
from App import views

urlpatterns = [
   
    path('info/',views.AboutView.as_view(),name='info'),
    path('prime/<int:pk>/',views.PrimeDetailView.as_view(),name='prime_detail'),
    path('prime/new/',views.PrimeCreateView.as_view(),name='prime_new'),
   # path('prime/<int:pk>/edit/',views.PrimeUpdateView.as_view(),name='prime_edit'),
   # path('prime/<int:pk>/remove/',views.PrimeDeleteView.as_view(),name='post_remove'),
    path('primes/',views.PrimeListView.as_view(),name='prime_list'),
    
]