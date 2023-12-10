from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def handle_search_get(request):
    url = request.GET.get('url', '')
    match url:
        case "https://yandex.ru":
            query = request.GET.get('query', '')
            if query:
                redirect_url = f"https://yandex.ru/search/?text={query}"
                return redirect(redirect_url)
            else:
                return redirect(url)
        case "https://www.google.com":
            query = request.GET.get('query', '')
            if query:
                redirect_url = f"https://www.google.com/search?q={query}"
                return redirect(redirect_url)
            else:
                return redirect(url)
        case "https://www.bing.com":
            query = request.GET.get('query', '')
            if query:
                redirect_url = f"https://www.bing.com/search?q={query}"
                return redirect(redirect_url)
            else:
                return redirect(url)
    return render(request, 'main/index.html')


def handle_search_post(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        match url:
            case "https://yandex.ru":
                query = request.POST.get('query', '')
                if query:
                    redirect_url = f"https://yandex.ru/search/?text={query}"
                    return redirect(redirect_url)
                else:
                    return redirect(url)
            case "https://www.google.com":
                query = request.POST.get('query', '')
                if query:
                    redirect_url = f"https://www.google.com/search?q={query}"
                    return redirect(redirect_url)
                else:
                    return redirect(url)
            case "https://www.bing.com":
                query = request.POST.get('query', '')
                if query:
                    redirect_url = f"https://www.bing.com/search?q={query}"
                    return redirect(redirect_url)
                else:
                    return redirect(url)
    return render(request, 'main/index.html')
