import strawberry
from strawberry.asgi import GraphQL

print ("Passo 2a")

from resolvers.hello.resolve_hello import *



@strawberry.type
class Query:
    hello_word = strawberry.field (resolve_hello_word)

schema = strawberry.Schema (query=Query())
graphql_app = GraphQL (schema, debug=True)