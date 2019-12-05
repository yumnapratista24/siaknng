from django.contrib import admin

from siaknngauth.account.models import Account

admin.site.register([
    Account,
])
