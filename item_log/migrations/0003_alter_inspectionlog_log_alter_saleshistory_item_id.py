# Generated by Django 4.1.1 on 2022-10-03 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item_log', '0002_saleshistory_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionlog',
            name='log',
            field=models.TextField(help_text='Comment contents'),
        ),
        migrations.AlterField(
            model_name='saleshistory',
            name='item_id',
            field=models.ForeignKey(db_column='item_id', on_delete=django.db.models.deletion.CASCADE, to='item_log.item'),
        ),
    ]
