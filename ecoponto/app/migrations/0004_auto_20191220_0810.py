# Generated by Django 3.0.1 on 2019-12-20 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191220_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificado',
            name='empresas',
            field=models.ManyToManyField(related_name='certificados', to='app.Empresa'),
        ),
    ]
