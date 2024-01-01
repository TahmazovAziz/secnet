# Generated by Django 5.0 on 2023-12-24 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='users/%Y/%m/%d/')),
            ],
        ),
    ]
