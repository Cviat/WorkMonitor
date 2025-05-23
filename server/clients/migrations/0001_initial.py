

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100)),
                ('machine_name', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('last_active', models.DateTimeField()),
            ],
        ),
    ]
