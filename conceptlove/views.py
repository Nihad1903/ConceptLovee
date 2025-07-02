from django.shortcuts import render, redirect, get_object_or_404
from .forms import CodeForm
from .models import PersonalPage

def home(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
            print(code)
            try:
                page = PersonalPage.objects.get(code=code)
                return redirect('view_page', page_id=page.id)
            except PersonalPage.DoesNotExist:
                form.add_error("code", "No page found with this code.")
    else:
        form = CodeForm()
    return render(request, "home.html", {"form": form})

def view_page(request, page_id):
    page = get_object_or_404(PersonalPage, id=page_id)
    return render(request, "view_page.html", {"page": page})