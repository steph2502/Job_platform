# Generated by Django 5.1.1 on 2024-09-04 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_candidateprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
