# Generated by Django 4.2.6 on 2024-05-21 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('kor_co_nm', models.TextField(null=True)),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField(null=True)),
                ('join_way', models.TextField(null=True)),
                ('mtrt_cnd', models.TextField(null=True)),
                ('spcl_cnd', models.TextField(null=True)),
                ('join_deny', models.IntegerField(null=True)),
                ('join_member', models.TextField(null=True)),
                ('etc_note', models.TextField(null=True)),
                ('max_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(max_length=6)),
                ('kor_co_nm', models.TextField(null=True)),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('fin_prdt_nm', models.TextField(null=True)),
                ('join_way', models.TextField(null=True)),
                ('mtrt_cnd', models.TextField(null=True)),
                ('spcl_cnd', models.TextField(null=True)),
                ('join_deny', models.IntegerField(null=True)),
                ('join_member', models.TextField(null=True)),
                ('etc_note', models.TextField(null=True)),
                ('max_limit', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavingOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('save_trm', models.IntegerField(null=True)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('saving', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finlife.saving')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(null=True)),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('save_trm', models.IntegerField(null=True)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('deposit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finlife.deposit')),
            ],
        ),
    ]
