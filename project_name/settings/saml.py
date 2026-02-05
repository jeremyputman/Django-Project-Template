# Django Imports
from decouple import config

# Application Imports
from apps.core.functions import get_secret_data

# SAML Settings
SAML_BASE_URL=config("SAML_BASE_URL", cast=str)
SAML_SYNC_GROUPS=config("SAML_SYNC_GROUPS", cast=bool)
SAML_SYNC_GROUPS_CLAIM=config("SAML_SYNC_GROUPS_CLAIM", cast=str)
SAML_SYNC_GROUPS_PREFIX=config("SAML_SYNC_GROUPS_PREFIX", cast=str)
if SAML_SYNC_GROUPS:
    SOCIALACCOUNT_ADAPTER = "core.auth.adapters.dJangoAllAuthSAMLAdapater"

# Django-Allauth Settings
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_ONLY = True
ACCOUNT_EMAIL_VERIFICATION = "none"
LOGOUT_REDIRECT_URL = '/logoff'

SOCIALACCOUNT_PROVIDERS = {
    "saml": {
        "APPS": [
            {
                "name": "SAML Login",
                "provider_id": config("SAML_PROVIDER_ID", cast=str),
                "client_id": config("SAML_CLIENT_ID", cast=str),
                "settings": {
                    "attribute_mapping": {
                        "username": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name",
                        "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
                        "groups": "http://schemas.microsoft.com/ws/2008/06/identity/claims/groups",
                    },
                    "use_nameid_for_email": False,
                    "idp": {
                        "entity_id": f"https://sts.windows.net/{config("SAML_TENANT_ID", cast=str)}/",
                        "sso_url": f"https://login.microsoftonline.com/{config("SAML_TENANT_ID", cast=str)}/saml2",
                        "slo_url": f"https://login.microsoftonline.com/{config("SAML_TENANT_ID", cast=str)}/saml2",
                        "x509cert": get_secret_data("SAML_CERTIFICATE"),
                    },
                    "sp": {
                    },
                    "advanced": {
                        "allow_repeat_attribute_name": True,
                        "allow_single_label_domains": False,
                        "authn_request_signed": False,
                        "digest_algorithm": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
                        "logout_request_signed": False,
                        "logout_response_signed": False,
                        "metadata_signed": False,
                        "name_id_encrypted": False,
                        "name_id_format": "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
                        "reject_deprecated_algorithm": True,
                        "reject_idp_initiated_sso": True,
                        "signature_algorithm": "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256",
                        "want_assertion_encrypted": False,
                        "want_assertion_signed": False,
                        "want_attribute_statement": True,
                        "want_message_signed": False,
                        "want_name_id": False,
                        "want_name_id_encrypted": False,
                    },
                },
            },
        ]
    }
}