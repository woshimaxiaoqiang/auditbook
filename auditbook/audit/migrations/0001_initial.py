# Generated by Django 3.0.2 on 2020-01-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipname', models.CharField(max_length=50, verbose_name='设备名称')),
                ('equipno', models.CharField(max_length=50, verbose_name='设备编号')),
                ('equipmodel', models.CharField(max_length=50, verbose_name='设备型号')),
                ('equipfield', models.CharField(choices=[('化学', '化学'), ('机性', '机性'), ('金相', '金相'), ('计量器具', '计量器具'), ('其他设备', '其他设备')], max_length=20, verbose_name='所属专业')),
            ],
            options={
                'verbose_name_plural': '设备',
            },
        ),
        migrations.CreateModel(
            name='Personel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('position', models.CharField(max_length=20, verbose_name='职位')),
                ('profession', models.CharField(choices=[('实验室主任', '实验室主任'), ('质量负责人', '质量负责人'), ('技术负责人', '技术负责人'), ('QA人员', 'QA人员'), ('授权签字人', '授权签字人'), ('内审员', '内审员'), ('化学技术人员', '化学技术人员'), ('机性技术人员', '机性技术人员'), ('金相技术人员', '金相技术人员')], max_length=20, verbose_name='专业')),
            ],
            options={
                'verbose_name_plural': '人员',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tabno', models.CharField(max_length=20, verbose_name='记录编号')),
                ('tabname', models.CharField(max_length=30, verbose_name='记录名称')),
                ('tabtype', models.CharField(choices=[('质量记录', '质量记录'), ('技术记录', '技术记录'), ('内审记录', '内审记录'), ('NCR记录', 'NCR记录')], max_length=20, verbose_name='记录类型')),
                ('tabtime', models.DateField(verbose_name='记录时间')),
            ],
            options={
                'verbose_name_plural': '历年记录',
            },
        ),
        migrations.CreateModel(
            name='Stardands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdno', models.CharField(max_length=20, verbose_name='文件编号')),
                ('stdname', models.CharField(max_length=50, verbose_name='文件名称')),
                ('stdadd', models.FileField(default='', upload_to='../media/standard/', verbose_name='选择地址')),
                ('stdclass', models.CharField(choices=[('AC', 'AC'), ('CNAS/DILAC', 'CNAS/DILAC'), ('ASTM', 'ASTM'), ('GB', 'GB')], max_length=20, verbose_name='文件分类')),
            ],
            options={
                'verbose_name_plural': '准则/标准',
            },
        ),
        migrations.CreateModel(
            name='Zhiliangshouce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shouceno', models.CharField(max_length=20, verbose_name='文件编号')),
                ('shoucename', models.CharField(max_length=100, verbose_name='文件名称')),
                ('shouceauthor', models.CharField(choices=[], max_length=20, verbose_name='编制者')),
                ('shouceadd', models.FileField(default='', upload_to='../media/shouce/', verbose_name='选择地址')),
                ('fileclass', models.CharField(choices=[('质量手册', '质量手册'), ('程序文件', '程序文件'), ('三层次文件', '三层次文件'), ('技术管理规定', '技术管理规定')], max_length=20, verbose_name='文件分类')),
            ],
            options={
                'verbose_name_plural': '体系文件',
            },
        ),
    ]
