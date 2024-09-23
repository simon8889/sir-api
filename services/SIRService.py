import numpy as np
from scipy.integrate import odeint 
from models.SIRparameters import SIRParameters

class SIRService():
	def __init__(self, parameters: SIRParameters):
		self.population = parameters.population
		self.initial_s = parameters.initial_s
		self.initial_i = parameters.initial_i
		self.initial_r = parameters.initial_r
		self.infection_rate = parameters.infection_rate
		self.recuperation_rate = parameters.recuperation_rate
		self.days = parameters.days
	
	def sir_model(self, y, t, beta, gamma):
		S, I, R = y
		dS_dt = -beta * S * I
		dI_dt = beta * S * I - gamma * I
		dR_dt = gamma * I
		return [dS_dt, dI_dt, dR_dt]
	
	def calc_sir(self):
		s_ratio = self.initial_s / self.population
		i_ratio = self.initial_i / self.population
		r_ratio = self.initial_r / self.population
		y0  = [s_ratio, i_ratio, r_ratio]
		t = np.linspace(0, self.days, self.days)
		solution = odeint(self.sir_model, y0, t, args=(self.infection_rate, self.recuperation_rate))
		return self.proccess_data(solution)
	
	def proccess_data(self, solution):
		data_list = []
		S, I, R = solution.T
		for i in range(len(S)):
			data_list.append({"S": round(S[i] * self.population),
					 		  "I": round(I[i] * self.population ),
							  "R": round(R[i] * self.population)})
		return data_list