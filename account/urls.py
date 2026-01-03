from django.urls import path, include  
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'account'
urlpatterns = [
    # مسارات تسجيل الدخول والخروج
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # مسارات تغيير كلمة السر
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # مسارات إعادة تعيين كلمة السر (Reset)
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # المسارات الأساسية
    path('', views.dashboard, name='dashboard'),
    path('edit/', views.edit, name='edit'), 
    path('scientific/', views.research_scientifique, name='scientific'),
    path('analysis/', views.data_analysis, name='data_analysis'),
    path('database/', views.database_repo, name='database'),
    path('support/', views.support, name='support'),
    path('tools/', views.tools, name='tools'),
    path('community/', views.community, name='community'),
    path('contact/', views.contact_view, name='contact'),
    path("scientific/mutations/", views.mutation_analysis, name="mutation_analysis"),
    path("scientific/bioinformatics/", views.bioinformatics_analysis, name="bioinformatics_analysis"),
    path("scientific/rna-seq/", views.rna_seq_analysis, name="rna_seq_analysis"),
    path('about-disease/', views.disease_about_view, name='about_disease'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
