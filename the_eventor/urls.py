"""
URL configuration for the_eventor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appeventor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="index"),
    path('about/',views.about,name="about"),
    path('rent-venue/',views.rent_venue,name="rent-venue"),
    path('shows-events/',views.shows_events,name="shows-events"),
    path('corporate_party/',views.corporate_party,name="corporate_party"),
    path('tickets/',views.tickets,name="tickets"),
    path('ticket-details/',views.ticket_details,name="ticket-details"),
    path('event-details/',views.event_details,name="event-details"),
    path('login_user/',views.user_login,name="login_user"),
    path('register/',views.user_register,name="register"),
    path('logout/',views.user_logout,name="logout"),
    path('payment/', views.fake_payment_view, name='payment_page'),
    path('payment_success/<str:transaction_id>', views.payment_success, name='payment_success'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    #Admin urls 
    path("adminhome/",views.adminhome,name="adminhome"),
    path("subscription/",views.subscription,name="subscription"),
    path("client-profile/",views.client_profile,name="client-profile"),
    path("send-suggestions/",views.send_suggestions,name="send-suggestions"),
    path("users-profile/",views.admin_profile,name="users-profile"),
    path("view-documents/",views.view_documents,name="view-documents"),
    path("view-receive-payment/",views.view_receive_payment,name="view-receive-payment"),
    path("view-suggestions/",views.view_suggestions,name="view-suggestions"),
    path("user_edit/<int:id>",views.user_edit,name="user_edit"),
    path("pages_login/",views.pages_login,name="pages_login"),
    path("admin_logout/",views.admin_log_out,name="admin_logout"),
    path("get-notifications",views.get_notification_count,name="get-notifications"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("update/<int:id>",views.update,name="update"),
    
    #client urls
    path("clienthome/",views.clienthome,name="clienthome"),
    path("payment_info/",views.payment_info,name="payment_info"),
    path("profile/",views.profile,name="profile"),
    path("document/",views.document,name="document"),
    path("delete_data/",views.deletedata,name="delete_data"),
    path("send_query/",views.send_query,name="send_query"),
    path("view_suggestion/",views.view_suggestion,name="view_suggestion"),
   path('upload/', views.document, name="upload_document"),
   path('send_inquiry/', views.send_email, name="send_inquiry"),
    # path("update/<int:id>",views.update,name="update"),
    # path("delete/<int:id>",views.datadelete,name="delete"),
    #  path("datashow/",views.datashow,name="datashow"),
]
