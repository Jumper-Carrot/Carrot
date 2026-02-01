from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_userpreferences"),
    ]

    operations = [
        migrations.AddField(
            model_name="userpreferences",
            name="allow_custom_order",
            field=models.BooleanField(default=True),
        ),
    ]
