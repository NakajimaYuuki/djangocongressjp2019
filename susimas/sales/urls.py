from django.conf.urls import url, include
from django.contrib.auth import views
from django.urls import path

from sales.views import IndexView

app_name = 'sales'

urlpatterns = [
    # 売上げ一覧
    # url(r'^', IndexView.as_view(), name="index"),
    path('', IndexView.as_view(), name='index'),
    ]
