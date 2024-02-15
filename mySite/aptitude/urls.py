
# # aptitude/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.aptitude, name='home'),
#     path('quiz/<int:category_id>/', views.quiz, name='quiz'),
# ]


from django.urls import path
# from .views import aptitude, aptitude_test_result
from aptitude import views


urlpatterns = [
    path('/', views.aptitude, name='aptitude'),
    path('/aptitude1', views.aptitude1, name='aptitude1'),
    path('/aptitude2', views.aptitude2, name='aptitude2'),
    path('/aptitude3', views.aptitude3, name='aptitude3'),
    path('/result', views.result, name='result'),
    # path('aptitude-test-result/', views.aptitude_test_result, name='aptitude_test_result'),
]