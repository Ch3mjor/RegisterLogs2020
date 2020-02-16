# Generated by Django 2.0 on 2020-02-16 10:17

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_addr', models.GenericIPAddressField(null=True)),
                ('browser', models.CharField(max_length=50)),
                ('ctype', models.CharField(max_length=30)),
                ('query', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
        ),
    ]
