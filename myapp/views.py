from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImageForm
from .models import Image
# Create your views here.

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()

    img = Image.objects.all()

    context = {'form':form, 'img':img}
    return render(request, 'myapp/home.html', context)


def delete_image(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    
    # if request.method == 'POST':
    image.delete()
        # return redirect('home')
    
    return redirect('home')
    # return render(request, 'myapp/delete_image.html', {'image': image})
