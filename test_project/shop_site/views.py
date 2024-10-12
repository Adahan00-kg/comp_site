from rest_framework import viewsets
from .serializers import *



class Body_categoryViewSet(viewsets.ModelViewSet):
    queryset = Body_category.objects.all()
    serializer_class = Body_categorySerializerList


class Body_elementViewSet(viewsets.ModelViewSet):
    queryset = Body_element.objects.all()
    serializer_class = Body_elementSerializer


class Power_unit_categoryViewSet(viewsets.ModelViewSet):
    queryset = Power_unit_category.objects.all()
    serializer_class = Power_unit_categorySerializer


class Power_unit_elementViewSet(viewsets.ModelViewSet):
    queryset = Power_unit_element.objects.all()
    serializer_class = Power_unit_elementSerializer


class Wi_Fi_categoryViewSet(viewsets.ModelViewSet):
    queryset = Wi_Fi_category.objects.all()
    serializer_class = Wi_Fi_categorySerializer


class Wi_Fi_elementViewSet(viewsets.ModelViewSet):
    queryset = Wi_Fi_element.objects.all()
    serializer_class = Wi_Fi_elementerSerializers


class Sound_card_categoryViewSet(viewsets.ModelViewSet):
    queryset = Sound_card_category.objects.all()
    serializer_class = Sound_card_categorySerializer


class Sound_card_elementViewSet(viewsets.ModelViewSet):
    queryset = Sound_card_element.objects.all()
    serializer_class = Sound_card_elementSerializer


class Operating_system_categoryViewSet(viewsets.ModelViewSet):
    queryset = Operating_system_category.objects.all()
    serializer_class = Operating_system_categorySerializer


class Operating_system_elementViewSet(viewsets.ModelViewSet):
    queryset = Operating_system_element.objects.all()
    serializer_class = Operating_system_elementSerializer


class Mouse_catergoryViewSet(viewsets.ModelViewSet):
    queryset = Mouse_catergory.objects.all()
    serializer_class = Mouse_catergorySerializer


class Mouse_elementViewSet(viewsets.ModelViewSet):
    queryset = Mouse_element.objects.all()
    serializer_class = Mouse_elementSerializer


class Keyboard_categoryViewSet(viewsets.ModelViewSet):
    queryset = Keyboard_category.objects.all()
    serializer_class = Keyboard_categorySerializer


class Keyboard_elementViewSet(viewsets.ModelViewSet):
    queryset = Keyboard_element.objects.all()
    serializer_class = Keyboard_elementSerializer


class Manitor_categoryViewSet(viewsets.ModelViewSet):
    queryset = Manitor_category.objects.all()
    serializer_class = Manitor_categorySerializer


class Manitor_elementViewSet(viewsets.ModelViewSet):
    queryset = Manitor_element.objects.all()
    serializer_class = Manitor_elementSerializer


class Headset_elementViewSet(viewsets.ModelViewSet):
    queryset = Headset_element.objects.all()
    serializer_class = Headset_elementSerializer


class Headset_categoryViewSet(viewsets.ModelViewSet):
    queryset = Headset_category.objects.all()
    serializer_class = Headset_categorySerializer



class Processor_categoryViewSet(viewsets.ModelViewSet):
    queryset = Processor_category.objects.all()
    serializer_class = Processor_categorySerializer


class Processor_elementViewSet(viewsets.ModelViewSet):
    queryset = Processor_element.objects.all()
    serializer_class = Processor_elementSerializer


class Cooling_categoryViewSet(viewsets.ModelViewSet):
    queryset = Cooling_category.objects.all()
    serializer_class = Cooling_categorySerializer

class Cooling_elementViewSet(viewsets.ModelViewSet):
    queryset = Cooling_element.objects.all()
    serializer_class = Cooling_elementSerializer


class Random_access_memory_categoryViewSet(viewsets.ModelViewSet):
    queryset = Random_access_memory_category.objects.all()
    serializer_class = Random_access_memory_categorySerializer


class Random_access_memory_elementViewSet(viewsets.ModelViewSet):
    queryset = Random_access_memory_element.objects.all()
    serializer_class = Random_access_memory_elementSerializer


class The_motherboard_categoryViewSet(viewsets.ModelViewSet):
    queryset = The_motherboard_category.objects.all()
    serializer_class = The_motherboard_categorySerializer

class The_motherboard_elementViewSet(viewsets.ModelViewSet):
    queryset = The_motherboard_element.objects.all()
    serializer_class = The_motherboard_elementSerializer


class Video_card_categoryViewSet(viewsets.ModelViewSet):
    queryset = Video_card_category.objects.all()
    serializer_class = Video_card_categorySerializer


class Video_card_elementViewSet(viewsets.ModelViewSet):
    queryset = Video_card_element.objects.all()
    serializer_class = Video_card_elementSerializer


class Hard_drive_categoryViewSet(viewsets.ModelViewSet):
    queryset = Hard_drive_category.objects.all()
    serializer_class = Hard_drive_categorySerializer


class Hard_drive_elementViewSet(viewsets.ModelViewSet):
    queryset = Hard_drive_element.objects.all()
    serializer_class = Hard_drive_elementSerializer


class SSD_drive_1_categoryViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_1_category.objects.all()
    serializer_class = SSD_drive_1_categorySerializer


class SSD_drive_1_elementViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_1_element.objects.all()
    serializer_class = SSD_drive_1_elementSerializer


class SSD_drive_2_categoryViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_2_category.objects.all()
    serializer_class = SSD_drive_2_categorySerializer


class SSD_drive_2_elementViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_2_element.objects.all()
    serializer_class = SSD_drive_2_elementSerializer


class DVD_drive_categoryViewSet(viewsets.ModelViewSet):
    queryset = DVD_drive_category.objects.all()
    serializer_class = DVD_drive_categorySerializer


class DVD_drive_elementViewSet(viewsets.ModelViewSet):
    queryset = DVD_drive_element.objects.all()
    serializer_class = DVD_drive_elementSerializer

class ShowcompViewSet(viewsets.ModelViewSet):
    queryset = Showcomp.objects.all()
    serializer_class = MainCompSerializer