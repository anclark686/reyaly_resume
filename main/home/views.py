from django.shortcuts import render
from django.http import HttpResponse, Http404
from wsgiref.util import FileWrapper
import os


def home(request):
    return render(request, "home/home.html")


# def download(request):
#     filename = "A_Clark_Resume-2022F.pdf"
#     content = FileWrapper(filename)
#     response = HttpResponse(content, content_type='application/pdf')
#     response['Content-Length'] = os.path.getsize(filename)
#     response['Content-Disposition'] = 'attachment; filename=%s' % 'faults.pdf'
#     return response

def open_file(request, *args, **kwargs):
    path = str(kwargs['p'])

    file_path = '/Users/anclark686/Desktop/Programming/Python/reyaly_resume/main/home/static/download/A_Clark_Resume-2022F.pdf'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404