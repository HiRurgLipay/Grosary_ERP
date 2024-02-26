from django.urls import path
from . import views


urlpatterns = [
    # URL для начала опроса
    path('registration', views.register, name='register'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('survey/', views.start_survey, name='start_survey'),
    path('save_answer/', views.save_answer, name='save_answer'),
    path('question/<int:question_id>/<int:survey_id>/', views.get_question, name='get_question'),
    path('admin_panel/', views.add_question, name='admin_panel'),
    path('add_answer/', views.add_answer, name='add_answer'),
    path('survey-complete/', views.survey_complete, name='survey_complete'),
    path('survey-complete/public_catering.html', views.public_catering_view, name='public_catering'),
    path('survey-complete/retail.html', views.retail_view, name='retail'),
    path('survey-complete/appointment.html', views.appointment_view, name='appointment'),
]   