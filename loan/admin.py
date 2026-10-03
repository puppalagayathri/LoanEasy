from django.contrib import admin
from .models import Customer, LoanApplication


admin.site.register(Customer)


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'full_name',
        'loan_type',
        'amount',
        'status',
        'applied_on',
    )

    list_filter = (
        'status',
        'loan_type',
        'employment_type',
    )

    search_fields = (
        'full_name',
        'email',
        'phone',
        'user__username',
    )
