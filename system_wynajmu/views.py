from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

@login_required
def user_page(request):
    return render(request, 'strona_uzytkownika.html')

@login_required
def estate_page(request):
    return render(request, 'strona_nieruchomosci.html')

@login_required
def estate_edit_page(request):
    return render(request, 'strona_edycji_nieruchomosci.html')

