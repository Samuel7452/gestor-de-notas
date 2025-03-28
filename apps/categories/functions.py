from django.shortcuts import render, redirect
from .forms import CategoryForm
from django.contrib import messages

def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Categoría creada con éxito.")
            return redirect('/api/v1/notes/list/')
        else:
            messages.error(request, "❌ Hubo un error al crear la categoría.")
    
    else:
        form = CategoryForm()

    return render(request, "categories/category_form.html", {"form": form})

