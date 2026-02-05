# Django Imports
from typing import cast

# Third party Imports
from azure.keyvault.secrets import SecretClient
from azure.identity import ManagedIdentityCredential
from decouple import config


def get_secret_data(secret_name):
    """
    Retrieve secret from Azure Key Vault or from environment variable based on settings.

    Args:
        secret_name (str): The name of the secret to retrieve.
    Returns:
        str: The value of the secret.
    """
    if config("KEYVAULT_ENABLED", default=False, cast=bool):
        keyVaultName = config("KEYVAULT_NAME")
        KVUri = f"https://{keyVaultName}.vault.azure.net"
        client = SecretClient(vault_url=KVUri, credential=ManagedIdentityCredential())
        secret_name_str = cast(str, config(f"KEYVAULT_{secret_name}", cast=str))
        retrieved_secret = client.get_secret(secret_name_str)
        return retrieved_secret.value
    else:
        return config(secret_name)
    
def get_client_ip(request):
    """
    Function to get the client IP address from the request object taking into consideration the forwarded header.
    Args:
        request: The HTTP request object.
    Returns:
        str: The client IP address.
    """
    if(request is not None):
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            # "X-Forwarded-For" can contain multiple IPs; client is first
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
    else:
        return None    
