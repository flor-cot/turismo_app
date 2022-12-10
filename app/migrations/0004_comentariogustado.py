# Generated by Django 3.2.14 on 2022-12-07 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_auto_20221114_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioGustado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=False)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comentario')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
