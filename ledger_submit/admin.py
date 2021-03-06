from django.contrib import admin

from .models import Rule, Token


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'payee', 'note', 'new_note', 'new_payee', 'account'
    )


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['user', 'short_token']
