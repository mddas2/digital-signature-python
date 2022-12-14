# Generated by Django 4.1 on 2022-12-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('unsigned_file', models.FileField(null=True, upload_to='user/documents')),
                ('signed_file', models.FileField(null=True, upload_to='user/documents')),
            ],
        ),
    ]
