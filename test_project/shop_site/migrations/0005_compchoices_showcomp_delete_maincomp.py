# Generated by Django 5.1.1 on 2024-10-12 08:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0004_alter_maincomp_body_category_alter_maincomp_cooling_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.body_category', verbose_name='корпус')),
                ('cooling', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.cooling_category', verbose_name='охлождения')),
                ('dvd_drive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.dvd_drive_category', verbose_name='DVD привод')),
                ('hard_drive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.hard_drive_category', verbose_name='жесткий диск')),
                ('headset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.headset_category', verbose_name='гарнитура')),
                ('keyboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.keyboard_category', verbose_name='клавиатура')),
                ('manitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.manitor_category', verbose_name='манитор')),
                ('memory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.random_access_memory_category', verbose_name='оперативнная памят')),
                ('motherboard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.the_motherboard_category', verbose_name='Материнская плата')),
                ('mouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.mouse_catergory', verbose_name='мышь')),
                ('operating_system', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.operating_system_category', verbose_name='Операционнвя система')),
                ('power_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.power_unit_category', verbose_name='блок питания')),
                ('procecor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.processor_category', verbose_name='процессор')),
                ('sound_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.sound_card_category', verbose_name='звуковая карта')),
                ('ssd_drive_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.ssd_drive_1_category', verbose_name='SSD диск 1')),
                ('ssd_drive_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.ssd_drive_2_category', verbose_name='SSD диск 2')),
                ('video_card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.video_card_category', verbose_name='видео карта')),
                ('wi_fi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.wi_fi_category', verbose_name='wi-fi')),
            ],
        ),
        migrations.CreateModel(
            name='Showcomp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_category', models.ManyToManyField(blank=True, null=True, to='shop_site.body_category', verbose_name='корпус')),
                ('cooling', models.ManyToManyField(blank=True, null=True, to='shop_site.cooling_category', verbose_name='охлождения')),
                ('dvd_drive', models.ManyToManyField(blank=True, null=True, to='shop_site.dvd_drive_category', verbose_name='DVD привод')),
                ('hard_drive', models.ManyToManyField(blank=True, null=True, to='shop_site.hard_drive_category', verbose_name='жесткий диск')),
                ('headset', models.ManyToManyField(blank=True, null=True, to='shop_site.headset_category', verbose_name='гарнитура')),
                ('keyboard', models.ManyToManyField(blank=True, null=True, to='shop_site.keyboard_category', verbose_name='клавиатура')),
                ('manitor', models.ManyToManyField(blank=True, null=True, to='shop_site.manitor_category', verbose_name='манитор')),
                ('memory', models.ManyToManyField(blank=True, null=True, to='shop_site.random_access_memory_category', verbose_name='оперативнная памят')),
                ('motherboard', models.ManyToManyField(blank=True, null=True, to='shop_site.the_motherboard_category', verbose_name='Материнская плата')),
                ('mouse', models.ManyToManyField(blank=True, null=True, to='shop_site.mouse_catergory', verbose_name='мышь')),
                ('operating_system', models.ManyToManyField(blank=True, null=True, to='shop_site.operating_system_category', verbose_name='Операционнвя система')),
                ('power_unit', models.ManyToManyField(blank=True, null=True, to='shop_site.power_unit_category', verbose_name='блок питания')),
                ('procecor', models.ManyToManyField(blank=True, null=True, to='shop_site.processor_category', verbose_name='процессор')),
                ('sound_card', models.ManyToManyField(blank=True, null=True, to='shop_site.sound_card_category', verbose_name='звуковая карта')),
                ('ssd_drive_1', models.ManyToManyField(blank=True, null=True, to='shop_site.ssd_drive_1_category', verbose_name='SSD диск 1')),
                ('ssd_drive_2', models.ManyToManyField(blank=True, null=True, to='shop_site.ssd_drive_2_category', verbose_name='SSD диск 2')),
                ('video_card', models.ManyToManyField(blank=True, null=True, to='shop_site.video_card_category', verbose_name='видео карта')),
                ('wi_fi', models.ManyToManyField(blank=True, null=True, to='shop_site.wi_fi_category', verbose_name='wi-fi')),
            ],
        ),
        migrations.DeleteModel(
            name='MainComp',
        ),
    ]
