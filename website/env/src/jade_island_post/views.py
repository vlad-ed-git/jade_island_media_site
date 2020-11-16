from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateJadeIslandPostForm, UpdateJadeIslandPostForm
from account.models import Account
from .models import JadeIslandPost
from django.db.models import F, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from jade_analytics.views import saveAnalytics

# Create your views here.
def create_jade_island_post_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')
    form = CreateJadeIslandPostForm(
        request.POST or None, request.FILES or None)
    if form.is_valid():
        # we need to set the author property before we can save
        obj = form.save(commit=False)
        author = Account.objects.get(email=user.email)
        obj.author = author
        obj.save()
        context['successfully_created_post'] = True
        form = CreateJadeIslandPostForm()
    else:
        context['failed'] = True
        form.initial = {
            "title": request.POST.get("title"),
            "body": request.POST.get("body"),
            "post_category": request.POST.get("post_category"),
            "location": request.POST.get("location"),
            "contact": request.POST.get("contact"),
            "job_start_date": request.POST.get("job_start_date"),
            "sale_item_price_rmb": request.POST.get("sale_item_price_rmb"),
            "event_start_date": request.POST.get("event_start_date"),
            "event_end_date": request.POST.get("event_end_date"),
            "url_field": request.POST.get("url_field"),
            "event_category": request.POST.get("event_category"),
            "place_category": request.POST.get("place_category"),
            "sale_category": request.POST.get("sale_category"),
            "job_category": request.POST.get("job_category"),
            "job_type": request.POST.get("job_type"),
            "featured_image": request.POST.get("featured_image"),
            "extra_image_one": request.POST.get("extra_image_one"),
            "extra_image_two": request.POST.get("extra_image_two"),
            "extra_image_three": request.POST.get("extra_image_three"),
            "extra_image_four": request.POST.get("extra_image_four"),
            "extra_image_five": request.POST.get("extra_image_five"),
            "extra_image_six": request.POST.get("extra_image_six"),
            "extra_image_seven": request.POST.get("extra_image_seven"),
            "extra_image_eight": request.POST.get("extra_image_eight"),
            "extra_image_nine": request.POST.get("extra_image_nine"),
            "tags": request.POST.get("tags"),
            "is_featured": request.POST.get("is_featured"),
            "is_approved": request.POST.get("is_approved"),
        }
    context['create_form'] = form
    return render(request, 'jade_island_media/forms/create_post.html', context)
