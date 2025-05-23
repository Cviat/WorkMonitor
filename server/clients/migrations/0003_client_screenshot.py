
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_is_connected_alter_client_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='screenshot',
            field=models.ImageField(blank=True, null=True, upload_to='screenshots/'),
        ),
    ]
