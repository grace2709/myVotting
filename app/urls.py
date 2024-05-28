from django.urls import path
from . import  views


urlpatterns=[


    path("",views.CreatePoll.as_view(),name="create"),
    path("addchoice/<str:poll_id>/",views.AddChoiceView.as_view(),name="add_choice"),
    path("vote/<str:poll_id>/",views.VoteView.as_view(),name="vote"),
]