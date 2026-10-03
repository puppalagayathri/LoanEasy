from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=50)


def __str__(self):
    return self.full_name

class LoanApplication(models.Model):

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    ]

    LOAN_TYPE = [
        ('Personal', 'Personal'),
        ('Home', 'Home'),
        ('Education', 'Education'),
        ('Vehicle', 'Vehicle'),
        ('Business', 'Business')
    ]

    EMP_TYPE = [
        ('Salaried', 'Salaried'),
        ('Self-employed', 'Self-employed'),

    ]

    STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # ---------------- PERSONAL DETAILS ----------------

    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    # Complete Address
    house_no = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    # ---------------- EMPLOYMENT DETAILS ----------------

    employment_type = models.CharField(
        max_length=20,
        choices=EMP_TYPE
    )

    # Salaried
    company_name = models.CharField(
        max_length=100,
        blank=True
    )

    job_designation = models.CharField(
        max_length=100,
        blank=True
    )

    work_experience = models.CharField(
        max_length=50,
        blank=True
    )

    monthly_income = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Self-employed
    business_name = models.CharField(
        max_length=100,
        blank=True
    )

    business_type = models.CharField(
        max_length=100,
        blank=True
    )

    business_experience = models.CharField(
        max_length=50,
        blank=True
    )

    annual_income = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )

    # ---------------- LOAN DETAILS ----------------

    loan_type = models.CharField(
        max_length=20,
        choices=LOAN_TYPE
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    tenure_months = models.PositiveIntegerField()

    purpose = models.CharField(
        max_length=200
    )

    # ---------------- DOCUMENTS ----------------

    aadhaar_document = models.FileField(
        upload_to='documents/aadhaar/',
        blank=True,
        null=True
    )

    pan_document = models.FileField(
        upload_to='documents/pan/',
        blank=True,
        null=True
    )

    income_proof = models.FileField(
        upload_to='documents/income/',
        blank=True,
        null=True
    )

    bank_statement = models.FileField(
        upload_to='documents/bank/',
        blank=True,
        null=True
    )
    # ---------------- STATUS ----------------

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default='Pending'
    )

    applied_on = models.DateTimeField(
        auto_now_add=True
    )

    # ---------------- EMI ----------------

    def emi(self, rate=10):

        r = rate / 12 / 100
        n = self.tenure_months
        p = float(self.amount)

        return round(
            p * r * (1 + r) ** n /
            ((1 + r) ** n - 1),
            2
        )





