

from django.shortcuts import render


class omeView(ListView):

    def get(self, req):
        return render(req, 'home.html')
