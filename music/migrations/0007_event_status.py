# Generated by Django 5.1.1 on 2024-10-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_event_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Отменено', 'Отменено'), ('Прошло', 'Прошло'), ('Ожидается', 'Ожидается')], default='Ожидается', max_length=100),
        ),
    ]
