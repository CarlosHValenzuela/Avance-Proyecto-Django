from django.shortcuts import render
from django.http import StreamingHttpResponse
from core.utils.videoReconocer import   generate_frames
from core.utils.videoCapturar import capture_plate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Vista para la página principal
def home(request):
    return render(request, 'home.html')

def reconocedor(request):
    return render(request, 'reconocedor.html')

def captura(request):
    return render(request, 'captura.html')

# Vista para el feed de video
def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_capture(request):
    return StreamingHttpResponse(capture_plate(), content_type='multipart/x-mixed-replace; boundary=frame')