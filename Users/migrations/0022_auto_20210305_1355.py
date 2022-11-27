# Generated by Django 3.1.7 on 2021-03-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0021_auto_20210305_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createevent',
            name='guests',
        ),
        migrations.AddField(
            model_name='createevent',
            name='guests',
            field=models.ManyToManyField(to='Users.InvitedGuests'),
        ),
    ]