# Generated by Django 5.1.6 on 2025-04-07 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0054_discount"),
    ]

    operations = [
        migrations.AddField(
            model_name="peermessage",
            name="encrypted_key",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="peermessage",
            name="read_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="peermessage",
            name="starred",
            field=models.BooleanField(default=False),
        ),
    ]
