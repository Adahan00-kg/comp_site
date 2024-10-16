from rest_framework import viewsets, generics,status, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import CheckOwner


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class Body_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Body_category.objects.all()
    serializer_class = Body_categoryListSerializer


class Body_categoryViewSet(viewsets.ModelViewSet):
    queryset = Body_category.objects.all()
    serializer_class = Body_categorySerializer



class Body_elementViewSet(viewsets.ModelViewSet):
    queryset = Body_element.objects.all()
    serializer_class = Body_elementSerializer




class Power_unit_categoryViewSet(viewsets.ModelViewSet):
    queryset = Power_unit_category.objects.all()
    serializer_class = Power_unit_categorySerializer


class Power_unit_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Power_unit_category.objects.all()
    serializer_class = Power_unit_categoryListSerializer


class Power_unit_elementViewSet(viewsets.ModelViewSet):
    queryset = Power_unit_element.objects.all()
    serializer_class = Power_unit_elementSerializer


class Power_unit_elementListViewSet(viewsets.ModelViewSet):
    queryset = Power_unit_element.objects.all()
    serializer_class = Power_unit_elementListSerializer


class Wi_Fi_categoryViewSet(viewsets.ModelViewSet):
    queryset = Wi_Fi_category.objects.all()
    serializer_class = Wi_Fi_categorySerializer


class Wi_Fi_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Wi_Fi_category.objects.all()
    serializer_class = Wi_Fi_categoryListSerializer


class Wi_Fi_elementViewSet(viewsets.ModelViewSet):
    queryset = Wi_Fi_element.objects.all()
    serializer_class = Wi_Fi_elementerSerializers


class Wi_Fi_elementListViewSet(viewsets.ModelViewSet):
    queryset = Wi_Fi_element.objects.all()
    serializer_class = Wi_Fi_elementerListSerializers


class Sound_card_categoryViewSet(viewsets.ModelViewSet):
    queryset = Sound_card_category.objects.all()
    serializer_class = Sound_card_categorySerializer


class Sound_card_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Sound_card_category.objects.all()
    serializer_class = Sound_card_categoryListSerializer


class Sound_card_elementViewSet(viewsets.ModelViewSet):
    queryset = Sound_card_element.objects.all()
    serializer_class = Sound_card_elementSerializer


class Sound_card_elementListViewSet(viewsets.ModelViewSet):
    queryset = Sound_card_element.objects.all()
    serializer_class = Sound_card_elementListSerializer


class Operating_system_categoryViewSet(viewsets.ModelViewSet):
    queryset = Operating_system_category.objects.all()
    serializer_class = Operating_system_categorySerializer


class Operating_system_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Operating_system_category.objects.all()
    serializer_class = Operating_system_categoryListSerializer


class Operating_system_elementViewSet(viewsets.ModelViewSet):
    queryset = Operating_system_element.objects.all()
    serializer_class = Operating_system_elementSerializer


class Operating_system_elementListViewSet(viewsets.ModelViewSet):
    queryset = Operating_system_element.objects.all()
    serializer_class = Operating_system_elementListSerializer

class Mouse_catergoryViewSet(viewsets.ModelViewSet):
    queryset = Mouse_catergory.objects.all()
    serializer_class = Mouse_catergorySerializer

class Mouse_catergoryListViewSet(viewsets.ModelViewSet):
    queryset = Mouse_catergory.objects.all()
    serializer_class = Mouse_catergoryListSerializer

class Mouse_elementViewSet(viewsets.ModelViewSet):
    queryset = Mouse_element.objects.all()
    serializer_class = Mouse_elementSerializer


class Mouse_elementListViewSet(viewsets.ModelViewSet):
    queryset = Mouse_element.objects.all()
    serializer_class = Mouse_elementListSerializer


class Keyboard_categoryViewSet(viewsets.ModelViewSet):
    queryset = Keyboard_category.objects.all()
    serializer_class = Keyboard_categorySerializer


class Keyboard_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Keyboard_category.objects.all()
    serializer_class = Keyboard_categoryListSerializer


class Keyboard_elementViewSet(viewsets.ModelViewSet):
    queryset = Keyboard_element.objects.all()
    serializer_class = Keyboard_elementSerializer


class Keyboard_elementListViewSet(viewsets.ModelViewSet):
    queryset = Keyboard_element.objects.all()
    serializer_class = Keyboard_elementListSerializer


class Manitor_categoryViewSet(viewsets.ModelViewSet):
    queryset = Manitor_category.objects.all()
    serializer_class = Manitor_categorySerializer


class Manitor_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Manitor_category.objects.all()
    serializer_class = Manitor_categoryListSerializer


class Manitor_elementViewSet(viewsets.ModelViewSet):
    queryset = Manitor_element.objects.all()
    serializer_class = Manitor_elementSerializer


class Manitor_elementListViewSet(viewsets.ModelViewSet):
    queryset = Manitor_element.objects.all()
    serializer_class = Manitor_elementListSerializer


class Headset_elementViewSet(viewsets.ModelViewSet):
    queryset = Headset_element.objects.all()
    serializer_class = Headset_elementSerializer


class Headset_elementListViewSet(viewsets.ModelViewSet):
    queryset = Headset_element.objects.all()
    serializer_class = Headset_elementListSerializer


class Headset_categoryViewSet(viewsets.ModelViewSet):
    queryset = Headset_category.objects.all()
    serializer_class = Headset_categorySerializer


class Headset_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Headset_category.objects.all()
    serializer_class = Headset_categoryListSerializer


class Processor_categoryViewSet(viewsets.ModelViewSet):
    queryset = Processor_category.objects.all()
    serializer_class = Processor_categorySerializer


class Processor_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Processor_category.objects.all()
    serializer_class = Processor_categorySimpleSerializer


class Processor_elementViewSet(viewsets.ModelViewSet):
    queryset = Processor_element.objects.all()
    serializer_class = Processor_elementSerializer



class Processor_elementListViewSet(viewsets.ModelViewSet):
    queryset = Processor_element.objects.all()
    serializer_class = Processor_elementSimpleSerializer



class Cooling_categoryViewSet(viewsets.ModelViewSet):
    queryset = Cooling_category.objects.all()
    serializer_class = Cooling_categorySerializer



class Cooling_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Cooling_category.objects.all()
    serializer_class = Cooling_categorySimpleSerializer


class Cooling_elementViewSet(viewsets.ModelViewSet):
    queryset = Cooling_element.objects.all()
    serializer_class = Cooling_elementSerializer


class Cooling_elementListViewSet(viewsets.ModelViewSet):
    queryset = Cooling_element.objects.all()
    serializer_class = Cooling_elementSimpleSerializer



class Random_access_memory_categoryViewSet(viewsets.ModelViewSet):
    queryset = Random_access_memory_category.objects.all()
    serializer_class = Random_access_memory_categorySerializer

class Random_access_memory_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Random_access_memory_category.objects.all()
    serializer_class = Random_access_memory_categorySimpleSerializer


class Random_access_memory_elementViewSet(viewsets.ModelViewSet):
    queryset = Random_access_memory_element.objects.all()
    serializer_class = Random_access_memory_elementSerializer


class Random_access_memory_elementListViewSet(viewsets.ModelViewSet):
    queryset = Random_access_memory_element.objects.all()
    serializer_class = Random_access_memory_elementSimpleSerializer


class The_motherboard_categoryViewSet(viewsets.ModelViewSet):
    queryset = The_motherboard_category.objects.all()
    serializer_class = The_motherboard_categorySerializer


class The_motherboard_categoryListViewSet(viewsets.ModelViewSet):
    queryset = The_motherboard_category.objects.all()
    serializer_class = The_motherboard_categorySimpleSerializer


class The_motherboard_elementViewSet(viewsets.ModelViewSet):
    queryset = The_motherboard_element.objects.all()
    serializer_class = The_motherboard_elementSerializer

class The_motherboard_elementListViewSet(viewsets.ModelViewSet):
    queryset = The_motherboard_element.objects.all()
    serializer_class = The_motherboard_elementSimpleSerializer


class Video_card_categoryViewSet(viewsets.ModelViewSet):
    queryset = Video_card_category.objects.all()
    serializer_class = Video_card_categorySerializer


class Video_card_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Video_card_category.objects.all()
    serializer_class = Video_card_categorySimpleSerializer


class Video_card_elementViewSet(viewsets.ModelViewSet):
    queryset = Video_card_element.objects.all()
    serializer_class = Video_card_elementSerializer


class Video_card_elementListViewSet(viewsets.ModelViewSet):
    queryset = Video_card_element.objects.all()
    serializer_class = Video_card_elementSimpleSerializer


class Hard_drive_categoryViewSet(viewsets.ModelViewSet):
    queryset = Hard_drive_category.objects.all()
    serializer_class = Hard_drive_categorySerializer


class Hard_drive_categoryListViewSet(viewsets.ModelViewSet):
    queryset = Hard_drive_category.objects.all()
    serializer_class = Hard_drive_categorySimpleSerializer


class Hard_drive_elementViewSet(viewsets.ModelViewSet):
    queryset = Hard_drive_element.objects.all()
    serializer_class = Hard_drive_elementSerializer


class Hard_drive_elementListViewSet(viewsets.ModelViewSet):
    queryset = Hard_drive_element.objects.all()
    serializer_class = Hard_drive_elementSimpleSerializer


class SSD_drive_1_categoryViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_1_category.objects.all()
    serializer_class = SSD_drive_1_categorySerializer


class SSD_drive_1_categoryListViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_1_category.objects.all()
    serializer_class = SSD_drive_1_categorySimpleSerializer


class SSD_drive_1_elementViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_1_element.objects.all()
    serializer_class = SSD_drive_1_elementSerializer


class SSD_drive_1_elementListViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_1_element.objects.all()
    serializer_class = SSD_drive_1_elementSimpleSerializer


class SSD_drive_2_categoryViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_2_category.objects.all()
    serializer_class = SSD_drive_2_categorySerializer


class SSD_drive_2_categoryListViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_2_category.objects.all()
    serializer_class = SSD_drive_2_categorySimpleSerializer


class SSD_drive_2_elementViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_2_element.objects.all()
    serializer_class = SSD_drive_2_elementSerializer


class SSD_drive_2_elementListViewSet(viewsets.ModelViewSet):
    queryset = SSD_drive_2_element.objects.all()
    serializer_class = SSD_drive_2_elementSimpleSerializer


class DVD_drive_categoryViewSet(viewsets.ModelViewSet):
    queryset = DVD_drive_category.objects.all()
    serializer_class = DVD_drive_categorySerializer

class DVD_drive_categoryListViewSet(viewsets.ModelViewSet):
    queryset = DVD_drive_category.objects.all()
    serializer_class = DVD_drive_categorySimpleSerializer

class DVD_drive_elementDetailViewSet(viewsets.ModelViewSet):
    queryset = DVD_drive_element.objects.all()
    serializer_class = DVD_drive_elementSerializer

class DVD_drive_elementListViewSet(viewsets.ModelViewSet):
    queryset = DVD_drive_element.objects.all()
    serializer_class = DVD_drive_elementSimpleSerializer



class ShowcompViewSet(viewsets.ModelViewSet):
    queryset = Showcomp.objects.all()
    serializer_class = ShowCompSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = self.get_serializer(cart)
        return Response(serializer.data)


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart_user=self.request.user)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)
