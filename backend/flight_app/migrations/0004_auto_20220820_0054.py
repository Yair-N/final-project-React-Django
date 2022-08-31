# Generated by Django 3.2.14 on 2022-08-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight_app', '0003_alter_airport_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Country'},
        ),
        migrations.RenameField(
            model_name='airline_company',
            old_name='code',
            new_name='Code',
        ),
        migrations.AddField(
            model_name='airport',
            name='display_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
