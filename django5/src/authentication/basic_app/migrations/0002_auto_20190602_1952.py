# Generated by Django 2.1.7 on 2019-06-02 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='protfolio_site',
            new_name='portfolio_site',
        ),
    ]
