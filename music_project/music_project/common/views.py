from django.shortcuts import render, redirect

from music_project.profiles.forms import ProfileCreateForm
from music_project.utils import get_user_obj


def home(request):
    user = get_user_obj()
    form = ProfileCreateForm(request.POST or None, instance=user)
    if user:
        albums = list(user.albums.all())
    else:
        albums = None

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form,
               'user': user,
               'albums': albums}
    if not user:
        return render(request, 'common/home-no-profile.html', context)

    return render(request, 'common/home-with-profile.html', context)


# def home(request):
#     user = get_user_obj()
#
#     if not user:
#         if request.method == 'POST':
#             form = ProfileCreateForm(request.POST or None, instance=user)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#             context = {'form': form}
#             return render(request, 'common/home-with-profile.html', context)
#
#         if request.method == 'GET':
#             return render(request, 'common/home-no-profile.html')
#
#     return render(request, 'common/home-with-profile.html')

