from django.shortcuts import render


def album_add(request):
    return render(request, template_name='albums/album-add.html', context={})


def album_details(request):
    return render(request, template_name='albums/album-details.html', context={})


def album_edit(request):
    return render(request, template_name='albums/album-edit.html', context={})


def album_delete(request):
    return render(request, template_name='albums/album-delete.html', context={})
