# Generated by Django 4.2.6 on 2023-10-16 10:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0005_member_slug_alter_member_joined_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="joined_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 10, 16, 10, 20, 33, 254756, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="member",
            name="phone",
            field=models.IntegerField(),
        ),
    ]
