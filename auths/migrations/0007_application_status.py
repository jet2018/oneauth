# Generated by Django 3.2.9 on 2021-11-21 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0006_auto_20211121_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('free', 'Freemium'), ('premium', 'Premium')], default='free', max_length=10),
        ),
    ]
