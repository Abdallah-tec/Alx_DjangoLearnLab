from django.urls import path
from . import views
from .views import list_books , LibraryDetailView

urlpatterns = [
    path('booklist/',views.list_books, name = "list_books"),
    path('librarylist/<int:pk>/',views.LibraryDetailView.as_view(), name ="librarylist"),
    path('admin/', views.admin_view, name = "admin"),
    path('librarian/', views.librarian_view, name = "librarian"),
    path('member/', views.member_view, name = 'member'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('logout/',views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('register/',views.register.as_view(), name = 'register'),
    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('admin/', views.admin_view, name = 'admin_view'),
    path('librarian/', views.librarian_view, name = 'librarian_view'),
    path('member/', views.member_view, name = 'member_view'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('edit_book/', views.edit_book, name = 'edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]