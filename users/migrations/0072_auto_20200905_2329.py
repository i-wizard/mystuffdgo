# Generated by Django 2.2.1 on 2020-09-05 22:29

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0071_auto_20200905_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='uploads/default_img/team-5.png', upload_to=utilities.helper.Helper.user_upload_file_name),
        ),
    ]