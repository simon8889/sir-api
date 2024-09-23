from pydantic import BaseModel

class SIRParameters(BaseModel):
	population: int
	initial_s: int
	initial_i: int
	initial_r: int
	infection_rate: float
	recuperation_rate: float
	days: int
	class Config:
		json_schema_extra = {
			"example": {
				"population": 1000,
				"initial_s": 999,
				"initial_i": 1,
				"initial_r": 0,
				"infection_rate": 0.3,
				"recuperation_rate": 0.1,
				"days": 160
			}
		}