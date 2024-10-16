from django.contrib import admin

from .models import *



class Processor_elemenInlines(admin.TabularInline):
    model = Processor_element
    extra = 0


class Processor_categoryAdmin(admin.ModelAdmin):
    inlines = [Processor_elemenInlines]


class Cooling_elementInlines(admin.TabularInline):
    model = Cooling_element
    extra = 0


class Cooling_categoryAdmin(admin.ModelAdmin):
    inlines = [Cooling_elementInlines]


class The_motherboard_elementInlines(admin.TabularInline):
    model = The_motherboard_element
    extra = 0


class The_motherboard_categoryAdmin(admin.ModelAdmin):
    inlines = [The_motherboard_elementInlines]


class Random_access_memory_elementInlines(admin.TabularInline):
    model = Random_access_memory_element
    extra = 0



class Random_access_memory_categoryAdmin(admin.ModelAdmin):
    inlines = [Random_access_memory_elementInlines]


class Video_card_elementInlines(admin.TabularInline):
    model = Video_card_element
    extra = 0


class Video_card_categoryAdmin(admin.ModelAdmin):
    inlines = [Video_card_elementInlines]


class Hard_drive_elementInlines(admin.TabularInline):
    model = Hard_drive_element
    extra = 0


class Hard_drive_categoryAdmin(admin.ModelAdmin):
    inlines = [Hard_drive_elementInlines]



class SSD_drive_1_elementInlines(admin.TabularInline):
    model = SSD_drive_1_element
    extra = 0


class SSD_drive_1_categoryAdmin(admin.ModelAdmin):
    inlines = [SSD_drive_1_elementInlines]



class SSD_drive_2_elementInlines(admin.TabularInline):
    model = SSD_drive_2_element
    extra = 0


class SSD_drive_2_categoryAdmin(admin.ModelAdmin):
    inlines = [SSD_drive_2_elementInlines]


class DVD_drive_elementInlines(admin.TabularInline):
    model = DVD_drive_element
    extra = 0


class DVD_drive_categoryAdmin(admin.ModelAdmin):
    inlines = [DVD_drive_elementInlines]


admin.site.register(Processor_category,Processor_categoryAdmin)
admin.site.register(Cooling_category,Cooling_categoryAdmin)
admin.site.register(Random_access_memory_category,Random_access_memory_categoryAdmin)
admin.site.register(The_motherboard_category,The_motherboard_categoryAdmin)
admin.site.register(Video_card_category,Video_card_categoryAdmin)
admin.site.register(Hard_drive_category,Hard_drive_categoryAdmin)
admin.site.register(SSD_drive_1_category,SSD_drive_1_categoryAdmin)
admin.site.register(SSD_drive_2_category,SSD_drive_2_categoryAdmin)
admin.site.register(DVD_drive_category,DVD_drive_categoryAdmin)



class Body_elementInlines(admin.TabularInline):
    model = Body_element
    extra = 0

class Body_categoryAdmin(admin.ModelAdmin):
    inlines = [Body_elementInlines]

class Power_unit_elementInlines(admin.TabularInline):
    model = Power_unit_element
    extra = 0

class Power_unit_categoryAdmin(admin.ModelAdmin):
    inlines = [Power_unit_elementInlines]

class Wi_Fi_elementInlines(admin.TabularInline):
    model = Wi_Fi_element
    extra = 0

class Wi_Fi_categoryAdmin(admin.ModelAdmin):
    inlines = [Wi_Fi_elementInlines]

class Sound_card_elementInlines(admin.TabularInline):
    model = Sound_card_element
    extra = 0

class Sound_card_categoryAdmin(admin.ModelAdmin):
    inlines = [Sound_card_elementInlines]

class Operating_system_elementInlines(admin.TabularInline):
    model = Operating_system_element
    extra = 0

class Operating_system_categoryAdmin(admin.ModelAdmin):
    inlines = [Operating_system_elementInlines]

class Mouse_elementInlines(admin.TabularInline):
    model = Mouse_element
    extra = 0

class Mouse_catergoryAdmin(admin.ModelAdmin):
    inlines = [Mouse_elementInlines]

class Keyboard_elementInlines(admin.TabularInline):
    model = Keyboard_element
    extra  = 0

class Keyboard_categoryAdmin(admin.ModelAdmin):
    inlines = [Keyboard_elementInlines]

class Manitor_elementInlines(admin.TabularInline):
    model = Manitor_element
    extra = 0

class Manitor_categoryAdmin(admin.ModelAdmin):
    inlines = [Manitor_elementInlines]

class Headset_elementInlines(admin.TabularInline):
    model = Headset_element
    extra = 0

class Headset_categoryAdmin(admin.ModelAdmin):
    inlines = [Headset_elementInlines]


admin.site.register(Body_category,Body_categoryAdmin)
admin.site.register(Power_unit_category,Power_unit_categoryAdmin)
admin.site.register(Wi_Fi_category,Wi_Fi_categoryAdmin)
admin.site.register(Sound_card_category,Sound_card_categoryAdmin)
admin.site.register(Operating_system_category,Operating_system_categoryAdmin)
admin.site.register(Mouse_catergory,Mouse_catergoryAdmin)
admin.site.register(Keyboard_category,Keyboard_categoryAdmin)
admin.site.register(Manitor_category,Manitor_categoryAdmin)
admin.site.register(Headset_category,Headset_categoryAdmin)
admin.site.register(Showcomp)
admin.site.register(CompChoices)
admin.site.register(Cart)
admin.site.register(CartItem)