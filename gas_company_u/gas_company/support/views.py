from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RequestForm, AssignRepForm
from .models import SupportRequest

def submit_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            support_request = form.save(commit=False)
            support_request.requester = request.user
            support_request.save()
            messages.success(request, 'Your request has been submitted successfully.')
            return redirect('request_status')
    else:
        form = RequestForm()
    return render(request, 'support/submit_request.html', {'form': form})

def request_status(request):
    user_requests = SupportRequest.objects.filter(requester=request.user)
    return render(request, 'support/request_status.html', {'requests': user_requests})

def request_detail(request, pk):
    support_request = get_object_or_404(SupportRequest, pk=pk)
    return render(request, 'support/request_detail.html', {'request': support_request})

def update_request_status(request, pk):
    support_request = get_object_or_404(SupportRequest, pk=pk)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(SupportRequest.STATUS_CHOICES).keys():
            support_request.status = status
            support_request.save()
            messages.success(request, 'Request status updated successfully.')
        else:
            messages.error(request, 'Invalid status value.')
        return redirect('request_status')
    return render(request, 'support/update_status.html', {'request': support_request})

def assign_rep(request, pk):
    support_request = get_object_or_404(SupportRequest, pk=pk)
    if request.method == 'POST':
        form = AssignRepForm(request.POST, instance=support_request)
        if form.is_valid():
            form.save()
            messages.success(request, 'Representative assigned successfully.')
            return redirect('request_status')
    else:
        form = AssignRepForm(instance=support_request)
    return render(request, 'support/assign_rep.html', {'form': form, 'request': support_request})
