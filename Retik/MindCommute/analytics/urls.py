from django.urls import path
from .views import CreateJournal, JournalList, JournalDetail

urlpatterns = [
    path('create', CreateJournal.as_view(), name = 'createjournal'),
    path('journal', JournalList.as_view(), name = 'journallist'),
    path('journal/<pk>/', JournalDetail.as_view(), name = 'journaldetail'),
]
