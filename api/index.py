from ariadne.asgi import GraphQL
from ariadne import (QueryType, load_schema_from_path,
                     make_executable_schema)
from api._utils.member import member

type_defs = load_schema_from_path("api/_utils/typeDefs.graphql")
query = QueryType()


@query.field("hello")
def resolve_hello(*_, name: str):
    return f"Hello, {name}!!"


@query.field("goodbye")
def resolve_goodbye(*_):
    return "goodbye!"


@query.field("members")
def resolve_members(*_):
    return member


schema = make_executable_schema(type_defs, query)

app = GraphQL(schema, debug=True)
