from django.shortcuts import render, redirect, get_object_or_404
## Usado para Login
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

# Create your views here.
@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'v_person': persons})


@login_required
def person_new(request):
    ## caso cliente ja tenha preenchido ele crias com dados
    form = PersonForm(request.POST or None, request.FILES or None)
    # Depois precisamos validar form
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'v_form': form})

@login_required
def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(
        request.POST or None, request.FILES or None, instance=person
    )
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'v_form': form})

@login_required
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(
        request.POST or None, request.FILES or None, instance=person
    )
    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')

    return render(request, 'person_delete_confirm.html', {'person': person})

