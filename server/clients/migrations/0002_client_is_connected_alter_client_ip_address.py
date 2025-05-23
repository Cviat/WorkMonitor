
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_connected',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]
