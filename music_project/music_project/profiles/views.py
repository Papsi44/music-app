from django.shortcuts import render, redirect

from music_project.utils import get_user_obj


def profile_details(request):
    user = get_user_obj()
    context = {'user': user}
    return render(request, 'profiles/profile-details.html', context)


def profile_delete(request):
    user = get_user_obj()
    if request.method == 'POST':
        user.delete()
        return redirect('home')

    context = {'user': user}

    return render(request, 'profiles/profile-delete.html', context)



