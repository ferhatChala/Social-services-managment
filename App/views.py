from django.shortcuts import render
from django.urls import reverse_lazy,reverse

from App.models import Article,Prime
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.

class AboutView(TemplateView):
    template_name= 'info.html'



class PrimeCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'App/prime_list.html'
    fields = ('article','justif')
    model = Prime

    def form_valid(self,form):
        form.save(commit=False)
        form.instance.employer = self.request.user
        
        
        return super(PrimeCreateView,self).form_valid(form)
    
   


class PrimeListView(LoginRequiredMixin,ListView):
    #context_object_name='primes'
    login_url = '/login/'
    redirect_field_name = 'App/prime_list.html'
    model = Prime

class PrimeDetailView(DetailView):
    model = Prime

