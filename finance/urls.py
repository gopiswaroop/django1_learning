from django.urls import path
from finance.views import feeDue
from finance.views import feeReport
from finance.views import feeCollection
urlpatterns = [
    path('feecol/', feeCollection),
    path('feedue/', feeDue),
    path('feerep/', feeReport),
]