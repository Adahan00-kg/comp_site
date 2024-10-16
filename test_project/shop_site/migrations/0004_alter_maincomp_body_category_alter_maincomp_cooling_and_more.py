# Generated by Django 5.1.1 on 2024-10-11 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0003_maincomp_adahan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maincomp',
            name='body_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.body_category', verbose_name='корпус'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='cooling',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.cooling_category', verbose_name='охлождения'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='dvd_drive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.dvd_drive_category', verbose_name='DVD привод'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='hard_drive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.hard_drive_category', verbose_name='жесткий диск'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='headset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.headset_category', verbose_name='гарнитура'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='keyboard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.keyboard_category', verbose_name='клавиатура'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='manitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.manitor_category', verbose_name='манитор'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='memory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.random_access_memory_category', verbose_name='оперативнная памят'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='motherboard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.the_motherboard_category', verbose_name='Материнская плата'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='mouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.mouse_catergory', verbose_name='мышь'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='operating_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.operating_system_category', verbose_name='Операционнвя система'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='power_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.power_unit_category', verbose_name='блок питания'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='procecor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.processor_category', verbose_name='процессор'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='sound_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.sound_card_category', verbose_name='звуковая карта'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='ssd_drive_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.ssd_drive_1_category', verbose_name='SSD диск 1'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='ssd_drive_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.ssd_drive_2_category', verbose_name='SSD диск 2'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='video_card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.video_card_category', verbose_name='видео карта'),
        ),
        migrations.AlterField(
            model_name='maincomp',
            name='wi_fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop_site.wi_fi_category', verbose_name='wi-fi'),
        ),
    ]
