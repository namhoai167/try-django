from django.http import HttpResponse

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse('<h1>Welcome to homepage</h1>')
