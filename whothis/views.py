from django.http import HttpResponse
from django.shortcuts import render

from PIL import Image
from io import BytesIO
from time import time_ns
import face_recognition as fr

# home page
def index (request):
    context = {'key': 'val'}
    return render(request,'whothis/index.html',context)

# acquire the person whose id it is
def acquire_human (request, uid):
    return HttpResponse("dev.")

def post (request):
    filename = f'{time_ns()}.png'

    stream = BytesIO (request.body)
    image = Image.open(stream).convert("RGB")
    stream.close()

    print(type(request.body))

    image.save(filename)


    arnav = fr.face_encodings(fr.load_image_file("key.jpg"), num_jitters=30)
    print(filename)
    encodings = fr.face_encodings(fr.load_image_file(filename))

    net_result = True

    for encoding in encodings:
        results = fr.compare_faces(arnav,encoding, tolerance=0.5)
        print(results)
        net_result = results[0] and net_result

    return HttpResponse(net_result)
