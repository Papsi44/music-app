from django.shortcuts import render, redirect

from music_project.albums.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm
from music_project.albums.models import Album
from music_project.utils import get_user_obj


def album_add(request):
    user = get_user_obj()
    form = AlbumAddForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
        form.instance.owner = user
        form.save()
        # form.instance.owner = user
        # form.save()
        return redirect('home')
    context = {'form': form,
               }

    return render(request, 'albums/album-add.html', context)


def album_details(request, id):
    album_det = Album.objects.get(pk=id)

    context = {
        'album': album_det,
    }
    return render(request,'albums/album-details.html', context)


def album_edit(request, id):
    album_to_edit = Album.objects.get(pk=id)
    form = AlbumEditForm(request.POST or None, instance=album_to_edit)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form,
    }

    return render(request,'albums/album-edit.html',context)


def album_delete(request, id):
    album_to_delete = Album.objects.get(pk=id)
    form = AlbumDeleteForm(request.POST or None, instance=album_to_delete)
    if request.method == 'POST':
        album_to_delete.delete()
        return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'albums/album-delete.html', context)
