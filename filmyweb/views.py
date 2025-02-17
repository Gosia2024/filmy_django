from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm



# Create your views here.
def wszystkie_filmy(request):
    #return HttpResponse("<h1>To jest nasz pierwszy test</h1>")
    wszystkie = Film.objects.all()

    return render(request, 'filmy.html', {'filmy':wszystkie})


def nowy_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
     form.save()
    return redirect(wszystkie_filmy)
        
    return render(request, 'film_form.html', {'form': form})

def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id)

    form = FilmForm(request.POST or None, request.FILES or None,
    instance=film)

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy)
        
    return render(request, 'film_form.html', {'form': form})