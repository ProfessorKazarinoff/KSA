# Generated by Django 3.0.3 on 2020-07-17 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ksas", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job", old_name="description", new_name="title",
        ),
    ]
