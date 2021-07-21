from typing import List
from job.models import Listing
from itertools import chain


def listing_tracker(user):
    all_listings = Listing.objects.all()
    applied = []
    accepted = []
    interviewing = []
    offer_extended = []
    hired = []
    reject = []
    for listing in all_listings:
          print(user in listing.applicants.all())
          if user in listing.applicants.all():
              applied += chain(Listing.objects.filter(id=listing.id)) 
          if user in listing.accepted_apps.all():
              accepted += chain(Listing.objects.filter(id=listing.id))
          if user in listing.interviewing_apps.all():
              interviewing += chain(Listing.objects.filter(id=listing.id))
          if user in listing.offer_extended_apps.all():
              offer_extended += chain(Listing.objects.filter(id=listing.id))
          if user in listing.hired_apps.all():
              hired += chain(Listing.objects.filter(id=listing.id))
          if user in listing.denied_apps.all():
              reject += chain(Listing.objects.filter(id=listing.id))
    return applied, accepted, interviewing, offer_extended, hired, reject
