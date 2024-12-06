from django.urls import path
from . views import RegisterEmployeeView,EmployeeDetail

urlpatterns = [
    path('register/',RegisterEmployeeView.as_view(),name='register'),
    path('<int:pk>/',EmployeeDetail.as_view(),name='employee-detail'),

]