from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator



class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True,
                                           validators=[MinValueValidator(18), MaxValueValidator(100)])
    phone_number = PhoneNumberField(null=True, blank=True, region='KG')
    password = models.CharField(max_length=100)
    date_register = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Processor_category(models.Model):   #Процессор
    processor_category_name = models.CharField(max_length=100,  unique=True)

    def __str__(self):
        return self.processor_category_name


class Cooling_category(models.Model): #Охлаждение
    cooling_category_name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.cooling_category_name

class Random_access_memory_category(models.Model): #Оперативная память
    access_memory_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
          return self.access_memory_category_name

class The_motherboard_category(models.Model): #Материнская плата
    motherboard_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.motherboard_category_name


class Video_card_category(models.Model): #Видеокарта
    video_card_category_name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.video_card_category_name

class Hard_drive_category(models.Model):  # Жёсткий диск
    drive_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.drive_category_name


class SSD_drive_1_category(models.Model):  # SSD диск 1
    ssd_drive_1_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.ssd_drive_1_category_name

class SSD_drive_2_category(models.Model):  # SSD диск 2
    ssd_2_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.ssd_2_category_name


class DVD_drive_category(models.Model): #DVD-привод
    dvd_drive_category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.dvd_drive_category_name





class Processor_element(models.Model):
    middle_processor_conaction = models.ForeignKey(Processor_category, related_name='middle_processor_conaction', on_delete=models.CASCADE)
    processor_element_name = models.CharField(max_length=100, verbose_name='Name')
    soket = models.CharField(verbose_name='Сокет', max_length=100, null=True, blank=True)
    l3_cache_size = models.PositiveSmallIntegerField(default=0, verbose_name='Объем кэша L3', null=True, blank=True)
    number_of_cores = models.PositiveSmallIntegerField(default=0, verbose_name='Количество ядер', null=True, blank=True)
    processor_frequency = models.PositiveSmallIntegerField(default=0, verbose_name='Частота процессора', null=True, blank=True)
    technical_process = models.CharField(max_length=100, verbose_name='Техпроцесс', null=True, blank=True)
    the_core = models.CharField(max_length=100, verbose_name='Ядро', null=True, blank=True)
    maximum_frequency_with_turbo_boost = models.PositiveSmallIntegerField(verbose_name='Максимальная частота с Turbo Boost', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    processor_image = models.ImageField(upload_to='Processor_images/', null=True, blank=True)

    def __str__(self):
        return self.processor_element_name




class Cooling_element(models.Model):
    middle_cooling_conaction = models.ForeignKey(Cooling_category, related_name='middle_cooling_conaction', on_delete=models.CASCADE)
    cooling_element_name = models.CharField(max_length=100, verbose_name='Name')
    radiator_material = models.CharField(max_length=100, verbose_name='Материал радиатора', null=True, blank=True)
    cooler_height = models.PositiveSmallIntegerField(default=0, verbose_name='Высота кулера', null=True, blank=True)
    number_of_heat_pipes = models.PositiveSmallIntegerField(default=0, verbose_name='Количество тепловых трубок', null=True, blank=True)
    rotation_speed = models.CharField(max_length=100, verbose_name='Скорость вращения', null=True, blank=True)
    air_flow = models.CharField(max_length=100, verbose_name='Воздушный поток', null=True, blank=True)
    noise_level = models.DecimalField(max_digits=500, decimal_places=2, verbose_name='Уровень шума', null=True, blank=True)
    type_of_bearing = models.CharField(max_length=100, verbose_name='Тип подшипника', null=True, blank=True)
    the_backlight = models.CharField(max_length=100, verbose_name='Подсветка', null=True, blank=True)
    uptime = models.PositiveSmallIntegerField(default=0, verbose_name='Время безотказной работы', null=True, blank=True)
    weight = models.PositiveSmallIntegerField(default=0, verbose_name='Вес', null=True, blank=True)
    water_block_material = models.CharField(max_length=100, verbose_name='Материал водоблока', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    cooling_image = models.ImageField(upload_to='Cooling_images/', null=True, blank=True)

    def __str__(self):
        return self.cooling_element_name


class The_motherboard_element(models.Model):
    middle_the_motherboard_conaction = models.ForeignKey(The_motherboard_category, related_name='middle_the_motherboard_conaction', on_delete=models.CASCADE)
    motherboard_element_name = models.CharField(max_length=100, verbose_name='Name')
    the_form_factor = models.CharField(max_length=100, verbose_name='Форм-фактор', null=True, blank=True)
    number_of_lots = models.PositiveSmallIntegerField(default=0, verbose_name='Количество слотов памяти', null=True, blank=True)
    chipset = models.CharField(max_length=100, verbose_name='Чипсет', null=True, blank=True)
    sound = models.CharField(max_length=100, verbose_name='Звук', null=True, blank=True)
    socket = models.PositiveSmallIntegerField(default=0, verbose_name='Socket', null=True, blank=True)
    slot_expansion = models.CharField(max_length=100, verbose_name='Слоты расширения', null=True, blank=True)
    slot_type_m = models.CharField(max_length=100, verbose_name='Тип слотов M.2', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    motherboard_element_images = models.ImageField(upload_to='motherboard_element_images/', null=True, blank=True)

    def __str__(self):
        return self.motherboard_element_name




class Random_access_memory_element(models.Model):
    middle_memory_conaction = models.ForeignKey(Random_access_memory_category, related_name='middle_memory_conaction', on_delete=models.CASCADE)
    access_memory_element_name = models.CharField(max_length=100)
    memory_type = models.CharField(max_length=100, verbose_name='Тип памяти', null=True, blank=True)
    the_form_factor = models.CharField(max_length=100, verbose_name='Форм-фактор', null=True, blank=True)
    clock_frequency = models.CharField(max_length=100, verbose_name='Тактовая частота', null=True, blank=True)
    bandwidth = models.CharField(max_length=100, verbose_name='Пропускная', )
    supply_voltage = models.DecimalField(max_digits=50, decimal_places=2, verbose_name='Напряжение питания')
    volume = models.PositiveSmallIntegerField(default=0, verbose_name='Объем', null=True, blank=True)
    radiator = models.BooleanField(default=False, verbose_name='Радиатор')
    xmp_support = models.BooleanField(default=False, verbose_name='Поддержка XMP')
    price = models.PositiveSmallIntegerField(default=0)
    memory_element_images = models.ImageField(upload_to='memory_element_images', null=True, blank=True)

    def __str__(self):
        return self.access_memory_element_name





class Video_card_element(models.Model):
    middle_video_card_conaction = models.ForeignKey(Video_card_category, related_name='middle_video_card_conaction',  on_delete=models.CASCADE)
    card_element_name = models.CharField(max_length=100)
    graphics_processor = models.CharField(max_length=100, verbose_name='Графический процессор', null=True, blank=True)
    recommended_power_supply_power_supply = models.CharField(max_length=100, verbose_name='Рекомендуемая мощность блока питания', null=True, blank=True)
    technical_process = models.CharField(max_length=100, verbose_name='Техпроцесс', null=True, blank=True)
    the_amount_of_video_memory = models.CharField(max_length=100, verbose_name='Объем видеопамяти', null=True, blank=True)
    video_memory_bus_bit_rate = models.CharField(max_length=100, verbose_name='Разрядность шины видеопамяти', null=True, blank=True)
    cuda_support = models.CharField(max_length=100, verbose_name='Поддержка CUDA', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    card_element_images = models.ImageField(upload_to='card_element_images/', null=True, blank=True)

    def __str__(self):
        return self.card_element_name





class Hard_drive_element(models.Model):
    middle_hard_drive_conaction = models.ForeignKey(Hard_drive_category, related_name='drive_element',
                                                    on_delete=models.CASCADE)
    drive_element_name = models.CharField(max_length=100)
    volume = models.CharField(max_length=100, verbose_name='Объем', null=True, blank=True)
    type = models.CharField(max_length=100, verbose_name='Тип', null=True, blank=True)
    recording_speed_reading_speed = models.CharField(max_length=100, verbose_name='Скорость записи/Скорость чтения',
                                                     null=True, blank=True)
    the_amount_of_buffer_memory = models.CharField(max_length=100, verbose_name='Объем буферной памяти', null=True,
                                                   blank=True)
    connection = models.CharField(max_length=100, verbose_name='Подключение', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    drive_element_images = models.ImageField(upload_to='drive_element_images/', null=True, blank=True)

    def __str__(self):
        return self.drive_element_name





class SSD_drive_1_element(models.Model):
    middle_ssd_drive_1_conaction = models.ForeignKey(SSD_drive_1_category, related_name='middle_ssd_1_conaction',
                                                     on_delete=models.CASCADE)
    ssd_1_name = models.CharField(max_length=100)
    container = models.CharField(max_length=100, verbose_name='Емкость', null=True, blank=True)
    the_form_factor = models.PositiveSmallIntegerField(default=0, verbose_name='Форм-фактор', null=True, blank=True)
    m2_connector = models.BooleanField(default=False, verbose_name='Разъем M.2', null=True, blank=True)
    type_of_flash_memory = models.CharField(max_length=100, verbose_name='Тип флэш-памяти', null=True, blank=True)
    reading_speed = models.CharField(max_length=100, verbose_name='Скорость чтения', null=True, blank=True)
    recording_speed = models.CharField(max_length=100, verbose_name='Скорость записи', null=True, blank=True)
    max_interface_speed = models.CharField(max_length=100, verbose_name='Макс. скорость интерфейса', null=True,
                                           blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    images = models.ImageField(upload_to='SSD_1_element_images/', null=True, blank=True)

    def __str__(self):
        return self.ssd_1_name




class SSD_drive_2_element(models.Model):
    middle_ssd_drive_2_conaction = models.ForeignKey(SSD_drive_2_category, related_name='middle_ssd_2_conaction',
                                                     on_delete=models.CASCADE)
    ssd_2_element_name = models.CharField(max_length=100)
    container = models.CharField(max_length=100, verbose_name='Емкость', null=True, blank=True)
    the_form_factor = models.PositiveSmallIntegerField(default=0, verbose_name='Форм-фактор', null=True, blank=True)
    m2_connector = models.BooleanField(default=False, verbose_name='Разъем M.2', null=True, blank=True)
    type_of_flash_memory = models.CharField(max_length=100, verbose_name='Тип флэш-памяти', null=True, blank=True)
    reading_speed = models.CharField(max_length=100, verbose_name='Скорость чтения', null=True, blank=True)
    recording_speed = models.CharField(max_length=100, verbose_name='Скорость записи', null=True, blank=True)
    max_interface_speed = models.CharField(max_length=100, verbose_name='Макс. скорость интерфейса', null=True,
                                           blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    images = models.ImageField(upload_to='ssd_2_element_images/', null=True, blank=True)

    def __str__(self):
        return self.ssd_2_element_name




class DVD_drive_element(models.Model):
    middle_dvd_drive_conaction = models.ForeignKey(DVD_drive_category, related_name='middle_dvd_drive_conaction', on_delete=models.CASCADE)
    dvd_element_name = models.CharField(max_length=100)
    type_of_drive = models.CharField(max_length=100, verbose_name='Тип привода', null=True, blank=True)
    connection_interface = models.CharField(max_length=100, verbose_name='Интерфейс подключения', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    images = models.ImageField(upload_to='dvd_element_images', null=True, blank=True)

    def __str__(self):
        return self.dvd_element_name


class Headset_category(models.Model):
    the_headset_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.the_headset_name


class The_headset_element(models.Model):
    middle_the_headset_conaction = models.ForeignKey(Headset_category, related_name='middle_headset_conaction', on_delete=models.CASCADE)
    the_headset_element_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель', null=True, blank=True)
    type = models.CharField(max_length=100, verbose_name='Тип', null=True, blank=True)
    headphone_design = models.CharField(max_length=100, verbose_name='Конструкция наушников', null=True, blank=True)
    connection_type = models.CharField(max_length=100, verbose_name='Тип подключения', null=True, blank=True)
    type_of_acoustic_design = models.CharField(max_length=100, verbose_name='Тип акустического оформления', null=True, blank=True)
    mounting_type = models.CharField(max_length=100, verbose_name='Тип крепления', null=True, blank=True)
    cable_type = models.CharField(max_length=100, verbose_name='Тип кабеля', null=True, blank=True)
    folding_design = models.BooleanField(default=False, verbose_name='Складная конструкция', null=True, blank=True)
    connecting_the_cable = models.CharField(max_length=100, verbose_name='Подключение кабеля', null=True, blank=True)
    interface_connection_connector = models.CharField(max_length=100, verbose_name='Интерфейс/разъём подключения', null=True, blank=True)
    type_of_batteries = models.CharField(max_length=100, verbose_name='Тип элементов питания', null=True, blank=True)
    battery_life = models.CharField(max_length=100, verbose_name='Продолжительность работы от аккумуляторов', null=True, blank=True)
    type_of_wireless_connection = models.CharField(max_length=100, verbose_name='Тип беспроводной связи', null=True, blank=True)
    range_of_action = models.CharField(max_length=100, verbose_name='Радиус действия', null=True, blank=True)
    bluetooth_Version = models.CharField(max_length=100, verbose_name='Версия Bluetooth', null=True, blank=True)
    case_case_included = models.BooleanField(default=False, verbose_name='Чехол/футляр в комплекте', null=True, blank=True)
    volume_control = models.BooleanField(default=False, verbose_name='Регулятор громкости')
    colour = models.CharField(max_length=100, verbose_name='Цвет', null=True, blank=True)
    weight = models.CharField(max_length=100, verbose_name='Вес', null=True, blank=True)
    guarantee = models.CharField(max_length=100, verbose_name='Гарантия', null=True, blank=True)
    price = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='The_headset_element_images/')



    def __str__(self):
        return self.the_headset_element_name








class Body_category(models.Model):#Корпус serializer жазылды
    body_category_name = models.CharField(max_length=15,unique=True)

    def  __str__(self):
        return self.body_category_name


class Power_unit_category(models.Model):#Блок питания serizlizers жазылды
    power_unit_category_name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.power_unit_category_name


class Wi_Fi_category(models.Model): # wi fi serializers жазылды
    wi_fi_category_name = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.wi_fi_category_name

class Sound_card_category(models.Model): # Звуковая карта  serializers жазылды
    sound_category_name = models.CharField(max_length=25,  unique=True)

    def __str__(self):
        return self.sound_category_name



class Operating_system_category(models.Model):#Операционнвя система serializers жазылды
    operating_system_name = models.CharField(max_length=25,unique=True,verbose_name='Операционная система')

    def __str__(self):
        return self.operating_system_name


class Mouse_catergory(models.Model):# мышь serializer жазылды
    mouse_category_name = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.mouse_category_name


class  Keyboard_category(models.Model): # клавиатура serializer жазылды
    keyboard_category_name = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.keyboard_category_name


class Manitor_category(models.Model):
    manitor_category_name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.manitor_category_name


class Body_element(models.Model):#Корпус элемент serialzers жазылды
    form_factor = models.CharField(max_length=25)
    name_element_body = models.CharField(max_length=25)
    body_price = models.IntegerField(default=0)
    middle_body_conaction = models.ForeignKey(Body_category,on_delete=models.CASCADE,related_name='middle_body_conaction')
    type_size = models.CharField(max_length=25,verbose_name='Типопазмер',null=True,blank=True)
    length_video_card  =models.PositiveSmallIntegerField(default=0,verbose_name='Максимальная длинна видеокарты',null=True,blank=True)
    dimensions = models.CharField(max_length=25,verbose_name='Габариты(ШхВхГ)',null=True,blank=True)
    connectors_panel = models.CharField(max_length=100,verbose_name='Разъемы на лицевой панели',null=True,blank=True)
    liquid_cooling = models.BooleanField(default=False,verbose_name='возможность устоновить систему жидкостного охлождения',null=True,blank=True)
    processor_cooler = models.CharField(max_length=100,verbose_name='Максимальная высота процессорного кулера',null=True,blank=True)
    air_filter = models.BooleanField(default=False,verbose_name='Съемный воздушный фильтр',null=True,blank=True)
    body_element_image = models.FileField(upload_to='body_element_image',null=True,blank=True)
    body_img = models.ImageField(upload_to='body_img',null=True,blank=True)

    def __str__(self):
        return f'{self.name_element_body}'




class Power_unit_element(models.Model):#Блок питания serializers жазылды
    power_unit_element_name = models.CharField(max_length=50, unique=True)
    middle_power_unit_conaction = models.ForeignKey(Power_unit_category,on_delete=models.CASCADE,related_name='middle_power_unit_conaction',null=True,blank=True)
    power_unit_price = models.PositiveIntegerField(default=0,null=True,blank=True)
    power = models.IntegerField(default=0,verbose_name='Mощность',null=True,blank=True)
    standard_power = models.CharField(max_length=25,verbose_name='cтандарт',null=True,blank=True)
    power_img = models.ImageField(upload_to='power_img',null=True,blank=True)

    def __str__(self):
        return self.power_unit_element_name






class Wi_Fi_element(models.Model): # wi fi serializers жазылды
    wi_fi_element_name = models.CharField(max_length=25,unique=True)
    wi_fi_price = models.PositiveIntegerField(default=0,verbose_name='цена')
    wi_fi_middle_conaction = models.ForeignKey(Wi_Fi_category,related_name='wi_fi_middle_conaction',on_delete=models.CASCADE)
    wi_fi_type  =models.CharField(max_length=25,verbose_name='тип',null=True,blank=True)
    wi_fi_wireless_communication = models.CharField(max_length=25,verbose_name='Стандарт беспроводной связи',null=True,blank=True)
    wi_fi_number_antennas = models.IntegerField(choices=[(i ,str(i)) for i in range(5)],verbose_name='Стандарт беспроводной связи',null=True,blank=True)
    information_protection = models.CharField(max_length=25,verbose_name='Защита информации',null=True,blank=True)
    max_speed = models.CharField(max_length=25,verbose_name='Макс. скорость беспроводного соединения',null=True,blank=True)
    wi_fi_img = models.ImageField(upload_to='wi_fi_img',null=True,blank=True)


    def __str__(self):
        return self.wi_fi_element_name



class Sound_card_element(models.Model):# Звуковая карта serializers жазылды
    sound_name = models.CharField(max_length=25,unique=True)
    sound_middle_conaction = models.ForeignKey(Sound_card_category,related_name='sound_middle_conaction',on_delete=models.CASCADE,verbose_name='Производитель')
    sound_price = models.PositiveIntegerField(default=0,verbose_name='цена')
    sound_type = models.CharField(max_length=25,verbose_name='Тип',null=True,blank=True)
    sound_img = models.ImageField(upload_to='sound_img',null=True,blank=True)
    connection_type = models.CharField(max_length=25,verbose_name='Тип подключения',null=True,blank=True)
    multi_audio = models.BooleanField(default=True,verbose_name='Возможность вывода многоканального звука',null=True,blank=True)
    input_connectors = models.SmallIntegerField(default=1,verbose_name='Входных разъемов jack 3.5 мм',null=True,blank=True)
    microphone_inputs = models.SmallIntegerField(default=1,verbose_name='Микрофонных входов',null=True,blank=True)

    def __str__(self):
        return self.sound_name

class Headset_element(models.Model):
    middle_the_headset_conaction = models.ForeignKey(Headset_category, related_name='middle_the_headset_conaction', on_delete=models.CASCADE)
    the_headset_element_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100, verbose_name='Производитель', null=True, blank=True)
    type = models.CharField(max_length=100, verbose_name='Тип', null=True, blank=True)
    headphone_design = models.CharField(max_length=100, verbose_name='Конструкция наушников', null=True, blank=True)
    connection_type = models.CharField(max_length=100, verbose_name='Тип подключения', null=True, blank=True)
    type_of_acoustic_design = models.CharField(max_length=100, verbose_name='Тип акустического оформления', null=True, blank=True)
    mounting_type = models.CharField(max_length=100, verbose_name='Тип крепления', null=True, blank=True)
    cable_type = models.CharField(max_length=100, verbose_name='Тип кабеля', null=True, blank=True)
    folding_design = models.BooleanField(default=False, verbose_name='Складная конструкция', null=True, blank=True)
    connecting_the_cable = models.CharField(max_length=100, verbose_name='Подключение кабеля', null=True, blank=True)
    interface_connection_connector = models.CharField(max_length=100, verbose_name='Интерфейс/разъём подключения', null=True, blank=True)
    type_of_batteries = models.CharField(max_length=100, verbose_name='Тип элементов питания', null=True, blank=True)
    battery_life = models.CharField(max_length=100, verbose_name='Продолжительность работы от аккумуляторов', null=True, blank=True)
    type_of_wireless_connection = models.CharField(max_length=100, verbose_name='Тип беспроводной связи', null=True, blank=True)
    range_of_action = models.CharField(max_length=100, verbose_name='Радиус действия', null=True, blank=True)
    bluetooth_Version = models.CharField(max_length=100, verbose_name='Версия Bluetooth', null=True, blank=True)
    case_case_included = models.BooleanField(default=False, verbose_name='Чехол/футляр в комплекте', null=True, blank=True)
    volume_control = models.BooleanField(default=False, verbose_name='Регулятор громкости')
    colour = models.CharField(max_length=100, verbose_name='Цвет', null=True, blank=True)
    weight = models.CharField(max_length=100, verbose_name='Вес', null=True, blank=True)
    guarantee = models.CharField(max_length=100, verbose_name='Гарантия', null=True, blank=True)
    headset_price = models.PositiveIntegerField(verbose_name='цена')
    headset_img = models.ImageField(upload_to='headset_img/',null=True,blank=True)

    def __str__(self):
        return f'{self.the_headset_element_name}'

class Operating_system_element(models.Model):#Операционная система serializer  жазылды
    operating_element_name = models.CharField(max_length=25,unique=True)
    middle_operation_conaction = models.ForeignKey(Operating_system_category,related_name='middle_operation_conaction',on_delete=models.CASCADE)
    operating_img = models.ImageField(upload_to='operating_img',null=True,blank=True)
    operating_price = models.PositiveIntegerField(default=0,verbose_name='цена')

    def __str__(self):
        return self.operating_element_name





class Mouse_element(models.Model):# Мышь serializer жазылды
    mouse_element_name = models.CharField(max_length=25,unique=True)
    middle_mouse_conaction = models.ForeignKey(Mouse_catergory,on_delete=models.CASCADE,related_name='middle_mouse_conaction')
    mouse_type = models.CharField(max_length=25,verbose_name='тип',null=True,blank=True)
    mouse_price = models.PositiveIntegerField(default=0,verbose_name='цена')
    mouse_img = models.ImageField(upload_to='mouse_img',null=True,blank=True)
    connection_interface = models.CharField(max_length=25,null=True,blank=True)
    scroll_wheel = models.BooleanField(default=True,verbose_name='Колесо прокрутки',null=True,blank=True)
    number_keys = models.SmallIntegerField(default=1,verbose_name='Количество клавиш',null=True,blank=True)
    polling_frequency =  models.IntegerField(default=0,verbose_name='Частота опроса',null=True,blank=True)
    sensor_opt_resolution = models.IntegerField(default=0,verbose_name='Разрешение оптического сенсора',null=True,blank=True)
    weight  = models.CharField(max_length=10,verbose_name='Вес',null=True,blank=True)
    mouse_design = models.CharField(max_length=25,null=True,blank=True)
    sensor_resolution = models.CharField(max_length=25,verbose_name='Разрешение сенсора',null=True,blank=True)


    def __str__(self):
        return self.mouse_element_name


class Keyboard_element(models.Model):
    keyboard_element_name = models.CharField(max_length=25,unique=True)
    middle_keyboard_conaction = models.ForeignKey(Keyboard_category,on_delete=models.CASCADE,related_name='middle_keyboard_conaction',verbose_name='категория')
    keyboard_price = models.IntegerField(default=0)
    keyboard_img = models.ImageField(upload_to='keyboard_img',null=True,blank=True)
    connection_interface_keyboard = models.CharField(max_length=25,verbose_name='Интерфейс подключения',null=True,blank=True)
    digital_block = models.BooleanField(default=True,verbose_name='Цифровой блок',null=True,blank=True)
    number_keys = models.SmallIntegerField(default=0,verbose_name='Количество клавиш',null=True,blank=True)


    def __str__(self):
        return self.keyboard_element_name



class Manitor_element(models.Model):
    manitor_element_name = models.CharField(max_length=25,unique=True)
    manitor_price = models.IntegerField(default=0)
    manitor_img = models.ImageField(upload_to='manitor_img',null=True,blank=True)
    diagonal = models.CharField(max_length=25,verbose_name='Диагональ',null=True,blank=True)
    brightness = models.CharField(max_length=25,verbose_name='Яркость',null=True,blank=True)
    contrast_ratio = models.CharField(max_length=25,verbose_name='Контрастность',null=True,blank=True)
    response_time = models.CharField(max_length=25,verbose_name='Время отклика',null=True,blank=True)
    maximum_colors = models.CharField(max_length=25,verbose_name='Максимальное количество цветов',null=True,blank=True)
    update_frequency = models.IntegerField(default=0,verbose_name='Частота обновления',null=True,blank=True)
    height_adjustment = models.BooleanField(default=False,verbose_name='Регулировка по высоте',null=True,blank=True)
    middle_manitor_conaction = models.ForeignKey(Manitor_category,on_delete=models.CASCADE,related_name='middle_manitor_conaction')

    def __str__(self):
        return self.manitor_element_name


class CompChoices(models.Model):
    procecor = models.ForeignKey(Processor_category,on_delete=models.CASCADE,verbose_name='процессор',null=True,blank=True)
    cooling = models.ForeignKey(Cooling_category,on_delete=models.CASCADE,verbose_name='охлождения',null=True,blank=True)
    memory = models.ForeignKey(Random_access_memory_category,on_delete=models.CASCADE,verbose_name='оперативнная памят',null=True,blank=True)
    motherboard = models.ForeignKey(The_motherboard_category,on_delete=models.CASCADE,verbose_name='Материнская плата',null=True,blank=True)
    video_card = models.ForeignKey(Video_card_category,on_delete=models.CASCADE,verbose_name='видео карта',null=True,blank=True)
    hard_drive = models.ForeignKey(Hard_drive_category,on_delete=models.CASCADE,verbose_name='жесткий диск',null=True,blank=True)
    ssd_drive_1 = models.ForeignKey(SSD_drive_1_category,on_delete=models.CASCADE,verbose_name='SSD диск 1',null=True,blank=True)
    ssd_drive_2 = models.ForeignKey(SSD_drive_2_category,on_delete=models.CASCADE,verbose_name='SSD диск 2',null=True,blank=True)
    dvd_drive = models.ForeignKey(DVD_drive_category,on_delete=models.CASCADE,verbose_name='DVD привод',null=True,blank=True)
    body_category = models.ForeignKey(Body_category,on_delete=models.CASCADE,verbose_name='корпус',null=True,blank=True)
    power_unit = models.ForeignKey(Power_unit_category,on_delete=models.CASCADE,verbose_name='блок питания',null=True,blank=True)
    wi_fi = models.ForeignKey(Wi_Fi_category,on_delete=models.CASCADE,verbose_name='wi-fi',null=True,blank=True)
    sound_card = models.ForeignKey(Sound_card_category,on_delete=models.CASCADE,verbose_name='звуковая карта',null=True,blank=True)
    operating_system = models.ForeignKey(Operating_system_category,on_delete=models.CASCADE,verbose_name='Операционнвя система',null=True,blank=True)
    mouse = models.ForeignKey(Mouse_catergory,on_delete=models.CASCADE,verbose_name='мышь',null=True,blank=True)
    keyboard = models.ForeignKey(Keyboard_category,on_delete=models.CASCADE,verbose_name='клавиатура',null=True,blank=True)
    manitor = models.ForeignKey(Manitor_category,on_delete=models.CASCADE,verbose_name='манитор',null=True,blank=True)
    headset = models.ForeignKey(Headset_category,on_delete=models.CASCADE,verbose_name='гарнитура',null=True,blank=True)



class Showcomp(models.Model):
    procecor = models.ManyToManyField(Processor_category,verbose_name='процессор')
    cooling = models.ManyToManyField(Cooling_category,verbose_name='охлождения')
    memory = models.ManyToManyField(Random_access_memory_category,verbose_name='оперативнная памят')
    motherboard = models.ManyToManyField(The_motherboard_category,verbose_name='Материнская плата')
    video_card = models.ManyToManyField(Video_card_category,verbose_name='видео карта')
    hard_drive = models.ManyToManyField(Hard_drive_category,verbose_name='жесткий диск')
    ssd_drive_1 = models.ManyToManyField(SSD_drive_1_category,verbose_name='SSD диск 1')
    ssd_drive_2 = models.ManyToManyField(SSD_drive_2_category,verbose_name='SSD диск 2')
    dvd_drive = models.ManyToManyField(DVD_drive_category,verbose_name='DVD привод')
    body_category = models.ManyToManyField(Body_category,verbose_name='корпус')
    power_unit = models.ManyToManyField(Power_unit_category,verbose_name='блок питания')
    wi_fi = models.ManyToManyField(Wi_Fi_category,verbose_name='wi-fi')
    sound_card = models.ManyToManyField(Sound_card_category,verbose_name='звуковая карта')
    operating_system = models.ManyToManyField(Operating_system_category,verbose_name='Операционнвя система')
    mouse = models.ManyToManyField(Mouse_catergory,verbose_name='мышь')
    keyboard = models.ManyToManyField(Keyboard_category,verbose_name='клавиатура')
    manitor = models.ManyToManyField(Manitor_category,verbose_name='манитор')
    headset = models.ManyToManyField(Headset_category,verbose_name='гарнитура')


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, related_name='cart', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    main = models.ForeignKey(CompChoices, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)


    def get_total_price(self):
        return self.product.price * self.quantity
