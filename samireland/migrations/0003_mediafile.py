# Generated by Django 2.0 on 2018-01-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('samireland', '0002_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('name', models.TextField(primary_key=True, serialize=False)),
                ('mediafile', models.FileField(upload_to='')),
            ],
        ),
    ]
