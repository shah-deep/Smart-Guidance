# Generated by Django 3.0.6 on 2021-01-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_topic_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='key',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
