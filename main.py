from fastapi import FastAPI 
from models.SIRparameters import SIRParameters
from services.SIRService import SIRService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]
app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"], 
	allow_headers=["*"]
)

@app.post("/sir")
def get_sir(parameters: SIRParameters):
	sir_data = SIRService(parameters).calc_sir()
	return { "data": sir_data }
	