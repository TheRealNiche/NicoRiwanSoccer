import soccersimulator 
from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIU
from . import tools
from .tools import Superstate
from . import utils

import module.tools as t
import math


class Action(object):
    def __init__(self, name="action"):
        self.name = name


class Move(Action):
    def __init__(self, name=None):
        if name is not None:
            super(Move, self).__init__(name)
        else:
            super(Move, self).__init__()


#gardien
	def cagecentre(self,positionjoueur,gardienpos):
		if (t.Superstate.id_team==1): 
			return soccersimulator.SoccerAction(acceleration = gardienpos - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = gardienpos - positionjoueur, shoot = None)
	def zoneaetre(self,positionjoueur,zoneaetre):
		if (t.Superstate.id_team==1): 
			return soccersimulator.SoccerAction(acceleration = zoneaetre - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = zoneaetre - positionjoueur, shoot = None)

#defenseur
	def godef(self,positionjoueur,defensepos):
		if (t.Superstate.id_team==1): 
			return soccersimulator.SoccerAction(acceleration = defensepos - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = defensepos - positionjoueur, shoot = None)

	def defgoball(self,positionjoueur,positionballe):
		vectball=positionballe-positionjoueur
		return soccersimulator.SoccerAction(acceleration = vectball, shoot = None)


	def turfjoueur(self,positionjoueur,opp,nearopp):
		assumer=opp-nearopp
		vectassumer=(assumer/2-positionjoueur)+nearopp
		return soccersimulator.SoccerAction(acceleration = vectassumer, shoot = None)

	def bbe(self,positionjoueur,ennemiprocheballe):
		vect=(ennemiprocheballe-positionjoueur)
		return soccersimulator.SoccerAction(acceleration = vect, shoot = None)

	def antipasse(self,ennemiprocheballe,positionballe):
		passeposs=(ennemiprochaballe-positionballe)/3
		return soccersimulator.SoccerAction(acceleration = passeposs, shoot = None)

		



#avantage

	def avantagezone(self,positionjoueur,zoneavantage):
		if (t.Superstate.id_team==1):
			return soccersimulator.SoccerAction(acceleration = zoneavantage - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = zoneavantage - positionjoueur, shoot = None)

	def avantagezone1(self,positionjoueur,zoneavantage1):
		if (t.Superstate.id_team==1):
			return soccersimulator.SoccerAction(acceleration = zoneavantage1 - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = zoneavantage1 - positionjoueur, shoot = None)


	def avantagezone2(self,positionjoueur,zoneavantage2):
		if (t.Superstate.id_team==1):
			return soccersimulator.SoccerAction(acceleration = zoneavantage2 - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = zoneavantage2 - positionjoueur, shoot = None)





#attaquantt
	def goatt(self,positionjoueur,attaquepos):
		if (t.Superstate.id_team==1): 
			return soccersimulator.SoccerAction(acceleration = attaquepos - positionjoueur, shoot = None)
		else:
			return soccersimulator.SoccerAction(acceleration = attaquepos - positionjoueur, shoot = None)



	def goballe(self,positionjoueur,positionballe):
		balle=positionballe
		joueur=positionjoueur
		return soccersimulator.SoccerAction(acceleration =balle-joueur,shoot = None)



class Shoot(Action):
	def __init__(self, name=None):
		if (name is not None) :
			super(Shoot, self).__init__(name)
		else:
			super(Shoot, self).__init__()




	##def shootgoal(self,positionjoueur,cageennemi):
    	#avvect=(turfu - positionjoueur)
    	#return soccersimulator.SoccerAction(acceleration=None,shoot=vect)

	def ballopied(self,positionjoueur,positionballe,cageennemi,strentgh):
		turfu=cageennemi
    	shoot=utils.compute_shoot(positionjoueur,turfu,strentgh)
    	return soccersimulator.SoccerAction(acceleration = None , shoot = shoot)


	def viser(self,positionjoueur, turfu, strentgh):
		tir = utils.compute_shoot(positionjoueur,turfu,strentgh)
        vect = (turfu - positionjoueur)
        vectnorm = vect.normalize() * strentgh
        return soccersimulator.SoccerAction(acceleration=None, shoot = vectnorm)



	def shootcotebas(self,basennemi):
		if (t.Superstate.id_team==1): 
			return soccersimulator.SoccerAction(acceleration = none, shoot = basennemi)
		else:
			return soccersimulator.SoccerAction(acceleration = none, shoot = basennemi)

	def shootcotehaut(self,hautennemi):
		if (t.Superstate.id_team==1): 
			return soccersimulator.SoccerAction(acceleration = none, shoot = hautennemi)
		else:
			return soccersimulator.SoccerAction(acceleration = none, shoot = hautennemi)


	def ballocentre(self,centre):
		return soccersimulator.SoccerAction(acceleration = none, shoot = centre)





	def p(self,positionjoueur,positionpote,strentgh):
		return self.viser(positionjoueur,positionpote,strentgh)

























































