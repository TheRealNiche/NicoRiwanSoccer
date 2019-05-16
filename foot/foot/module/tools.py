from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu 
from soccersimulator import matches
from soccersimulator import settings
import math


class Superstate(object):
	def __init__(self,state,id_team,id_player):
		self.state=state
		self.id_team=idteam
		self.id_player=idplayer


	#balle		
	@property
	def vitesseballe(self):
		return self.state.balle.vitesse

	@property
	def positionballe(self):
		return self.state.ball.position

	@property
	def positionballex(self):
		return self.state.ball.position.x

	@property
	def positionballey(self):
		return self.state.ball.position.y

	@property
	def balleturfu(self):
		return self.positionballe + 5 * self.vitesseballe

	@property
	def ballejoueur(self):
		return self.posjoueur.distance(self.positionballe)




	#joueur
	@property
	def team(self):
		return self.id_team

	@property
	def positionjoueur(self):
		return self.player_state(self.id_team,self.id_player).position

	@property
	def positionjoueurx(self):
		return self.player_state(self.id_team,self.id_player).position.x

	@property
	def positionjoueury(self):
		return self.player_state(self.id_team,self.id_player).position.y


	@property
	def joueur(self):
		return self.player_state(self.id_team,self.id_player)


	@property
	def vitessejoueur(self):
		return self.player_state(self.id_team,self.id_player).vitesse



	@property
	def goballe(self):
		return Vector2D(self.positionballex - self.positionjoueurx, self.positionballey - self.positionballex)

	@property
	def easygoballe(self):
		return self.positionballe-self.positionjoueur


	#ttlesjoueurs
	@property
	def posallplayer(self):
		return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players]

	@property
	def playerprocheballe(self):
		p=self.posallplayer
		return min([(player.distance(self.positionballe), player) for player in playerprocheballe])


	#equipe
	
	@property
	def listepote(self):
		return [self.state.player_state(id_team,id_player).position for (id_team,id_player) in self.state.players if id_team == self.id_team and id_player != self.id_player]

	@property
	def poteproche(self):
		listepote=self.listepote
    	near = min([(player.distance(self.positionjoueur), player) for player in listepote])
        return near

	@property
	def poteprocheballe(self):
		listepote=self.listepote
    	return min([player.distance(self.positionballe) for player in listepote]


	@property		
	def potesdevant(self):
        potos = self.listepote
        if self.team == 1:
            m =  [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x > self.positionjoueurx and id_team == self.id_team]
        else:
            m =  [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players 
            if self.state.player_state(id_team, id_player).position.x < self.positionjoueurx and id_team == self.id_team]
        if m ==[]:
            return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players]
        else:
            return m



    @property
    def potes(self):
    	return self._potes
    
#adversaire
	@property
	def ennemis(self):
		return [self.state.player_state(id_team, id_player) for (id_team, id_player) in self.state.players if id_team != self.id_team]	

    @property
    def ennemipos(self):
    	return [self.state.player_state(id_team, id_player).position for (id_team, id_player) in self.state.players if id_team != self.id_team]


    @property
    def ennemiproche(self):
    	ennemi=self.ennemis
    	return min([self.positionjoueur.distance(player) for player in ennemi])


    @property
    def ennemiprocheballe(self):
        ennemi = self.ennemipos
        ballle = [player.distance(self.positionballe) for player in ennemi]
        return min(ballle)
    
    

#divers

	@property
	def passepossible(self):
		pd=self.potesdevant
		if pd!= []:
			return true
		return false

#avantage

	@property
	def avantagee1(self):
		if (score_team1(self)>score_team2(self))
			return true
		else:
			return false

	@property
	def avantagee2(self):
		if (score_team2(self)>score_team1(self))
			return true
		else:
			return false


	@property
	def zoneavantage(self):
		if self.id_team == 1:
			if (avantagee1):
				return Vector2D(GAME_WIDTH/2 - 10, 55)
		else:
			if (avantagee2):
				return Vector2D(GAME_WIDTH/2 + 10, 55)


	@property
	def zoneavantage1(self):
		if self.id_team == 1:
			if (avantagee1):
				return Vector2D(GAME_WIDTH/2 - 20, 35)
		else:
			if (avantagee2):
				return Vector2D(GAME_WIDTH/2 + 10, 55)


	@property
	def zoneavantage2(self):
		if self.id_team == 1:
			if (avantagee1):
				return Vector2D(GAME_WIDTH/2 - 30, 45)
		else:
			if (avantagee2):
				return Vector2D(GAME_WIDTH/2 + 10, 55)


#egaliteou<0
	@property
	def zoneattaque(self):
		if self.team == 1:
            if self.pos_joueur.x > 2*GAME_WIDTH/3:
                return True
            return False
        else:
            if self.pos_joueur.x < GAME_WIDTH/3:
                return True
            return False
	


	


#gardien
	@property
	def gardienpos(self):
		if (self.id_team == 1):
			return Vector2D(5,GAME_HEIGHT/2)
		else:
			return Vector2D(GAME_WIDTH-5,GAME_HEIGHT/2)

#defense
	@property
	def defensepos(self):
		if (self.id_team==1):
			return Vector2D(GAME_WIDTH/2 - 35, 45)
		else:
			return Vector2D(GAME_WIDTH/2 + 35, 45)
#attaque
	@property
	def attaquepos(self):
		if (self.id_team==1):
			return Vector2D(GAME_WIDTH/2 +15, 45)
		else:
			return Vector2D(GAME_WIDTH/2 -15, 45)
	

		

	
	
	

	@property
	def shootpossible(self, positionjoueur, turf):
        vshoot = turf - positionjoueur
        distshoot =positionjoueur.distance(turf)
                vect=balleturfu
                return vect
            
       

    @property
    def cage(self):
        return self.caged


    @property
    def cage-(self):
    	if self.id_team == 1
    		return Vector2D(GAME_WIDTH, GAME_HEIGHT/2)
        else:
            return Vector2D(0, GAME_HEIGHT/2)


    @property
    def caged(self):
    	if self.id_team == 1:
            return Vector2D(0, GAME_HEIGHT/2 + BALL_RADIUS)
        else:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT/2 - BALL_RADIUS)



    @property
    def hautennemi(self):
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH, GAME_HEIGHT)
        else:
            return Vector2D(0, GAME_HEIGHT)

    @property
    def basennemi(self):
        if self.id_team == 1:
            return Vector2D(GAME_WIDTH, 0)
        else:
            return Vector2D(0, 0)

    @property
    def hautgauche(self):
        return Vector2D(0,90)
    
    @property
    def hautedroite(self):
        return Vector2D(150,90) 
    
    @property
    def basgauche(self):
        return Vector2D(150,0)
        
    @property
    def basdroite(self):
        return Vector2D(0,0)
    
    @property
    def centre(self):
        return Vector2D(GAME_WIDTH/2,GAME_HEIGHT/2)

    


    
    
   @property
   def zoneaetre(self):
   	if id_team==1:
		if(ennemiprocheballe.y<GAME_HEIGHT/2):
	   		return Vector2D(ennemiprocheballe.x+centre.X,ennemiprocheballe.y+centre.y)
	   	else:
	   		return Vector2D(ennemiprocheballe.x-centre.X,ennemiprocheballe.y-centre.y)
   
	else:
		if(ennemiprocheballe.y<GAME_HEIGHT/2):
	   		return Vector2D(ennemiprocheballe.x-centre.X,ennemiprocheballe.y-centre.y)
	   	else:
	   		return Vector2D(ennemiprocheballe.x+centre.X,ennemiprocheballe.y+centre.y)

    


        
	
	
	
	
	

		
	



	
	
	
	
	

	
	
