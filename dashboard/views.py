from django.http import HttpResponse


def home(request):
    return HttpResponse("Recipe Dashboard is running.")

