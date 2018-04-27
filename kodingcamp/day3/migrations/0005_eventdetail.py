# Generated by Django 2.0.4 on 2018-04-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('day3', '0004_eventbasic'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_for_all', models.BooleanField()),
                ('screening_process', models.TextField()),
                ('registration_process', models.TextField()),
                ('payment_process', models.TextField()),
                ('additional_fee', models.FloatField()),
                ('review', models.TextField()),
                ('screening_confirmation_mail', models.TextField()),
                ('registration_confirmation_mail', models.TextField()),
                ('payment_confirmation_mail', models.TextField()),
                ('event_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='day3.EventBasic')),
            ],
        ),
    ]