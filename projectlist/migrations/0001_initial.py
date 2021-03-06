# Generated by Django 2.1.2 on 2018-10-22 20:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('project_title', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('descrption', models.TextField()),
                ('current_stage', models.CharField(max_length=200)),
                ('plan_board', models.URLField()),
                ('repo', models.URLField()),
            ],
        ),
    ]
