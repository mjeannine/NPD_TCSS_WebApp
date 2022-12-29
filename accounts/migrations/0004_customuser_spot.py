# Generated by Django 4.0.4 on 2022-12-29 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_counting_collector'),
        ('accounts', '0003_customuser_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='spot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collector_spot', to='api.spots'),
        ),
    ]