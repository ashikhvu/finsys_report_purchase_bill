# Generated by Django 4.2.11 on 2024-05-05 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vendor', '0007_alter_purchaseorder_po_number_historicalperformace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
