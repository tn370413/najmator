from django.shortcuts import render

def user_page(request):
    return render(request, 'strona_uzytkownika.html')
