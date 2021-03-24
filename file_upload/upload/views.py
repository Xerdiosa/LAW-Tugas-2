from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponse
import os, mimetypes

def filestorage(request):
    if request.method == 'POST':
        if 'file' not in request.FILES:
            return HttpResponse("FILE NOT PROVIDED", status=400)
        original_file = request.FILES['file']
        if os.path.exists("file_repo/" + original_file.name):
            return HttpResponse('FILE ALREADY EXIST', status=406)
        with open("file_repo/" + original_file.name, 'wb+') as destination:
            for chunk in original_file.chunks():
                destination.write(chunk)
        return HttpResponse('FILE UPLOADED', status=201)
    if request.method == 'GET':
        filename = request.GET.get('file')
        if filename is None:
            return HttpResponse("FILENAME NOT PROVIDED", status=400)
        if not os.path.exists("file_repo/" + filename):
            return HttpResponse('FILE NOT FOUND', status=404)
        file_type = mimetypes.guess_type(filename)[0]
        file = open("file_repo/" + filename, 'rb')
        response = HttpResponse(file.read(), content_type=file_type)
        response['Content-Disposition'] = f'attachment; filename={filename}'
        file.close()
        return response
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])