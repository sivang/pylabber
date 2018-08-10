# Generated by Django 2.1 on 2018-08-08 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('research', '0003_auto_20180808_1749'),
        ('questionnaires', '0003_auto_20180808_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questionnaires.Option')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questionnaires.Question')),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='questionnaires.Questionnaire')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='research.Subject')),
            ],
        ),
    ]