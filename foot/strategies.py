from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from foot.actions import Action, Move, Shoot
from foot.tools import Superstate
from soccersimulator.settings import maxPlayerAcceleration, maxPlayerShoot, PLAYER_RADIUS, BALL_RADIUS



class strategy1v1(Strategy):
	def __init__(self):
		Strategy.__init__(self, "Attaquant")
    


	def compute_strategy(self, state, id_team, id_player):
		t=Superstate(state,id_team,id_player)
    	move=Move(t)
    	shoot=Shoot(t)
    	#balle
    	positionballe=s.positionballe
    	turfu=s.balleturfu
    	#joueur
    	cageennemi=s.cageennemi
    	positionjoueur=s.positionjoueur
    	vitesse=s.vitessejoueur
    	distance=s.ballejoueur
    	#ennemi
    	ennemiepos=s.ennemipos
    	ennemiprocheballe=s.ennemiprocheballe
    	#terrrain
    	z1=s.defensepos
    	cageennemi=s.cageennemi
    	cornerb=s.basennemi
    	cornerh=s.hautennemi
    	#divers
    	strentgh=6


    	if (s.id_team==1):
    		#unpeu moins de la moitie terrain
    		if (balleturfu.x>= GAME_WIDTH/2-10):
    			#si joueur plus proche que adv gogo
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				return m+s
    			#sinon il se place entre lui et la balle et shoot dans langle oppose a ladv	
    			else:
    				m=move.bbe(positionjoueur,ennemiprocheballe)
    				if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    					s=shoot.shootcotehaut(cornerh)
    				else:
    					s=shoot.shootcotebas(cornerb)
    				return m+s

    		else:
    			#sinon il se rreplace en zone 1 et att la balle jusquau moment ou on sera plus porche
    			m=move.godef(positionjoueur,z1)
    			if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    					s=shoot.shootcotehaut(cornerh)
    			else:
    					s=shoot.shootcotebas(cornerb)
    			return m+s	
    	else:
    		#il part sur la balle et tire vers la cage adverrse ou bien il degage le plus loin possible de l'adversaire
    		if (balleturfu.x>= GAME_WIDTH/2+10):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				return m+s
    			else:
    				#
    				m=move.bbe(positionjoueur,ennemiprocheballe)
    				if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    					s=shoot.shootcotehaut(cornerh)
    				else:
    					s=shoot.shootcotebas(cornerb)
    				return m+s

    		else:
    			m=move.godef(positionjoueur,z1)
    			if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    					s=shoot.shootcotehaut(cornerh)
    			else:
    					s=shoot.shootcotebas(cornerb)
    			return m+s





class att2vs2(Strategy):
	def __init__(self):
		Strategy.__init__(self, "Attaquant")



		def compute_strategy(self, state, id_team, id_player):
			t=Superstate(state,id_team,id_player)
    		move=Move(t)
    		shoot=Shoot(t)
    		#balle
    		positionballe=s.positionballe
    		turfu=s.balleturfu
    		#joueur
    		cageennemi=s.cageennemi
    		positionjoueur=s.positionjoueur
	    	vitesse=s.vitessejoueur
	    	distance=s.ballejoueur
	    	#equipier
	    	poteproche=s.poteproche
	    	#action
	    	pd=s.passepossible
	    	sp=s.shootpossible
	    	#ennemi
	    	ennemiepos=s.ennemipos
	    	ennemiprocheballe=s.ennemiprocheballe
	    	#terrrain
	    	z1=s.defensepos
	    	cageennemi=s.cageennemi
	    	cornerb=s.basennemi
	    	cornerh=s.hautennemi
	    	za1=s.avantagee1
	    	#divers
	    	strentgh=6



	    	if (s.id_team==1):
	    		#si avantage 
	    		if (s.avantage==false):
	    			#si joueur plus proche balle enemie va vers la ball et kick vers goal
	    			if(distance<ennemiprocheballe):
	    				m=move.defgoball(positionjoueur,turfu,vitesse)
	    				s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
	    				return m+s
	    				#sinon se rerplace entre adv et soit fait une passe si quelqu'un est devant ou bien se met a distance futur possible shoot

	    			else:
	    				m=move.bbe(positionjoueur,ennemiprocheballe)
	    				if(sp==true):
	    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
	    				else:
	    					if (pd==true):
	    						s=shoot.passe(positionjoueur,poteproche,strentgh)
	    					else:
	    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
	    							s=shoot.shootcotehaut(cornerh)
	    						else:
	    							s=shoot.shootcotebas(cornerb)

	    				return m+s

	    		else:
	    			#si avantage present alors le joueur va uniquement vers la balle lorsqu'il estt plus proche de la balle que les joueurs adverses, s'il peut fairer la passe il l'a fait sinon il la degage dans un corner et ainsi de suite , et dans le cas ou il nestt pas proch e de la balle il se met en position de defense
	    			if(distance<ennemiprocheballe):
	    				m=move.defgoball(positionjoueur,turfu,vitesse)
	    				if(sp==true):
	    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
	    				else:
	    					if (pd==true):
	    						s=shoot.passe(positionjoueur,poteproche,strentgh)
	    					else:
	    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
	    							s=shoot.shootcotehaut(cornerh)
	    						else:
	    							s=shoot.shootcotebas(cornerb)
	    				return m+s
	    			else:
	    				m=move.avantagezone(positionjoueur,za1)
	    				if (pd==true):
	    					s=shoot.passe(positionjoueur,poteproche,strentgh)
	    				else:
	    					if(ennemiprocheballe.y<=GAME_HEIGHT/2):
	    						s=shoot.shootcotehaut(cornerh)
	    					else:
	    						s=shoot.shootcotebas(cornerb)

	    			return m+s	
	    			
	    	else:
	    		if (s.avantage==false):
	    			#si joueur plus proche balle enemie va vers la ball et kick vers goal
	    			if(distance<ennemiprocheballe):
	    				m=move.defgoball(positionjoueur,turfu,vitesse)
	    				s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
	    				return m+s
	    				#sinon se rerplace entre adv et soit fait une passe si quelqu'un est devant ou bien se met a distance futur possible shoot

	    			else:
	    				m=move.bbe(positionjoueur,ennemiprocheballe)
	    				if(sp==true):
	    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
	    				else:
	    					if (pd==true):
	    						s=shoot.passe(positionjoueur,poteproche,strentgh)
	    					elif(ennemiprocheballe.y>=GAME_HEIGHT/2):
	    						s=shoot.shootcotehaut(cornerh)
	    					else:
	    						s=shoot.shootcotebas(cornerb)

	    				return m+s

	    		else:
	    			if(distance<ennemiprocheballe):
	    				m=move.defgoball(positionjoueur,turfu,vitesse)
	    				if(sp==true):
	    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
	    				else:
	    					if (pd==true):
	    						s=shoot.passe(positionjoueur,poteproche,strentgh)
	    					else:
	    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
	    							s=shoot.shootcotehaut(cornerh)
	    						else:
	    							s=shoot.shootcotebas(cornerb)
	    				return m+s
	    			else:
	    				m=move.avantagezone(positionjoueur,za1)
	    				if (pd==true):
	    					s=shoot.passe(positionjoueur,poteproche,strentgh)
	    				else:
	    					if(ennemiprocheballe.y>=GAME_HEIGHT/2):
	    						s=shoot.shootcotehaut(cornerh)
	    					else:
	    						s=shoot.shootcotebas(cornerb)

	    			return m+s					





class gardien2vs2(Strategy):
	def __init__(self):
		Strategy.__init__(self, "gardien")



	def compute_strategy(self, state, id_team, id_player):
		t=Superstate(state,id_team,id_player)
    	move=Move(t)
    	shoot=Shoot(t)
    	#balle
    	positionballe=s.positionballe
    	turfu=s.balleturfu
    	#joueur
    	cageennemi=s.cageennemi
    	positionjoueur=s.positionjoueur
    	vitesse=s.vitessejoueur
    	distance=s.ballejoueur
    	gardienpos=s.gardienpos
    	attaquepos=s.attaquepos
    	#equipier
    	poteproche=s.poteproche
    	#action
    	pd=s.passepossible
    	sp=s.shootpossible
    	#ennemi
    	ennemiepos=s.ennemipos
    	ennemiprocheballe=s.ennemiprocheballe
    	#terrrain
    	z1=s.defensepos
    	cageennemi=s.cageennemi
    	cornerb=s.basennemi
    	cornerh=s.hautennemi
    	za1=s.avantagee1
    	zoneaetre=s.zoneaetre
    	#divers
    	strentgh=6

    	if (s.id_team==1):

    		if(positionballe>=GAME_WIDTH/2 + 35):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m+s
    			else:
    				m=move.attaquepos(positionjoueur,attaquepos)
    				return m

    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if (pd==true):
    					s=shoot.passe(positionjoueur,poteproche,strentgh)
    				else:
    					if(ennemiprocheballe>=GAME_HEIGHT/2):
    						s=shoot.shootcotehaut(cornerh)
    					else:
    						s=shoot.shootcotebas(cornerb)
    					return m+s
    			else:

    				m=move.cagecentre(positionjoueur,gardienpos)
    				return m
    	else:			
    		if(positionballe>=GAME_WIDTH/2 -25):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m+s
    			else:
    				m=move.attaquepos(positionjoueur,attaquepos)
    				return m

    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if (pd==true):
    					s=passe(positionjoueur,poteproche,strentgh)
    				else:
    					if(ennemiprocheballe<=GAME_HEIGHT/2):
    						s=shoot.shootcotehaut(cornerh)
    					else:
    						s=shoot.shootcotebas(cornerb)
    			else:
    				m=move.cagecentre(positionjoueur,gardienpos)
    				return m




#att 4vs4


class attaquant4vs4(Strategy):
	def __init__(self):
		Strategy.__init__(self, "gardien")



	def compute_strategy(self, state, id_team, id_player):
		t=Superstate(state,id_team,id_player)
    	move=Move(t)
    	shoot=Shoot(t)
    	#balle
    	positionballe=s.positionballe
    	turfu=s.balleturfu
    	#joueur
    	cageennemi=s.cageennemi
    	positionjoueur=s.positionjoueur
    	vitesse=s.vitessejoueur
    	distance=s.ballejoueur
    	gardienpos=s.gardienpos
    	attaquepos=s.attaquepos
    	#equipier
    	poteproche=s.poteproche
    	#action
    	pd=s.passepossible
    	sp=s.shootpossible
    	#ennemi
    	ennemiepos=s.ennemipos
    	ennemiprocheballe=s.ennemiprocheballe
    	ennemiproche=s.ennemiproche
    	#terrrain
    	z1=s.defensepos
    	cageennemi=s.cageennemi
    	cornerb=s.basennemi
    	cornerh=s.hautennemi
    	za1=s.zoneavantage
    	za2=s.zoneavantage1
    	za3=s.zoneavantage2


    	#divers
    	strentgh=6

    	if (s.id_team==1):
    		if (s.avantage==true):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m +s

    			else:
    				if(positionballe.x<za1.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.avantagezone1(positionjoueur,za1)
    					return m
    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m + s
    			else:
    				if(positionballe.x<positionjoueur.x):
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if(sp==true):
    						s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    					else:
    						if (pd==true):
    							s=shoot.passe(positionjoueur,poteproche,strentgh)
    						else:
    							if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    								s=shoot.shootcotehaut(cornerh)
    							else:
    								s=shoot.shootcotebas(cornerb)
    					return m + s

    	else:
    		if (s.avantage==true):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m +s

    			else:
    				if(positionballe.x<za1.x):
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.avantagezone1(positionjoueur,za1)
    					return m
    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m + s
    			else:
    				if(positionballe.x>positionjoueur.x):
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if(sp==true):
    						s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    					else:
    						if (pd==true):
    							s=shoot.passe(positionjoueur,poteproche,strentgh)
    						else:
    							if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    								s=shoot.shootcotehaut(cornerh)
    							else:
    								s=shoot.shootcotebas(cornerb)
    					return m + s













class centre(Strategy):
	def __init__(self):
		Strategy.__init__(self, "gardien")



	def compute_strategy(self, state, id_team, id_player):
		t=Superstate(state,id_team,id_player)
    	move=Move(t)
    	shoot=Shoot(t)
    	#balle
    	positionballe=s.positionballe
    	turfu=s.balleturfu
    	#joueur
    	cageennemi=s.cageennemi
    	positionjoueur=s.positionjoueur
    	vitesse=s.vitessejoueur
    	distance=s.ballejoueur
    	gardienpos=s.gardienpos
    	attaquepos=s.attaquepos
    	#equipier
    	poteproche=s.poteproche
    	#action
    	pd=s.passepossible
    	sp=s.shootpossible
    	#ennemi
    	ennemiepos=s.ennemipos
    	ennemiprocheballe=s.ennemiprocheballe
    	ennemiproche=s.ennemiproche
    	#terrrain
    	z1=s.defensepos
    	cageennemi=s.cageennemi
    	cornerb=s.basennemi
    	cornerh=s.hautennemi
    	za1=s.zoneavantage
    	za2=s.zoneavantage1
    	za3=s.zoneavantage2
    	zoneaetre=s.zoneaetre


    	#divers
    	strentgh=6



    	if (s.id_team==1):
    		if (s.avantage==true):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m +s

    			else:
    				if(positionballe.x<za2.x):
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.avantagezone1(positionjoueur,za2)
    					return m
    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m + s
    			else:
    				if(positionballe.x<positionjoueur.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.zoneaetre(positionjoueur,zoneaetre)
    					if(sp==true):
    						s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    					else:
    						if (pd==true):
    							s=shoot.passe(positionjoueur,poteproche,strentgh)
    						else:
    							if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    								s=shoot.shootcotehaut(cornerh)
    							else:
    								s=shoot.shootcotebas(cornerb)
    					return m + s

    	else:
    		if (s.avantage==true):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m +s

    			else:
    				if(positionballe.x<za2.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.avantagezone1(positionjoueur,za2)
    					return m
    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m + s
    			else:
    				if(positionballe.x>positionjoueur.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.zoneaetre(positionjoueur,zoneaetre)
    					if(sp==true):
    						s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    					else:
    						if (pd==true):
    							s=shoot.passe(positionjoueur,poteproche,strentgh)
    						else:
    							if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    								s=shoot.shootcotehaut(cornerh)
    							else:
    								s=shoot.shootcotebas(cornerb)
    					return m + s





class defenseur(Strategy):
	def __init__(self):
		Strategy.__init__(self, "gardien")



	def compute_strategy(self, state, id_team, id_player):
		t=Superstate(state,id_team,id_player)
    	move=Move(t)
    	shoot=Shoot(t)
    	#balle
    	positionballe=s.positionballe
    	turfu=s.balleturfu
    	#joueur
    	cageennemi=s.cageennemi
    	positionjoueur=s.positionjoueur
    	vitesse=s.vitessejoueur
    	distance=s.ballejoueur
    	gardienpos=s.gardienpos
    	attaquepos=s.attaquepos
    	#equipier
    	poteproche=s.poteproche
    	#action
    	pd=s.passepossible
    	sp=s.shootpossible
    	#ennemi
    	ennemiepos=s.ennemipos
    	ennemiprocheballe=s.ennemiprocheballe
    	ennemiproche=s.ennemiproche
    	#terrrain
    	z1=s.defensepos
    	cageennemi=s.cageennemi
    	cornerb=s.basennemi
    	cornerh=s.hautennemi
    	za1=s.zoneavantage
    	za2=s.zoneavantage1
    	za3=s.zoneavantage2
    	zoneaetre=s.zoneaetre


    	#divers
    	strentgh=6



    	if (s.id_team==1):
    		if (s.avantage==true):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m +s

    			else:
    				if(positionballe.x<za3.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.avantagezone1(positionjoueur,za3)
    					return m
    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m + s
    			else:
    				if(positionballe.x<positionjoueur.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if(sp==true):
    						s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    					else:
    						if (pd==true):
    							s=shoot.passe(positionjoueur,poteproche,strentgh)
    						else:
    							if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    								s=shoot.shootcotehaut(cornerh)
    							else:
    								s=shoot.shootcotebas(cornerb)
    					return m + s

    	else:
    		if (s.avantage==true):
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m +s

    			else:
    				if(positionballe.x<za3.x):
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					m=move.avantagezone1(positionjoueur,za3)
    					return m
    		else:
    			if(distance<ennemiprocheballe):
    				m=move.defgoball(positionjoueur,turfu,vitesse)
    				if(sp==true):
    					s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    				else:
    					if (pd==true):
    						s=shoot.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    				return m + s
    			else:
    				if(positionballe.x>positionjoueur.x):
    					m=move.defgoball(positionjoueur,turfu,vitesse)
    					if (pd==true):
    						s=shoott.passe(positionjoueur,poteproche,strentgh)
    					else:
    						if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    							s=shoot.shootcotehaut(cornerh)
    						else:
    							s=shoot.shootcotebas(cornerb)
    					return m+s
    				else:
    					if(ennemiprocheballe-ennemiproche<ennemiprocheballe- positionjoueur):
    						m=move.defgoball(positionjoueur,turfu,vitesse)
    					else:
    						m=move.antipasse(ennemiprocheballe,ennemiproche)
    					if(sp==true):
    						s=shoot.ballopied(positionjoueur,cageennemi,strentgh)
    					else:
    						if (pd==true):
    							s=shoot.passe(positionjoueur,poteproche,strentgh)
    						else:
    							if(ennemiprocheballe.y<=GAME_HEIGHT/2):
    								s=shoot.shootcotehaut(cornerh)
    							else:
    								s=shoot.shootcotebas(cornerb)
    					return m + s





