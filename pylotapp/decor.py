from functools import wraps
from django.db import transaction

from .models import Page, ContentVideo, ContentAudio, ContentText

def countedPage(f):
    @wraps(f)
    def decorator(request,*args,**kwargs):
        mdl = [Page.objects.all(),ContentVideo.objects.all(),ContentAudio.objects.all(),ContentText.objects.all()]

        for objarray in mdl:
            for i in range(objarray.count()) :
                counter = objarray[i]
                counter.counter = counter.counter+1
                counter.save()
        return f(request, *args, **kwargs)
    return decorator

