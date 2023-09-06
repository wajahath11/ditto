from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator


class PolicyProvider(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FieldRule(models.Model):
    provider = models.ForeignKey(PolicyProvider, on_delete=models.CASCADE)
    field_name = models.CharField(max_length=100)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.field_name} - Required: {self.is_required} - Provider: {self.provider.name}"


class Policy(models.Model):
    policy_provider = models.ForeignKey(PolicyProvider, on_delete=models.CASCADE)  # Required
    application_number = models.CharField(max_length=50, unique=True)  # Alphanumeric - Required
    customer_name = models.CharField(max_length=100)  # Max 100 Chars - Required
    email = models.EmailField()  # Valid Email - Required
    phone_number = models.CharField(max_length=15)  # Max 20 Chars - Required
    date_of_birth = models.DateField()  # Age should be 18-99 years
    policy_cover = models.BigIntegerField(
        validators=[
            MinValueValidator(2500000, message="Policy cover must be at least 25L"),
            MaxValueValidator(50000000, message="Policy cover cannot exceed 5cr"),
        ]
    )
    policy_status_choices = (
        ('Awaited', 'Requirements Awaited'),
        ('Closed', 'Requirements Closed'),
        ('Underwriting', 'Underwriting'),
        ('PolicyIssued', 'Policy Issued'),
        ('PolicyRejected', 'Policy Rejected'),
    )
    policy_status = models.CharField(max_length=20, choices=policy_status_choices)  # Choice Field
    policy_number = models.CharField(max_length=50, blank=True, null=True)  # Optional
    medical_type_choices = (
        ('TeleMedicals', 'Tele Medicals'),
        ('PhysicalMedicals', 'Physical Medicals'),
    )
    medical_type = models.CharField(max_length=20, choices=medical_type_choices, blank=True,
                                    null=True)  # Required only for MaxLife & HDFC Life
    medicals_status_choices = (
        ('Pending', 'Pending'),
        ('Scheduled', 'Scheduled'),
        ('WaitingForReport', 'Waiting for Report'),
        ('Done', 'Done'),
    )
    medicals_status = models.CharField(max_length=20,
                                       choices=medicals_status_choices, blank=True,
                                       null=True)  # Required only for MaxLife & HDFC Life

    remarks = models.TextField(
        validators=[MinLengthValidator(1), MaxLengthValidator(200)],
        blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Auto Generated - Read Only

    def __str__(self):
        return f"policy provider: {self.policy_provider.name} to {self.customer_name}"

    def trigger_email(self) -> None:
        """
        Trigger a confirmation email to whom the policy issued.
        :return:
        """
        subject: str = "Policy issued"
        message = (f"This is an confirmation email to let you know that {self.policy_provider.name} policy has been "
                   f"issued with policy number: {self.policy_number}")
        from_email = settings.EMAIL_HOST_USER  # Use the sender email address specified in EMAIL_HOST_USER
        recipient_list = [self.email]  # List of recipient email addresses
        send_mail(subject, message, from_email, recipient_list)


class Comment(models.Model):
    policy = models.ForeignKey(PolicyProvider, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.policy.name} : {self.comment}"
