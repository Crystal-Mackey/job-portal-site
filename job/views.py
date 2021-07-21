from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .helpers import searchAlgo
from .models import Listing
from .forms import CreateListingForm
from user.models import User


class listing_detail_view(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        template = 'listing_detail.html'
        user = request.user
        listing_id = kwargs['listing_id']
        listing = Listing.objects.get(id=listing_id)
        print(user is listing.user,)
        
        if not user.username==listing.user.username:
            print(user.username, listing.user.username)
        if not user in listing.applicants.all():
            print("line 19 should work")
            print(user, listing.applicants)
        context = {
            'listing': listing,
            'user': user
        }
        print('WORKING?', request, template, context)
        return render(request, template, context)

    def post(self, request, *args, **kwargs):
        template = 'listing_detail.html'
        user = request.user
        listing_id = kwargs['listing_id']
        listing = Listing.objects.get(id=listing_id)
        listing.applicants.add(user)
        listing.save()
        print(listing.applicants)
        return HttpResponseRedirect("/listing/%s" % listing.id)


class create_listing_view(View):
    def get(self, request):
        user = self.request.user
        template_name = 'create_listing.html'
        form = CreateListingForm()
        context = {'form': form}
        return render(request, template_name, context)

    def post(self, request, *args, **kwargs):
        form = CreateListingForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                listing = form.save(commit=False)
                listing.user = request.user
                listing.save()
                template = 'listing_detail.html'
                messages.add_message(
                    request, messages.INFO, "<p id='listing-message'>Want to create another Job Listing? Click <a href='/create/'>here</a></p>", extra_tags='safe')
                return HttpResponseRedirect("/listing/%s" % listing.id)


def search_view(request):
    template = 'search.html'
    keywords = request.GET.get('query', '')
    print(keywords)
    results = searchAlgo(keywords)
    context = {
        'results': results,
        'keywords': keywords,
    }
    return render(request, 'search.html', context)


def toggle_favorite(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    if request.user in listing.favorited_by.all():
        listing.favorited_by.remove(request.user)
    else:
        listing.favorited_by.add(request.user)
    return HttpResponseRedirect(f"/listing/{listing_id}/")


def reject_applicant_view(request, listing_id: int, user_id: int):
    listing = Listing.objects.get(id=listing_id)
    rejected_user = User.objects.get(id=user_id)
    listing.applicants.remove(rejected_user)
    listing.accepted_apps.remove(rejected_user)
    listing.interviewing_apps.remove(rejected_user)
    listing.offer_extended_apps.remove(rejected_user)
    listing.hired_apps.remove(rejected_user)
    listing.denied_apps.add(rejected_user)
    listing.save()
    return HttpResponseRedirect(f"/listing/{listing_id}/")

def accept_view(request, listing_id:int, user_id:int):
    listing = Listing.objects.get(id=listing_id)
    accepted_user = User.objects.get(id=user_id)
    listing.applicants.remove(accepted_user)
    listing.accepted_apps.add(accepted_user)
    listing.save()
    return HttpResponseRedirect(f"/listing/{listing_id}/")

def accepted_app_view(request, listing_id:int, user_id:int):
    listing = Listing.objects.get(id=listing_id)
    accepted_user = User.objects.get(id=user_id)
    listing.accepted_apps.remove(accepted_user)
    listing.interviewing_apps.add(accepted_user)
    listing.save()
    return HttpResponseRedirect(f"/listing/{listing_id}/")

def interviewing_view(request, listing_id:int, user_id:int):
    listing = Listing.objects.get(id=listing_id)
    accepted_user = User.objects.get(id=user_id)
    listing.interviewing_apps.remove(accepted_user)
    listing.offer_extended_apps.add(accepted_user)
    listing.save()
    return HttpResponseRedirect(f"/listing/{listing_id}/")

def offer_extended_view(request, listing_id:int, user_id:int):
    listing = Listing.objects.get(id=listing_id)
    accepted_user = User.objects.get(id=user_id)
    listing.offer_extended_apps.remove(accepted_user)
    listing.hired_apps.add(accepted_user)
    listing.save()
    return HttpResponseRedirect(f"/listing/{listing_id}/")

def hired_view(request, listing_id:int, user_id:int):
    listing = Listing.objects.get(id=listing_id)
    accepted_user = User.objects.get(id=user_id)
    listing.offer_extended_apps.remove(accepted_user)
    listing.hired_apps.add(accepted_user)
    listing.save()
    return HttpResponseRedirect(f"/listing/{listing_id}/")