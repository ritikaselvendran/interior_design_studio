from django.shortcuts import render, get_object_or_404, redirect
from .models import Design, Favorite
from .forms import DesignForm
from django.contrib.auth import authenticate, login


def design_list(request):
    designs = Design.objects.all()
    return render(request, 'design_list.html', {'designs': designs})


def design_detail(request, pk):
    design = get_object_or_404(Design, pk=pk)
    return render(request, 'design_detail.html', {'design': design})


def design_create(request):
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES)
        if form.is_valid():
            design = form.save()
            return redirect('design_detail', pk=design.pk)
    else:
        form = DesignForm()
    return render(request, 'design_form.html', {'form': form, 'action': 'Create'})


def design_edit(request, pk):
    design = get_object_or_404(Design, pk=pk)
    if request.method == 'POST':
        form = DesignForm(request.POST, request.FILES, instance=design)
        if form.is_valid():
            design = form.save()
            return redirect('design_detail', pk=design.pk)
    else:
        form = DesignForm(instance=design)
    return render(request, 'design_form.html', {'form': form, 'action': 'Edit'})


def design_confirm_delete(request, pk):
    design = get_object_or_404(Design, pk=pk)
    if request.method == 'POST':
        design.delete()
        return redirect('design_list')
    return render(request, 'design_confirm_delete.html', {'design': design})


def add_favorite(request, design_id):
    design = get_object_or_404(Design, pk=design_id)
    favorite, created = Favorite.objects.get_or_create(design=design)
    return redirect('design_detail', pk=design_id)


def login_view(request):
    return render(request, 'login.html')


def home_view(request):
    # Logic for rendering home.html
    return render(request, 'home.html')


def balcony(request):
    return render(request, 'balcony.html')


def bathroom(request):
    return render(request, 'bathroom.html')


def bedroom(request):
    return render(request, 'bedroom.html')


def dining(request):
    return render(request, 'dining.html')


def dressing(request):
    return render(request, 'dressing.html')


def kitchen(request):
    return render(request, 'kitchen.html')


def living(request):
    return render(request, 'living.html')


def office(request):
    return render(request, 'office.html')


def pooja(request):
    return render(request, 'pooja.html')


