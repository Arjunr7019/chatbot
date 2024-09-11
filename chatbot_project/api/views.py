
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

# Login View
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

# Logout View
@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'}, status=200)


