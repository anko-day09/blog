# Generated by Django 5.0.2 on 2024-02-18 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_image', models.ImageField(upload_to='post_content_images/')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.post')),
            ],
        ),
    ]
