from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0002_remove_loanapplication_aadhaar_number_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [

        migrations.DeleteModel(
            name='LoanApplication',
        ),

        migrations.CreateModel(
            name='LoanApplication',
            fields=[

                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),

                # Personal details
                ('full_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('gender', models.CharField(
                    choices=[
                        ('Male', 'Male'),
                        ('Female', 'Female'),
                        ('Other', 'Other')
                    ],
                    max_length=10
                )),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),

                # Address
                ('house_no', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=10)),

                # Employment
                ('employment_type', models.CharField(
                    choices=[
                        ('Salaried', 'Salaried'),
                        ('Self-employed', 'Self-employed'),
                        ('Student', 'Student'),
                        ('Other', 'Other')
                    ],
                    max_length=20
                )),

                # Salaried
                ('company_name', models.CharField(
                    blank=True,
                    max_length=100
                )),
                ('job_designation', models.CharField(
                    blank=True,
                    max_length=100
                )),
                ('work_experience', models.CharField(
                    blank=True,
                    max_length=50
                )),
                ('monthly_income', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    max_digits=10,
                    null=True
                )),

                # Self-employed
                ('business_name', models.CharField(
                    blank=True,
                    max_length=100
                )),
                ('business_type', models.CharField(
                    blank=True,
                    max_length=100
                )),
                ('business_experience', models.CharField(
                    blank=True,
                    max_length=50
                )),
                ('annual_income', models.DecimalField(
                    blank=True,
                    decimal_places=2,
                    max_digits=12,
                    null=True
                )),

                # Loan
                ('loan_type', models.CharField(
                    choices=[
                        ('Personal', 'Personal'),
                        ('Home', 'Home'),
                        ('Education', 'Education'),
                        ('Vehicle', 'Vehicle'),
                        ('Business', 'Business')
                    ],
                    max_length=20
                )),
                ('amount', models.DecimalField(
                    decimal_places=2,
                    max_digits=12
                )),
                ('tenure_months', models.PositiveIntegerField()),
                ('purpose', models.CharField(max_length=200)),

                # Documents
                ('aadhaar_document', models.FileField(
                    upload_to='documents/aadhaar/'
                )),
                ('pan_document', models.FileField(
                    upload_to='documents/pan/'
                )),
                ('income_proof', models.FileField(
                    upload_to='documents/income/'
                )),
                ('bank_statement', models.FileField(
                    upload_to='documents/bank/'
                )),

                # Status
                ('status', models.CharField(
                    choices=[
                        ('Pending', 'Pending'),
                        ('Approved', 'Approved'),
                        ('Rejected', 'Rejected')
                    ],
                    default='Pending',
                    max_length=10
                )),
                ('applied_on', models.DateTimeField(
                    auto_now_add=True
                )),

                # User
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='auth.user'
                )),
            ],
        ),
    ]