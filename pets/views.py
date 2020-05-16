from django.views.generic.list import ListView
from django.shortcuts import render


class HomeView(ListView):

    def get(self, req):
        return render(req, './templates/home.html')
