# Generated by Django 2.2.1 on 2019-10-01 22:03

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_auto_20190924_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesetting',
            name='num_jackpot_winners',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='gamesetting',
            name='trial_start',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]