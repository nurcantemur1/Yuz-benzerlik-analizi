from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from face_detect import Deneme


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        fs.save(myfile.name, myfile)
        result = Deneme(myfile.name)
        return render(request, 'core/simple_upload.html', {
            'result': result
        })
    form = DocumentForm()
    return render(request, 'core/simple_upload.html', {'form': form})
