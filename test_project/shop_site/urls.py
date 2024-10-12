from django.urls import path
from .views import *


urlpatterns = [
    path('',MainCompViewSet.as_view({'get':'list'}),name = 'main_list'),


    path('body/', Body_categoryViewSet.as_view({'get': 'list'}), name='body_list'),
    path('body/<int:pk>/', Body_elementViewSet.as_view({'get': 'retrieve'}),name='body_detail'),

    path('power/', Power_unit_categoryViewSet.as_view({'get': 'list'}), name='power_list'),
    path('power/<int:pk>/', Power_unit_elementViewSet.as_view({'get': 'retrieve'}),name='power_detail'),

    path('user/', Body_categoryViewSet.as_view({'get': 'list'}), name='body_list'),
    path('user/<int:pk>/', Body_elementViewSet.as_view({'get': 'retrieve'}),name='body_detail'),

    path('wi_fi/', Wi_Fi_categoryViewSet.as_view({'get': 'list'}), name='wi_fi_list'),
    path('wi_fi/<int:pk>/', Wi_Fi_elementViewSet.as_view({'get': 'retrieve'}),name='wi_fi_detail'),

    path('card/', Sound_card_categoryViewSet.as_view({'get': 'list'}), name='card_list'),
    path('card/<int:pk>/', Sound_card_elementViewSet.as_view({'get': 'retrieve'}), name='card_detail'),

    path('system/', Operating_system_categoryViewSet.as_view({'get': 'list'}), name='system_list'),
    path('system/<int:pk>/', Operating_system_elementViewSet.as_view({'get': 'retrieve'}), name='system_detail'),

    path('mouse/', Mouse_catergoryViewSet.as_view({'get': 'list'}), name='mouse_list'),
    path('mouse/<int:pk>/', Mouse_elementViewSet.as_view({'get': 'retrieve'}), name='mouse_detail'),

    path('keyboard/', Keyboard_categoryViewSet.as_view({'get': 'list'}), name='keyboard_list'),
    path('keyboard/<int:pk>/', Keyboard_elementViewSet.as_view({'get': 'retrieve'}), name='keyboard_detail'),

    path('manitor/', Manitor_categoryViewSet.as_view({'get': 'list'}), name='manitor_list'),
    path('manitor/<int:pk>/', Manitor_elementViewSet.as_view({'get': 'retrieve'}), name='manitor_detail'),

    path('headset/', Headset_categoryViewSet.as_view({'get': 'list'}), name='headset_list'),
    path('headset/<int:pk>/', Headset_elementViewSet.as_view({'get': 'retrieve'}), name='headset_detail'),

    path('processor/', Processor_categoryViewSet.as_view({'get': 'list'}), name='processor_list'),
    path('processor/<int:pk>/', Processor_elementViewSet.as_view({'get': 'retrieve'}), name='processor_detail'),

    path('cooling/', Cooling_categoryViewSet.as_view({'get': 'list'}), name='cooling_list'),
    path('cooling/<int:pk>/', Cooling_elementViewSet.as_view({'get': 'retrieve'}), name='cooling_detail'),

    path('random_access/', Random_access_memory_categoryViewSet.as_view({'get': 'list'}), name='random_access_list'),
    path('random_access/<int:pk>/', Random_access_memory_elementViewSet.as_view({'get': 'retrieve'}),
         name='random_access_detail'),

    path('the_motherboard/', The_motherboard_categoryViewSet.as_view({'get': 'list'}), name='the_motherboard_list'),
    path('the_motherboard/<int:pk>/', The_motherboard_elementViewSet.as_view({'get': 'retrieve'}),
         name='the_motherboard_detail'),

    path('video_card/', Video_card_categoryViewSet.as_view({'get': 'list'}), name='video_card_list'),
    path('video_card/<int:pk>/', Video_card_elementViewSet.as_view({'get': 'retrieve'}), name='video_card_detail'),

    path('hard_drive/', Hard_drive_categoryViewSet.as_view({'get': 'list'}), name='hard_drive_list'),
    path('hard_drive/<int:pk>/', Hard_drive_elementViewSet.as_view({'get': 'retrieve'}), name='hard_drive_detail'),

    path('ssd_drive_1/', SSD_drive_1_categoryViewSet.as_view({'get': 'list'}), name='ssd_drive_1_list'),
    path('ssd_drive_1/<int:pk>/', SSD_drive_1_elementViewSet.as_view({'get': 'retrieve'}), name='ssd_drive_1_list'),

    path('ssd_drive_2/', SSD_drive_2_categoryViewSet.as_view({'get': 'list'}), name='ssd_drive_2_list'),
    path('ssd_drive_2/<int:pk>/', SSD_drive_2_elementViewSet.as_view({'get': 'retrieve'}), name='ssd_drive_2_list'),

    path('dvd_drive/', DVD_drive_categoryViewSet.as_view({'get': 'list'}), name='dvd_drive_list'),
    path('dvd_drive/<int:pk>/', DVD_drive_elementViewSet.as_view({'get': 'retrieve'}), name='dvd_drive_detail'),

]