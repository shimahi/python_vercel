from ariadne import gql


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
