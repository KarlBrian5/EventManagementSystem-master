# Generated by Django 3.1.6 on 2021-02-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_auto_20210216_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitedguests',
            name='county',
            field=models.CharField(choices=[('Kisumu', 'Kisumu'), ('Nairobi', 'Nairobi'), ('Mombasa', 'Mombasa'), ('Siaya', 'Siaya')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='invitedguests',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='', max_length=100),
        ),
        migrations.AddField(
            model_name='invitedguests',
            name='phonenumber',
            field=models.CharField(default=123456, max_length=100),
            preserve_default=False,
        ),
    ]
