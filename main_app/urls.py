from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('stepsheets/', views.sheet_index, name='index'),
    path('stepsheets/<int:sheet_id>/', views.sheet_detail, name='detail'),
    path('stepsheets/submit/', views.SheetCreate.as_view(), name='sheets_create'),
    path('stepsheets/<int:pk>/update/', views.SheetUpdate.as_view(), name='sheets_update'),
    path('stepsheets/<int:pk>/delete/', views.SheetDelete.as_view(), name='sheets_delete'),
    path('choreographers/', views.ChoreoList.as_view(), name='choreo_index'),
    path('choreographers/<int:pk>', views.ChoreoDetail.as_view(), name='choreo_detail'),
    path('choreographers/add', views.ChoreoCreate.as_view(), name='choreo_create'),
    path('choreographers/<int:pk>/update', views.ChoreoDetail.as_view(), name='choreo_update'),
    path('stepsheets/<int:sheet_id>/assoc_choreo/<int:choreo_id>/', views.assoc_choreo, name='assoc_choreo'),
    path('accounts/signup/', views.signup, name='signup'),
    path('videos/submit/', views.VideoCreate.as_view(), name='videos_create'),
    path('stepsheets/<int:sheet_id>/assoc_video/<int:choreo_id>/', views.assoc_video, name='assoc_video'),
]