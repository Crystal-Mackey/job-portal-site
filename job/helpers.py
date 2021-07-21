from .models import Listing

def searchAlgo(q):
    q_set = []
    keywords = q.lower()
    for listing in Listing.objects.all():
        title = listing.title.lower()
        if title.find(keywords) != -1:
            print(listing, "match")
            q_set.append(listing)
    print(q_set)
    return q_set
        

