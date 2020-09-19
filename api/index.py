from ariadne.asgi import GraphQL
from ariadne import (QueryType, gql,
                     make_executable_schema)


type_defs = gql("""
type Query {
  hello(name: String = "いぬ"): String!
  goodbye: String!
  members: [Member!]!
}

type Member {
  name: String!
  part: String!
}

""")
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


# from ariadne import QueryType, gql, make_executable_schema
# from ariadne.asgi import GraphQL

# type_defs = gql("""
#     type Query {
#         hello: String!
#     }
# """)

# # Create type instance for Query type defined in our schema...
# query = QueryType()

# # ...and assign our resolver function to its "hello" field.


# @query.field("hello")
# def resolve_hello(_, info):
#     request = info.context["request"]
#     user_agent = request.headers.get("user-agent", "guest")
#     return "Hello, %s!" % user_agent


# schema = make_executable_schema(type_defs, query)
# app = GraphQL(schema, debug=True)
