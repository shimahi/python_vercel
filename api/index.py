from ariadne.asgi import GraphQL
from ariadne import (QueryType, load_schema_from_path,
                     make_executable_schema)


type_defs = load_schema_from_path("typeDefs.graphql")
query = QueryType()


@query.field("hello")
def resolve_hello(*_, name):
    return f"Hello, {name}!!"


@query.field("goodbye")
def resolve_goodbye(*_):
    return "goodbye!"


@query.field("members")
def resolve_members(*_):
    return [
        {
            "name": "shimahi",
            "part": "guitar"
        },
        {
            "name": "mochi",
            "part": "vocal"
        }
    ]


schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)
