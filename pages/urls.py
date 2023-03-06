from django.urls import path
from .views import about_page_view, george_page_view, home_page_view
from .views import home_post, results


urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_page_view, name='about'),
    path('george/', george_page_view, name='george'),
    path('homePost/', home_post, name='home_post'),
    path('results/<int:choice>/<str:gmat>/', results, name='results')
]
