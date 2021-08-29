"""API handler."""
from fastapi import FastAPI, APIRouter
from titanic.api.provider.endpoints.titanic import titanic

# Combine all endpoints to the same FastAPI app instance
router = APIRouter()

# Add Titanic endpoint
router.include_router(
    titanic.router,
    prefix="/titanic",
    tags=["Titanic"],
)

# Create the FastAPI app
app = FastAPI(title="Titanic ML API")
app.include_router(router)
