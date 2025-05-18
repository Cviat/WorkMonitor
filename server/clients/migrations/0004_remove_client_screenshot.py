

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_client_screenshot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='screenshot',
        ),
    ]
