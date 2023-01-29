from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Creature
from .forms import CreatureForm

def creature_list(request):
    creatures = Creature.objects.all()
    return render(request, 'creatures/creature_list.html', {'creatures': creatures})

@login_required
def creature_create(request):
    if request.method == 'POST':
        form = CreatureForm(request.POST)
        if form.is_valid():
            creature = form.save(commit=False)
            creature.owner = request.user
            creature.save()
            return redirect('creature_list')
    else:
        form = CreatureForm()
    return render(request, 'creatures/creature_form.html', {'form': form})

@login_required
def creature_update(request, pk):
    creature = get_object_or_404(Creature, pk=pk)
    if request.user != creature.owner:
        return redirect('creature_list')

    if request.method == 'POST':
        form = CreatureForm(request.POST, instance=creature)
        if form.is_valid():
            creature = form.save(commit=False)
            creature.owner = request.user
            creature.save()
            return redirect('creature_list')
    else:
        form = CreatureForm(instance=creature)
    return render(request, 'creatures/creature_form.html', {'form': form})

@login_required
def creature_delete(request, pk):
    creature = get_object_or_404(Creature, pk=pk)
    if request.user != creature.owner:
        return redirect('creature_list')

    creature.delete()
    return redirect('creature_list')