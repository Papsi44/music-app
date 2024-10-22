from django.shortcuts import render


def profile_details(request):
    return render(request, template_name='profiles/profile-details.html', context={})


def profile_delete(request):
    return render(request, template_name='profiles/profile-delete.html', context={})


def home_no_profile(request):
    return render(request, template_name='profiles/home-no-profile.html', context={})


def home_with_profile(request):
    return render(request, template_name='profiles/home-with-profile.html', context={})
