from django.shortcuts import render

# home page
def home_page_view(request):
    context = {}
    return render(request, 'jade_island_media/index.html', context=context)




# error pages
def handler404(request, exception):
    return render(request, 'jade_island_media/error_pages/404.html', status=404)

def handler500(request):
    return render(request, 'jade_island_media/error_pages/500.html', status=500)