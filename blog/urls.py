from django.urls import path
from .views import BlogListView, BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns =[
    path('', BlogListView.as_view(), name ='home'),
    path('<int:pk>/', BlogDetailView.as_view(), name = 'detail' ),
    path('new/', BlogCreateView.as_view(), name ='post_new' ),
    path('new/<int:pk>/update/', BlogUpdateView.as_view(), name='post_update'),
    path('new/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),

]