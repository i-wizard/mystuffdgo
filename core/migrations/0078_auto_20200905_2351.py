# Generated by Django 2.2.1 on 2020-09-05 22:51

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0077_auto_20200905_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]