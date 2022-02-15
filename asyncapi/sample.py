from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

from asyncapi.spec.specification import (
    Contact,
    ExternalDocs, Info,
    License,
    Server,
    ServerVariable,
    Specification, Tag,
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

spec = Specification(
    info=Info(
        title="Sample API",
        version="0.0.1",
        description="A sample API for demonstration",
        terms_of_service="Don't be evil",
        contact=Contact(
            name="Ed Herbert",
            url="https://github.com/edherbs135/asyncapi-python",
            email="edherbs147@gmail.com",
        ),
        license=License(
            name="Apache 2.0",
            url="https://www.apache.org/licenses/LICENSE-2.0.html",
        ),
    ),
    servers={
        "SampleServer": Server(
            url="localhost.{SampleVar}.kafka",
            protocol="kafka",
            protocol_version="1.2.7",
            description="Example of a server",
            variables={
                "SampleVar": ServerVariable(
                    default="ABC",
                    description="A test",
                    enum=["ABC", "DEF"],
                    examples=["XYZ"],
                )
            }
        )
    },
    tags=[
        Tag(
            name='TestTag',
            description='A tag for testing'
        ),
        Tag(
            name='TestTagWithDocs',
            description='A tag for testing',
            external_docs=ExternalDocs(
                url='https://www.asyncapi.com',
                description='Find out more about AsyncAPI'
            )
        )
    ],
    external_docs=ExternalDocs(
        url='https://www.asyncapi.com',
        description='Find out more about AsyncAPI'
    )
)


@app.get("/")
def docs(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "spec": spec}
    )
