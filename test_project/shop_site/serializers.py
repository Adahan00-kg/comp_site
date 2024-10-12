from .models import *
from rest_framework import serializers


from rest_framework import serializers
from .models import *


class Processor_elementSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor_element
        fields = ['id', 'processor_element_name', 'price']


class Processor_elementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Processor_element
        fields = ['id', 'processor_element_name', 'soket',
                  'l3_cache_size', 'number_of_cores', 'processor_frequency',
                  'technical_process', 'the_core', 'maximum_frequency_with_turbo_boost',
                  'price', 'processor_image']

class Processor_categorySerializer(serializers.ModelSerializer):
    middle_processor_conaction = Processor_elementSerializer(read_only=True, many=True)

    class Meta:
        model = Processor_category
        fields = ['id','processor_category_name',  'middle_processor_conaction']


class Processor_categorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor_category
        fields = ['processor_category_name']


class Cooling_elementSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cooling_element
        fields = ['id', 'cooling_element_name', 'price']

class Cooling_elementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cooling_element
        fields = ['id', 'cooling_element_name',
                   'radiator_material', 'cooler_height', 'number_of_heat_pipes', 'rotation_speed',
                  'air_flow', 'noise_level', 'type_of_bearing', 'the_backlight', 'uptime', 'weight',
                  'water_block_material', 'price', 'cooling_image']


class Cooling_categorySerializer(serializers.ModelSerializer):
    middle_cooling_conaction = Cooling_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Cooling_category
        fields = ['id', 'cooling_category_name', 'middle_cooling_conaction']

class Cooling_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cooling_category
        fields = ['cooling_category_name']



class Random_access_memory_elementSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Random_access_memory_element
        fields = ['id', 'access_memory_element_name', 'price']

class Random_access_memory_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Random_access_memory_element
        fields = ['id', 'access_memory_element_name', 'memory_element_images',
                  'memory_type', 'the_form_factor', 'clock_frequency', 'bandwidth',
                  'supply_voltage', 'volume', 'radiator', 'xmp_support', 'price']



class Random_access_memory_categorySerializer(serializers.ModelSerializer):
    middle_memory_conaction = Random_access_memory_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Random_access_memory_category
        fields = ['id', 'access_memory_category_name', 'middle_memory_conaction']

class Random_access_memory_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Random_access_memory_category
        fields = ['access_memory_category_name']


class The_motherboard_elementSimpleSerializer(serializers. ModelSerializer):
    class Meta:
        model = The_motherboard_element
        fields = ['id', 'motherboard_element_name', 'price']

class The_motherboard_elementSerializer(serializers. ModelSerializer):
    class Meta:
        model = The_motherboard_element
        fields = ['id', 'motherboard_element_name', 'motherboard_element_images', 'the_form_factor', 'number_of_lots',
                  'chipset', 'sound', 'socket', 'slot_expansion', 'slot_type_m', 'price']


class The_motherboard_categorySerializer(serializers.ModelSerializer):
    middle_the_motherboard_conaction = The_motherboard_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = The_motherboard_category
        fields = ['id', 'motherboard_category_name', 'middle_the_motherboard_conaction']

class The_motherboard_categorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = The_motherboard_category
        fields = ['motherboard_category_name']



class Video_card_elementSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_card_element
        fields = ['id', 'card_element_name', 'price']


class Video_card_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_card_element
        fields = ['id', 'card_element_name', 'card_element_images', 'graphics_processor', 'recommended_power_supply_power_supply',
                  'technical_process', 'the_amount_of_video_memory', 'video_memory_bus_bit_rate', 'cuda_support', 'price',]

class Video_card_categorySerializer(serializers.ModelSerializer):
    middle_video_card_conaction = Video_card_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Video_card_category
        fields = ['id', 'video_card_category_name', 'middle_video_card_conaction']

class Video_card_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video_card_category
        fields = ['video_card_category_name']



class Hard_drive_elementSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hard_drive_element
        fields = ['id', 'drive_element_name', 'price']

class Hard_drive_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hard_drive_element
        fields = ['id', 'drive_element_name', 'drive_element_images', 'volume', 'type', 'recording_speed_reading_speed',
                  'the_amount_of_buffer_memory', 'connection', 'price']

class Hard_drive_categorySerializer(serializers.ModelSerializer):
    middle_hard_drive_conaction = Hard_drive_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = Hard_drive_category
        fields = ['id', 'drive_category_name', 'middle_hard_drive_conaction']

class Hard_drive_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hard_drive_category
        fields = ['drive_category_name']


class SSD_drive_1_elementSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SSD_drive_1_element
        fields = ['id', 'ssd_1_name', 'price']


class SSD_drive_1_elementSerializer(serializers.ModelSerializer):

    class Meta:
        model = SSD_drive_1_element
        fields = ['id', 'ssd_1_name', 'images', 'container', 'the_form_factor', 'm2_connector',
                  'type_of_flash_memory', 'reading_speed', 'recording_speed', 'max_interface_speed', 'price']


class SSD_drive_1_categorySerializer(serializers.ModelSerializer):
    middle_ssd_1_conaction = SSD_drive_1_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = SSD_drive_1_category
        fields = ['id', 'ssd_drive_1_category_name', 'middle_ssd_1_conaction']

class SSD_drive_1_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SSD_drive_1_category
        fields = ['ssd_drive_1_category_name']




class SSD_drive_2_elementSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD_drive_2_element
        fields = ['id', 'ssd_2_element_name', 'price']



class SSD_drive_2_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = SSD_drive_2_element
        fields = ['id', 'ssd_2_element_name', 'images', 'container', 'the_form_factor',
                  'm2_connector',
                  'type_of_flash_memory', 'reading_speed', 'recording_speed', 'max_interface_speed', 'price']


class SSD_drive_2_categorySerializer(serializers.ModelSerializer):
    middle_ssd_2_conaction = SSD_drive_2_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = SSD_drive_2_category
        fields = ['id', 'ssd_drive_2_category_name', 'middle_ssd_2_conaction']

class SSD_drive_2_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = SSD_drive_2_category
        fields = ['ssd_drive_2_category_name']



class DVD_drive_elementSimpleSerializer(serializers. ModelSerializer):
    class Meta:
        model = DVD_drive_element
        fields = ['id', 'dvd_element_name', 'price']

class DVD_drive_elementSerializer(serializers. ModelSerializer):
    class Meta:
        model = DVD_drive_element
        fields = ['id', 'dvd_element_name', 'images', 'type_of_drive', 'connection_interface',
                  'price']


class DVD_drive_categorySerializer(serializers.ModelSerializer):
    middle_dvd_drive_conaction = DVD_drive_elementSimpleSerializer(read_only=True, many=True)

    class Meta:
        model = DVD_drive_category
        fields = ['id', 'dvd_drive_category_name', 'middle_dvd_drive_conaction']


class DVD_drive_categorySimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = DVD_drive_category
        fields = ['dvd_drive_category_name']


class Body_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Body_element
        fields = ['name_element_body','body_price']

class Body_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Body_element
        fields = ['id','name_element_body',
                  'middle_body_conaction','form_factor','length_video_card',
                  'dimensions','connectors_panel','liquid_cooling',
                  'processor_cooler','air_filter','body_element_image',
                  'body_img']


class Body_categorySerializer(serializers.ModelSerializer):
    middle_body_conaction = Body_elementSerializerList(read_only=True,many=True)
    class Meta:
        model = Body_category
        fields = ['body_category_name','middle_body_conaction']


class Body_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Body_category
        fields = ['body_category_name']


class Power_unit_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Power_unit_element
        fields = ['power_unit_element_name','power_unit_price']


class Power_unit_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power_unit_element
        fields = ['power_unit_element_name','middle_power_unit_conaction'
            ,'power','standard_power','power_img']


class Power_unit_categorySerializer(serializers.ModelSerializer):
    middle_power_unit_conaction = Power_unit_elementSerializerList(read_only=True,many=True)
    class Meta:
        model = Power_unit_category
        fields = ['power_unit_category_name','middle_power_unit_conaction']


class Power_unit_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Power_unit_category
        fields = ['power_unit_category_name']


class Wi_Fi_elementerSerializersList(serializers.ModelSerializer):
    class Meta:
        model = Wi_Fi_element
        fields = ['wi_fi_element_name','wi_fi_price']


class  Wi_Fi_elementerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Wi_Fi_element
        fields = ['wi_fi_element_name','wi_fi_middle_conaction',
                  'wi_fi_type','wi_fi_wireless_communication',
                  'wi_fi_number_antennas','information_protection','max_speed','wi_fi_img']


class Wi_Fi_categorySerializer(serializers.ModelSerializer):
    wi_fi_middle_conaction = Wi_Fi_elementerSerializers(read_only=True,many=True)
    class Meta:
        model = Wi_Fi_category
        fields = ['wi_fi_category_name','wi_fi_middle_conaction']


class Wi_Fi_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Wi_Fi_category
        fields = ['wi_fi_category_name']


class Sound_card_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Sound_card_element
        fields = ['sound_name','sound_price']

class Sound_card_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound_card_element
        fields = ['sound_name','sound_middle_conaction',
                  'sound_type','sound_img','connection_type',
                  'multi_audio','input_connectors','microphone_inputs']

class Sound_card_categorySerializer(serializers.ModelSerializer):
    sound_middle_conaction = Sound_card_elementSerializer(read_only=True,many=True)
    class Meta:
        model = Sound_card_category
        fields = ['sound_category_name','sound_middle_conaction']


class Sound_card_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Sound_card_categorySerializer
        fields = ['sound_category_name']


class Operating_system_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Operating_system_element
        fields = ['operating_element_name','operating_price']


class Operating_system_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operating_system_element
        fields = ['operating_element_name','middle_operation_conaction',
                  'operating_img']


class Operating_system_categorySerializer(serializers.ModelSerializer):
    middle_operation_conaction = Operating_system_elementSerializer(read_only=True,many=True)
    class Meta:
        model = Operating_system_category
        fields = ['operating_system_name','middle_operation_conaction']


class Operating_system_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Operating_system_category
        fields = ['operating_system_name']


class Mouse_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Mouse_element
        fields = ['mouse_element_name','mouse_price']


class Mouse_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse_element
        fields = ['mouse_element_name','middle_mouse_conaction',
                  'mouse_type','mouse_price','mouse_img',
                  'connection_interface','scroll_wheel','number_keys',
                  'polling_frequency','sensor_opt_resolution',
                  'weight','mouse_design','sensor_resolution']


class Mouse_catergorySerializer(serializers.ModelSerializer):
    middle_mouse_conaction = Mouse_elementSerializer(read_only=True,many=True)
    class Meta:
        model = Mouse_catergory
        fields = ['mouse_category_name','middle_mouse_conaction']


class Mouse_catergorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Mouse_catergory
        fields = ['mouse_category_name']


class Keyboard_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Keyboard_element
        fields = ['keyboard_element_name','keyboard_price']


class Keyboard_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard_element
        fields = ['keyboard_element_name','middle_keyboard_conaction',
                  'keyboard_price','keyboard_img',
                  'connection_interface_keyboard','digital_block','number_keys']


class Keyboard_categorySerializer(serializers.ModelSerializer):
    middle_keyboard_conaction = Keyboard_elementSerializer(read_only=True,many=True)
    class Meta:
        model = Keyboard_category
        fields = ['keyboard_category_name','middle_keyboard_conaction']


class Keyboard_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Keyboard_category
        fields = ['keyboard_category_name']


class Manitor_elementSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Manitor_element
        fields = ['manitor_element_name','manitor_price']


class Manitor_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manitor_element
        fields = ['manitor_element_name','manitor_img',
                  'diagonal','brightness','contrast_ratio','response_time',
                  'maximum_colors','update_frequency',
                  'height_adjustment','middle_manitor_conaction']


class Manitor_categorySerializer(serializers.ModelSerializer):
    middle_manitor_conaction = Manitor_elementSerializer(read_only=True,many=True)
    class Meta:
        model = Manitor_category
        fields = ['manitor_category','middle_manitor_conaction']


class Manitor_categoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manitor_category
        fields = ['manitor_category_name']

class Headset_elemenListtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headset_element
        fields = ['the_headset_element_name','headset_price']


class Headset_elementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Headset_element
        fields = ['the_headset_element_name','manufacturer',
                  'type','headphone_design','connection_type',
                  'type_of_acoustic_design','mounting_type',
                  'cable_type','folding_design',
                  'connecting_the_cable',
                  'interface_connection_connector',
                  'type_of_batteries','battery_life',
                  'type_of_wireless_connection','range_of_action',
                  'bluetooth_Version','case_case_included',
                  'volume_control','colour','weight','guarantee']



class Headset_categorySerializer(serializers.ModelSerializer):
    middle_the_headset_conaction = Headset_elemenListtSerializer(read_only=True,many=True)
    class Meta:
        model = Headset_category
        fields = ['the_headset_name','price']

class Headset_categorySerializerList(serializers.ModelSerializer):
    class Meta:
        model = Headset_category
        fields = ['the_headset_name']



class MainCompSerializer(serializers.ModelSerializer):
    procecor = Processor_categorySerializer(many=True)
    cooling = Cooling_categorySimpleSerializer(many=True)
    memory = Random_access_memory_categorySimpleSerializer(many=True)
    motherboard = The_motherboard_categorySimpleSerializer(many=True)
    video_card = Video_card_categorySimpleSerializer(many=True)
    hard_drive = Hard_drive_categorySimpleSerializer(many=True)
    ssd_drive_1 = SSD_drive_1_categorySimpleSerializer(many=True)
    ssd_drive_2 = SSD_drive_2_categorySimpleSerializer(many=True)
    dvd_drive = DVD_drive_categorySimpleSerializer(many=True)
    body_category = Body_categorySerializerList(many=True)
    power_unit = Power_unit_categorySerializerList(many=True)
    wi_fi = Wi_Fi_categorySerializerList(many=True)
    sound_card = Sound_card_categorySerializerList(many=True)
    operating_system = Operating_system_categorySerializerList(many=True)
    mouse = Mouse_catergorySerializerList(many=True)
    keyboard = Keyboard_categorySerializerList(many=True)
    manitor = Manitor_categoryListSerializer(many=True)
    headset = Headset_categorySerializerList(many=True)

    class Meta:
        model = Showcomp
        fields = '__all__'


class CompChoicesSerializer(serializers.ModelSerializer):
    procecor = Processor_categorySimpleSerializer(many=True)
    cooling = Cooling_categorySimpleSerializer(many=True)
    memory = Random_access_memory_categorySimpleSerializer(many=True)
    motherboard = The_motherboard_categorySimpleSerializer(many=True)
    video_card = Video_card_categorySimpleSerializer(many=True)
    hard_drive = Hard_drive_categorySimpleSerializer(many=True)
    ssd_drive_1 = SSD_drive_1_categorySimpleSerializer(many=True)
    ssd_drive_2 = SSD_drive_2_categorySimpleSerializer(many=True)
    dvd_drive = DVD_drive_categorySimpleSerializer(many=True)
    body_category = Body_categorySerializerList(many=True)
    power_unit = Power_unit_categorySerializerList(many=True)
    wi_fi = Wi_Fi_categorySerializerList(many=True)
    sound_card = Sound_card_categorySerializerList(many=True)
    operating_system = Operating_system_categorySerializerList(many=True)
    mouse = Mouse_catergorySerializerList(many=True)
    keyboard = Keyboard_categorySerializerList(many=True)
    manitor = Manitor_categoryListSerializer(many=True)
    headset = Headset_categorySerializerList(many=True)

    class Meta:
        model = CompChoices
        fields = '__all__'


