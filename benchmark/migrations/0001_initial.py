# Generated by Django 3.0.6 on 2020-06-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlueNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('tool_id', models.IntegerField()),
                ('detection', models.IntegerField()),
                ('capacite_d_analyse', models.IntegerField()),
                ('complexite_d_analyse', models.IntegerField()),
                ('export_des_resultats', models.IntegerField()),
                ('creation_de_regles', models.IntegerField()),
                ('export_de_fichier_suspect', models.IntegerField()),
                ('prevention', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlueWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('detection', models.IntegerField()),
                ('capacite_d_analyse', models.IntegerField()),
                ('complexite_d_analyse', models.IntegerField()),
                ('export_des_resultats', models.IntegerField()),
                ('creation_de_regles', models.IntegerField()),
                ('export_de_fichier_suspect', models.IntegerField()),
                ('prevention', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RedNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('tool_id', models.IntegerField()),
                ('mise_a_jour', models.IntegerField()),
                ('capacite_de_detection', models.IntegerField()),
                ('configuration', models.IntegerField()),
                ('rapidite_d_execution', models.IntegerField()),
                ('comsommation_de_ressources', models.IntegerField()),
                ('explication_de_vulnerabilite', models.IntegerField()),
                ('documentation', models.IntegerField()),
                ('scope_de_scan', models.IntegerField()),
                ('flexibilite', models.IntegerField()),
                ('communaute', models.IntegerField()),
                ('compatibilite_avec_outils_externes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RedWeight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('mise_a_jour', models.IntegerField()),
                ('capacite_de_detection', models.IntegerField()),
                ('configuration', models.IntegerField()),
                ('rapidite_d_execution', models.IntegerField()),
                ('comsommation_de_ressources', models.IntegerField()),
                ('explication_de_vulnerabilite', models.IntegerField()),
                ('documentation', models.IntegerField()),
                ('scope_de_scan', models.IntegerField()),
                ('flexibilite', models.IntegerField()),
                ('communaute', models.IntegerField()),
                ('compatibilite_avec_outils_externes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('team', models.CharField(max_length=30)),
            ],
        ),
    ]
