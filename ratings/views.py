from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.forms.models import model_to_dict

from ratings.models import Rating
from ratings.forms import RatingForm, RatingEditForm, RatingDeleteForm


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
        rating = get_object_or_404(Rating, id=rating_id)

        form = self.form_class(model_to_dict(rating))
        return render(request, self.template_name, {'form': form, 'id': rating_id})

    def post(self, request, rating_id):
        if not request.method == 'POST':
            return redirect(home)
        
        print "hello, world"
        rating = get_object_or_404(Rating, id=rating_id)
        form = RatingEditForm(request.POST, instance=rating)
        if form.is_valid():
            form.save()
            return redirect(home)
        return render(request, self.template_name, {'form': form})

        
class RatingDelete(View):    
    def post(self, request, rating_id): 
        rating = get_object_or_404(Rating, id=rating_id)
        form = RatingDeleteForm(request.POST, instance=rating)
        if form.is_valid():
            rating.delete()
        return redirect(home)






