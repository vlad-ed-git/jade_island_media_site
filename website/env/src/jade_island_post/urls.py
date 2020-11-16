from django.urls import path
from .views import(
    create_jade_island_post_view,
)

app_name = 'jade_island_post'
urlpatterns = [
    path('create/', create_jade_island_post_view, name='create'),
]
