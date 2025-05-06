from collections import defaultdict
from django.shortcuts import render
from django.http import JsonResponse
from collections import defaultdict
from .models import seeds ,x
from .forms import SEED_SEARCH
# Create your views here.

def pagehome(request):
    categories = seeds.objects.values_list('catgory', flat=True).distinct()
    print("الفئات الموجودة بدون تكرار:", list(categories))
    return render(request,'alfajr/index.html' ,{'categories':categories})

def product(request, category):
    # جلب كل المنتجات من الفئة المحددة
    all_seeds = seeds.objects.filter(catgory=category).order_by('classification')


    return render(request, 'alfajr/product.html', {
        'seed': all_seeds,
        
        'category': category,
    })

def search(request):
    query = SEED_SEARCH(request.GET or None)
    results = []

    if request.method == 'GET' and query.is_valid():
        search_query = query.cleaned_data.get('search_query')
        if search_query:  # ← فقط إذا المستخدم كتب شي
            results = seeds.objects.filter(name_s__icontains=search_query).order_by('name_s')

    return render(request, 'alfajr/product_search.html', {'results': results, 'query': query})

# myapp/views.py

def search_e(request):
    query = request.GET.get('q', '')
    if query:
        seeds_found = seeds.objects.filter(name_s__icontains=query)
        results = []
        for seed in seeds_found:
            results.append({
                'name_s': seed.name_s,
                'img_url': seed.img_url or '',
            })
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)

