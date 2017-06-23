from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from .forms import PlaceCreateForm


class PlaceCreateView(View):

    @login_required()
    def get(self, request):
        form = PlaceCreateForm()
        context = {'form': form}
        return render(request, 'places:place_create.html', context)