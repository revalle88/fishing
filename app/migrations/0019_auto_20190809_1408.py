# Generated by Django 2.1.11 on 2019-08-09 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190809_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.Review'),
        ),
    ]
