# Generated by Django 2.2.4 on 2019-08-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_pedido_observacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoitem',
            name='atacado',
            field=models.BooleanField(default=False, verbose_name='atacado'),
        ),
    ]
