from django.shortcuts import render, redirect

from music_project.albums.forms import AlbumAddForm
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


def album_details(request):
    form = AlbumAddForm(request.POST or None)


    return render(request,'albums/album-details.html')


def album_edit(request):
    return render(request, template_name='albums/album-edit.html', context={})


def album_delete(request):
    return render(request, template_name='albums/album-delete.html', context={})
