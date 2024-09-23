# SIR Model API

This API allows you to calculate and simulate the SIR (Susceptible-Infected-Recovered) model for studying the spread of infectious diseases.

## Endpoints

### 1. Calculate SIR Model

- **URL**: `/sir`
- **Method**: `POST`
- **Description**: Calculates the number of individuals in each state (susceptible, infected, and recovered) over time.

#### Request Body

```json
{
	"population": 1000,
	"initial_s": 999,
	"initial_i": 1,
	"initial_r": 0,
	"infection_rate": 0.3,
	"recuperation_rate": 0.1,
	"days": 160
}
