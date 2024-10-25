from django.shortcuts import render


def profile_details(request):
    return render(request, 'profiles/profile-details.html')


def profile_delete(request):
    return render(request, 'profiles/profile-delete.html')



