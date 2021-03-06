# Generated by Django 3.0.4 on 2020-11-21 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20201121_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prime',
            name='justif',
            field=models.ImageField(blank=True, null=True, upload_to='justif'),
        ),
        migrations.AlterField(
            model_name='prime',
            name='state',
            field=models.CharField(choices=[('EN', 'En attent'), ('AC', 'Accepted'), ('RE', 'Rejected')], default='EN', max_length=10),
        ),
    ]
