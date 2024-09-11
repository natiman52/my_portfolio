from django.urls import path
from .views import home,Get_Token,AboutFetch,WorkFetch,SkiilFetch,WorkExperienceFetch,BrandFetch,PostContact
from django.views.decorators.csrf import csrf_protect,csrf_exempt
urlpatterns = [
    path("", home),
    path('get_token/',Get_Token),
    path("about/",AboutFetch),
    path('work/',WorkFetch),
    path('work-experiance/',WorkExperienceFetch),
    path('skill/',SkiilFetch),
    path("brand/",BrandFetch),
    path("contact/",PostContact.as_view())
]