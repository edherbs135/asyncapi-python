from dataclasses import dataclass
from enum import Enum
from typing import Optional


# TODO: Finish implementing as per
#  https://www.asyncapi.com/docs/specifications/v2.3.0#securitySchemeObject

class SecurityType(Enum):
    USER_PASSWORD = "userPassword"
    API_KEY = "apiKey"
    X509 = "X509"
    SYMMETRIC_ENCRYPTION = "symmetricEncryption"
    ASYMMETRIC_ENCRYPTION = "asymmetricEncryption"
    HTTP_API_KEY = "httpApiKey"
    HTTP = "http"
    OAUTH2 = "oauth2"
    OPEN_ID_CONNECT = "openIdConnect"
    PLAIN = "plain"
    SCRAM_SHA_256 = "scramSha256"
    SCRAM_SHA_512 = "scramSha512"
    GSSAPI = "gssapi"


class KeyLocation(Enum):
    USER = 'user'
    PASSWORD = 'password'
    QUERY = 'query'
    HEADER = 'header'
    COOKIE = 'cookie'


@dataclass
class SecurityScheme:
    type: SecurityType
    description: Optional[str] = None


@dataclass(init=False)
class HttpApiKeyScheme(SecurityScheme):
    name: str

    def __init__(self, name: str, description: Optional[str] = None) -> None:
        super().__init__(SecurityType.HTTP_API_KEY, description)
        self.name = name
