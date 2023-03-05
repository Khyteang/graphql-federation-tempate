import uvicorn
import strawberry
import typing

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types
from src.order.schema import Query, Mutation, Order, Patient

schema = strawberry.federation.Schema(
  query=Query, 
  types=[Patient, Order],
  mutation=Mutation, 
  enable_federation_2=True
)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema()))
app.include_router(graphql_app, prefix="/graphql")

def start():
  uvicorn.run(
    'src.app:app',
    host="localhost",
    port=8081,
    log_level="info",
    reload=True
  )