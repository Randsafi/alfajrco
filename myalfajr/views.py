from django.shortcuts import render
from django.http import JsonResponse
from .models import seeds
from .forms import SEED_SEARCH
# Create your views here.

def pagehome(request):
    categories = seeds.objects.values_list('catgory', flat=True).distinct()
    print("الفئات الموجودة بدون تكرار:", list(categories))
    return render(request,'alfajr/index.html' ,{'categories':categories})

def product(request, category):
    all_seeds = seeds.objects.filter(catgory=category).order_by('name_s')

    if request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.GET.get('show') == 'all':
        results = []
        for seed in all_seeds:
            results.append({
                'name_s': seed.name_s,
                'img_url': seed.img_url,
            })
        return JsonResponse({'seeds': results})

    if request.GET.get('show') == 'all':
        first_seeds = all_seeds
        show_more = False
    else:
        first_seeds = all_seeds[:8]
        show_more = all_seeds.count() > 8

    return render(request, 'alfajr/product.html', {
        'seed': first_seeds,
        'show_more': show_more,
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

