

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_remove_client_screenshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='screenshot',
            field=models.TextField(blank=True, null=True),
        ),
    ]
