from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Metadata
from django.db.utils import IntegrityError
from .oauth_handler import oauth_handler

from datetime import datetime

class MetadataView(View):
    def get(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            if not oauth_handler(token):
                return HttpResponse("UNAUTHORIZED", status=401)
        except:
            return HttpResponse("UNAUTHORIZED", status=401)
        title = request.GET.get('title')
        if title is None:
            return HttpResponse("TITLE NOT PROVIDED", status=400)
        try:
            metadata = Metadata.objects.get(title=title)
        except Metadata.DoesNotExist:
            return HttpResponse("METADATA DOES NOT EXIST", status=404)
        metadata_dict = {"title":metadata.title, 
                        "author":metadata.author, 
                        "description":metadata.description}
        return JsonResponse(metadata_dict)
    def post(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            if not oauth_handler(token):
                return HttpResponse("UNAUTHORIZED", status=401)
        except:
            return HttpResponse("UNAUTHORIZED", status=401)
        title = request.POST.get('title', None)
        if title is None:
            return HttpResponse('TITLE IS EMPTY', status=400)
        author = request.POST.get('author', None)
        description = request.POST.get('description', None)
        metadata = Metadata(title=title, author=author, description=description)
        try:
            metadata.save()
        except IntegrityError:
            return HttpResponse('METADATA RECORD ALREADY EXIST', status=400)
        return HttpResponse('CREATED', status=201)
    def put(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            if not oauth_handler(token):
                return HttpResponse("UNAUTHORIZED", status=401)
        except:
            return HttpResponse("UNAUTHORIZED", status=401)
        request.method = "POST"
        title = request.POST.get('title')
        if title is None:
            return HttpResponse("TITLE NOT PROVIDED", status=400)
        try:
            metadata = Metadata.objects.get(title=title)
        except Metadata.DoesNotExist:
            return HttpResponse("METADATA DOES NOT EXIST", status=404)
        metadata.author = request.POST.get('author', None)
        metadata.description = request.POST.get('description', None)
        metadata.updated_at = datetime.now()
        metadata.save()
        return HttpResponse('UPDATED')
    def delete(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            if not oauth_handler(token):
                return HttpResponse("UNAUTHORIZED", status=401)
        except:
            return HttpResponse("UNAUTHORIZED", status=401)
        request.method = "POST"
        title = request.POST.get('title')
        if title is None:
            return HttpResponse("TITLE NOT PROVIDED", status=400)
        try:
            metadata = Metadata.objects.get(title=title)
        except Metadata.DoesNotExist:
            return HttpResponse("METADATA DOES NOT EXIST", status=404)
        metadata.delete()
        return HttpResponse("DELETED")

