from dataclasses import dataclass, field
from typing import Dict, List, Optional

from asyncapi.spec.security import SecurityScheme

ASYNCAPI_VERSION = "2.3.0"
DEFAULT_CONTENT_TYPE = "application/schema+json"


@dataclass
class Components:
    messages: Dict[str, "Message"] = field(default_factory=dict)
    schemas: Dict[str, "Schema"] = field(default_factory=dict)


@dataclass
class Specification:
    asyncapi: str = field(default=ASYNCAPI_VERSION, init=False)
    info: "Info"
    default_content_type: str = DEFAULT_CONTENT_TYPE
    servers: Dict[str, "Server"] = field(default_factory=dict)
    channels: Dict[str, "Channel"] = field(default_factory=dict)
    components: Components = Components()
    tags: List['Tag'] = field(default_factory=list)
    external_docs: Optional['ExternalDocs'] = None


@dataclass
class Info:
    title: str
    version: str
    description: Optional[str] = None
    terms_of_service: Optional[str] = None
    contact: Optional["Contact"] = None
    license: Optional["License"] = None


@dataclass
class Contact:
    name: Optional[str] = None
    url: Optional[str] = None
    email: Optional[str] = None


@dataclass
class License:
    name: str
    url: Optional[str] = None


@dataclass
class ExternalDocs:
    url: str
    description: Optional[str] = None


@dataclass
class Tag:
    name: str
    description: Optional[str] = None
    external_docs: Optional['ExternalDocs'] = None


@dataclass
class Server:
    url: str
    protocol: str
    protocol_version: Optional[str] = None
    description: Optional[str] = None
    variables: Dict[str, "ServerVariable"] = field(default_factory=dict)
    security: SecurityScheme = None
    # bindings: 'Bindings' = None


@dataclass
class ServerVariable:
    default: Optional[str] = None
    description: Optional[str] = None
    enum: List[str] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)


@dataclass
class Channel:
    description: str
    servers: List[str] = field(default_factory=list)
    subscribe: str = None
    publish: str = None


@dataclass
class Message:
    description: str


@dataclass
class Schema:
    description: str
