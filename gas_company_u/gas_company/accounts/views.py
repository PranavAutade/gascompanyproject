from django.shortcuts import render, redirect
from .forms import UserProfileForm

def account_info(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('account_info')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'account/account_info.html', {'form': form})
