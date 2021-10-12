from django.urls import path
from project import views

urlpatterns=[
    path('account/signup',views.SignUpViews.as_view()),
    path('account/signin',views.SigninView.as_view())
]