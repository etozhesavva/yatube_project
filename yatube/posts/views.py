from django.http import HttpResponse

def index(request):    
    return HttpResponse('Добро пожаловать в Yatube!')

def group_posts(request, slug):
    return HttpResponse(f'Новости {slug}')