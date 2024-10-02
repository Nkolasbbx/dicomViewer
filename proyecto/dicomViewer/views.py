from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DicomFile
import pydicom
from PIL import Image
import numpy as np
import io
import base64


# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import DicomFile

# Se le envía una solicitud y retorna una respuesta.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def archivos(request):
    archivos_dicom = DicomFile.objects.all()  # Obtiene todos los archivos DICOM
    return render(request, 'archivos/index.html', {'archivos': archivos_dicom})

def subirArchivo(request):  
    return render(request, 'archivos/subirArchivo.html')


def verArchivo(request, pk):
    archivo = get_object_or_404(DicomFile, pk=pk)

    # Leer el archivo DICOM
    ds = pydicom.dcmread(archivo.dicom_file.path)
    pixel_array = ds.pixel_array
    image = Image.fromarray(pixel_array).convert("L")  # Convertir a escala de grises

    # Guardar la imagen en un buffer para mostrar en HTML
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return render(request, 'archivos/verArchivo.html', {'archivo': archivo, 'img_data': img_str})