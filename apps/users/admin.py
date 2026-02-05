# Django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

# Application Imports
from apps.users.models import User

# Third Party Imports
from allauth.account.admin import EmailAddressAdmin as AllauthEmailAddressAdmin
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken
from import_export.admin import ImportExportModelAdmin  # type: ignore[import]
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm  # type: ignore[import]
from unfold.admin import ModelAdmin  # type: ignore[import]
from unfold.contrib.import_export.forms import ExportForm, ImportForm  # type: ignore[import]

admin.site.unregister(Group)
admin.site.unregister(EmailAddress)

# Try to unregister first (allauth may or may not have registered depending on your setup)
for model in (SocialApp, SocialAccount, SocialToken):
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin, ImportExportModelAdmin): # type: ignore[misc]
    # Forms loaded from `unfold.forms`
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    import_form_class = ImportForm
    export_form_class = ExportForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(SocialApp)
class SocialAppAdmin(ModelAdmin):
    pass

@admin.register(SocialAccount)
class SocialAccountAdmin(ModelAdmin):
    pass

@admin.register(SocialToken)
class SocialTokenAdmin(ModelAdmin):
    pass

@admin.register(EmailAddress)
class EmailAddressAdmin(AllauthEmailAddressAdmin, ModelAdmin):
    pass