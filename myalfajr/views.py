from django.shortcuts import render
from django.http import JsonResponse
from .models import seeds
# Create your views here.

def pagehome(request):
    return render(request,'alfajr/index.html')

def product(request, category):
    all_seeds = seeds.objects.filter(catgory=category)
    if request.GET.get('show') == 'all':
        first_seeds = all_seeds  # عرض الكل
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
    query = request.GET.get('q', '')
    if query:
        # بحث حسب الاسم أو أي معيار تاني
        seeds_found = seeds.objects.filter(name_s__icontains=query)
        results = []
        for seed in seeds_found:
            results.append({
                'name_s': seed.name_s,
                'img_s': seed.img_s.url,
            })
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)

#def search_product(request):
#    query = request.GET.get('q', '')
#    if query:
#        results = seeds.objects.filter(name_s__icontains=query).values('name_s', 'img_s')
#        data = list(results)
#    else:
#        data = []
#    return JsonResponse(data, safe=False)
