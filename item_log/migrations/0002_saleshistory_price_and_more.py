# Generated by Django 4.1.1 on 2022-10-02 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='saleshistory',
            name='price',
            field=models.IntegerField(default=0, verbose_name='상품가격'),
        ),
        migrations.AlterField(
            model_name='inspectionlog',
            name='inspection_date',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='item',
            name='production_date',
            field=models.DateField(verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='saleshistory',
            name='sales_date',
            field=models.DateField(verbose_name='판매일'),
        ),
    ]
