# Generated by Django 3.0.3 on 2020-05-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200507_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(default='2000-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='doj',
            field=models.DateTimeField(null=True),
        ),
    ]
