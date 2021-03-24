from django.http import HttpResponse, HttpResponseNotAllowed
from .oauth_handler import oauth_handler
import zipfile

def compress(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split()[1]
        if not oauth_handler(token):
            return HttpResponse("UNAUTHORIZED", status=401)
    except:
        return HttpResponse("UNAUTHORIZED", status=401)
    if request.method == 'POST':
        original_file = request.FILES['file']
        response = HttpResponse(content_type='application/zip')
        zf = zipfile.ZipFile(response, 'w')
        zf.writestr(original_file.name, original_file.read())
        zf.close()
        response['Content-Disposition'] = f'attachment; filename={original_file.name}.zip'
        return response
    return HttpResponseNotAllowed(["POST"])

