# Generated by Django 2.2.1 on 2020-08-30 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_selfquestion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfquestion',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='survey.Question'),
        ),
    ]