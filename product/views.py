from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)
    page = request.GET.get('page') #page parametrei alarak,kullanıcının görmek istediği sayfa numarasısıdır.Url page parametresi ekledik.
    #Kullanıcı ilk sayfayı görmek istiyorsa, URL şu şekilde olabilir: http://example.com/products?page=1
    #Kullanıcı ikinci sayfayı görmek istiyorsa, URL şu şekilde olabilir: http://example.com/products?page=2
    #Django'da, bu page parametresini request.GET.get('page') ile alıyoruz. Bu ifade, URL'de page parametresine karşılık gelen değeri alı
        
    try:
        products = paginator.page(page) #istenen sayfadaki ürün
    except PageNotAnInteger:
        products = paginator.page(1)  #eğer kullanıcı geçersiz urlde bir ınt değer girerse eğer  ilk sayfaya yollar.
    except EmptyPage:
        products = paginator.page(paginator.num_pages) #geçerli sayfa numarası girere fakat o kadar sayfa yoksa eğerson sayfaya gider
    
    context = {
        'products': products,
    }
    
    return render(request, 'index.html', context)
