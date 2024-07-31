from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_status')
    else:
        form = ServiceRequestForm()
    return render(request, 'request/submit_request.html', {'form': form})

@login_required
def request_status(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'request/request_status.html', {'requests': requests})
