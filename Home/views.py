from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def services(request, name):
    page_map = {
        'Maha-Saraswathy-Temple':'product-one.html',
        'Garbha-Rakshamibgai' : 'product-two.html',
        'Karuvalarcheri-Amman' : 'product-three.html',
        'Rajagopalaswamy-Temple' : 'product-four.html',
        'Vanadurga-Devi-Temple' : 'product-five.html',
        'Durga-Devi-Temple' : 'product-six.html',
        'Garbha-Rakshamibgai-Thirukarukavoor' : 'product-seven.html',
        'Guru-Bagavan-Temple' : 'product-eight.html'
    }
    return render(request, page_map[name])

def faq(request):
    return render(request, 'faq.html')

def dfc(request):
    return render(request, 'donation-for-cause.html')

def PujaOnline(request):
    return render(request, 'puja-online.html')

def TandC(request):
    return render(request, 'terms-and-conditions.html')

def Privacy(request):
    return render (request, 'privacy.html')
