from django.contrib import admin
from .models import PolicyProvider, FieldRule, Policy, Comment

admin.site.register(PolicyProvider)
admin.site.register(FieldRule)
admin.site.register(Policy)
admin.site.register(Comment)
