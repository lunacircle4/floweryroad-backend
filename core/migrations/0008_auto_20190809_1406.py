# Generated by Django 2.2.4 on 2019-08-09 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190809_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='description',
            field=models.TextField(),
        ),
    ]
