from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Firmware

def upload_firmware(request):
    if request.method == 'POST':
        version = request.POST['version']
        file = request.FILES['file']
        description = request.POST['description']
        firmware = Firmware(version=version, file=file, description=description)
        firmware.save()
        return redirect('firmware_list')
    return render(request, 'ota/upload_firmware.html')

def check_for_updates(request):
    version = request.GET.get('version')
    latest_firmware = Firmware.objects.latest('id')
    if version == latest_firmware.version:
        return JsonResponse({'message': 'You are already on the latest version.'})
    else:
        firmware_url = request.build_absolute_uri(latest_firmware.file.url)
        return JsonResponse({'version': latest_firmware.version, 'description': latest_firmware.description, 'url': firmware_url})

def firmware_list(request):
    firmwares = Firmware.objects.all()
    return render(request, 'ota/firmware_list.html', {'firmwares': firmwares})