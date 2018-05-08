from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect, HttpResponse
from system_wynajmu.models import Estate, Contract
from system_wynajmu.forms import ContractForm, EstateForm
from django.urls import reverse
import datetime

@login_required
def user_page(request):
    estates = Estate.objects.filter(user_id=request.user)
    con = Contract.objects.all()
    contracts = []
    cons = {}
    for e in estates:
        c = Contract.objects.filter(estate_id = e)
        try:
            cons[e] = c[0]
        except Exception:
            cons[e] = None
    return render(request, 'strona_uzytkownika.html', {'estates': estates, 'user': request.user, 'cons': cons})
 
@login_required 
def delete_contract(request):
    contract = get_object_or_404(Contract, id=request.session['cont'])
    estate = contract.estate_id
    if contract.estate_id.user_id != request.user:
        return HttpResponse("aby zobaczyć stronę nieruchomości musisz być jej właścicielem")
    contract.delete()
    return HttpResponseRedirect(reverse('system:estate_page', kwargs={'estate_id': estate.id}))
   
   

    
@login_required
def estate_page(request, estate_id): 
    estate = get_object_or_404(Estate, pk=estate_id)
    if estate.user_id != request.user:
        return HttpResponse("aby zobaczyć stronę nieruchomości musisz być jej właścicielem")
    found_contract = False
    for contract in Contract.objects.all().filter(estate_id=estate):
        found_contract = True
        con = contract
    if not found_contract:
        con = Contract(estate_id=estate, date_start=datetime.date.today)
    if request.method == 'POST':
        form = ContractForm(request.POST, instance=con)
        if form.is_valid():
            con = form.save()
            found_contract = True
        else:
            return render(request, 'strona_nieruchomosci.html', 
            {'estate': estate, 'form': form, 'found': found_contract, 'invalid': True, 'con': con})
    if found_contract:
        request.session['cont'] = con.id
        form = ContractForm(instance=con)
        return render(request, 'strona_nieruchomosci.html', {'estate': estate, 
            'form': form, 'found': found_contract, 'contract': con})
    else:
        form = ContractForm(instance=con)
        return render(request, 'strona_nieruchomosci.html', {'estate': estate, 'form': form, 'found': found_contract, 'con': con})

@login_required
def estate_edit_page(request):
    edit = False
    if 'edit' in request.session and request.session['edit']:
        est = get_object_or_404(Estate, id=request.session['est'])
        if est.user_id != request.user:
            return HttpResponse("aby zobaczyć stronę nieruchomości musisz być jej właścicielem")
        edit = True
    else:
        est = Estate(user_id=request.user)
    if request.method == 'POST':
        form = EstateForm(request.POST, instance=est)
        if form.is_valid():
            est = est.save()
            return HttpResponseRedirect(reverse('system:user_page'))
        else:
            return render(request, 'strona_edycji_nieruchomosci.html', {'edit': edit, 'form': form, 'estate': est})
    form = EstateForm(instance=est)
    return render(request, 'strona_edycji_nieruchomosci.html', {'edit': edit, 'form': form, 'estate': est})

    
@login_required 
def estate_edit(request, estate_id):
    request.session['edit'] = True
    request.session['est'] = estate_id
    return HttpResponseRedirect(reverse('system:estate_edit_page'))

@login_required 
def estate_add(request):
    request.session['edit'] = False
    return HttpResponseRedirect(reverse('system:estate_edit_page'))
     
    
@login_required 
def delete_estate(request, estate_id):
    estate = get_object_or_404(Estate, id=estate_id)
    if estate.user_id != request.user:
        return HttpResponse("aby usunąć nieruchomość musisz być jej właścicielem")
    estate.delete()
    return HttpResponseRedirect(reverse('system:user_page'))
   
