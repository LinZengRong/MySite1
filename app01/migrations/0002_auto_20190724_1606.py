# Generated by Django 2.2.2 on 2019-07-24 08:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Looms',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Id_mac', models.CharField(max_length=4, unique=True)),
                ('Model', models.CharField(max_length=30)),
                ('Maker', models.CharField(max_length=20)),
                ('Type', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('Id_plan', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('P_date', models.CharField(max_length=30)),
                ('Id_mac', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app01.Looms')),
            ],
        ),
    ]