# Generated by Django 3.1.7 on 2021-03-06 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0024_auto_20210305_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestregistration',
            name='event_organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.createevent'),
        ),
    ]
