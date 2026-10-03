from django import forms
from .models import Customer
from.models import LoanApplication

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'




class LoanApplicationForm(forms.ModelForm):

    class Meta:
        model = LoanApplication

        exclude = [
            'user',
            'status',
            'applied_on'
        ]

        widgets = {
            'dob': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        employment_type = cleaned_data.get('employment_type')

        if employment_type == 'Salaried':

            required_fields = [
                'company_name',
                'job_designation',
                'work_experience',
                'monthly_income'
            ]

            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(
                        field,
                        'This field is required for salaried applicants.'
                    )

        elif employment_type == 'Self-employed':

            required_fields = [
                'business_name',
                'business_type',
                'business_experience',
                'annual_income'
            ]

            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(
                        field,
                        'This field is required for self-employed applicants.'
                    )

        return cleaned_data


