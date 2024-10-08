# Generated by Django 5.0 on 2024-09-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1234, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='chave_pix',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='conta_bancaria',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.TextField(null=True),
        ),
    ]
