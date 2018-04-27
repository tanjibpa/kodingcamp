# Generated by Django 2.0.4 on 2018-04-27 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day3', '0009_jobbasic'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('apply_instructions', models.TextField()),
                ('screening_details', models.TextField()),
                ('job_post_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='day3.JobBasic')),
            ],
        ),
    ]