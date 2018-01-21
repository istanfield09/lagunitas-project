from django.shortcuts import render, redirect
from django.views.generic.base import View

from ratings.models import Rating
from ratings.forms import RatingForm, RatingEditForm


def home(request):
    """ Show the entry point to the ratings app
    :param request: Django request object
    :return: rendered homepage
    """
    context = {'ratings': Rating.objects.all()}
    return render(request, 'home.html', context)


class RatingCreate(View):
    """ Create a new Rating """
    form_class = RatingForm
    template_name = 'ratings/rating_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            _ = form.save()
            return redirect(home)
        return render(request, self.template_name, {'form': form})

class RatingEdit(View):
    """ Edit an existing Rating """
    form_class = RatingEditForm
    template_name = 'ratings/edit_rating_form.html'

    def get(self, request, rating_id):
        try:
            rating = Rating.objects.get(pk=rating_id)
        except:
            return redirect(home)

        data = {'score': rating.score, 'notes': rating.notes,
                'beer_name': rating.beer_name}
        form = self.form_class(data)
        return render(request, self.template_name, {'form': form})

    def post(self, request, rating_id):
        try:
            rating = Rating.objects.get(pk=rating_id)
        except:
            return redirect(home)
        
        fields = ['score', 'notes', 'beer_name']
        for field in fields:
            if request.POST.get(field, None):
                setattr(rating, field, request.POST.get(field))

        if not rating.save():
            return redirect(home)
        return render(request, self.template_name, {'form': form})

