from django.http import HttpResponse, HttpResponseNotAllowed
import zipfile

def compress(request):
    if request.method == 'POST':
        original_file = request.FILES['file']
        response = HttpResponse(content_type='application/zip')
        zf = zipfile.ZipFile(response, 'w')
        zf.writestr(original_file.name, original_file.read())
        zf.close()
        response['Content-Disposition'] = f'attachment; filename={original_file.name}.zip'
        return response
    return HttpResponseNotAllowed(["POST"])

