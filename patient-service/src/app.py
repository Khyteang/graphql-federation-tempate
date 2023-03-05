import uvicorn
import strawberry
import typing

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from strawberry.tools import merge_types
from src.patient.schema import Query as PatientQuery, Mutation as PatientMutation
from src.prescription.schema import Query as PrescriptionQuery, Mutation as PrescriptionMutation

queries = (PatientQuery, PrescriptionQuery)
mutations = (PatientMutation, PrescriptionMutation)

Query = merge_types("Query", queries)
Mutation = merge_types("Mutation", mutations)

schema = strawberry.federation.Schema(query=Query, mutation=Mutation, enable_federation_2=True)

graphql_app = GraphQLRouter(schema)

app = FastAPI()

# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema()))
app.include_router(graphql_app, prefix="/graphql")

def start():
  uvicorn.run(
    'src.app:app',
    host="localhost",
    port=8080,
    log_level="info",
    reload=True
  )