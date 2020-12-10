from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # url example: /polls/
    path('', views.index, name='index'),

    # url example: /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),

    # url example: /polls/1/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # url example: /polls/1/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
