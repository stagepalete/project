# Generated by Django 5.1.1 on 2024-10-09 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='parking',
            field=models.CharField(choices=[('Есть', 'Есть'), ('Нет', 'Нет')], default='Есть', max_length=100),
        ),
    ]