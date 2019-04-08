from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_sim


class jefaistout(strategy):
	def __init__(self):
		Strategy.__init__(self,"Defense")

	def compute_strategy(self, state, id_team, id_player):
        
		p1=state.player_state(1,id_player).position
		p2=state.player_state(2,id_player).position
		a=state.ball.position
		future=a+8*state.ball.vitesse
        if(a.position>Vector2D(90,0)):
			if(id_team==1):
				if(a.distance(p1)<35):
					v1=Vector2D(135,45)
					return SoccerAction(acceleration=a-p1,shoot=v1-a)
				else:
					v1=Vector2D(55,future.y)
					return SoccerAction(v1-p1)
			else :
				if(a.distance(p2)<35):
					v1=Vector2D(45,45)
					return SoccerAction(acceleration=a-p2,shoot=v1-a)
				else:
					v1=Vector2D(125,future.y)
					return SoccerAction(v1-p2)
		else:
			if (id_team==1):
				if(p2.x>135):
					if (p2.y>=45) :
						v1=Vector2D(90,0)
					else:
						v2=Vector2D(90,90)
				else:
					if (p2.y>45) :
						v1=Vector2D(180,0)
					else:
						v1=Vector2D(180,90)
						return SoccerAction(acceleration=a-p1,shoot=v1-a)
			if (id_team==2):
				if(p1.x<=45):
					if (p1.y>=45) :
						v1=Vector2D(45,0)
					else:
						v1=Vector2D(45,90)
				else:
					if (p1.y<45) :
						v1=Vector2D(0,90)
					else:
						v1=Vector2D(0,0)
				return SoccerAction(acceleration=a-p2,shoot=v2-a)
				
        
        


            
            
            
team1 = SoccerTeam(name="bataillon1")
team2 = SoccerTeam(name="bataillon2")

# Add players
team2.add("Billgateslephilantrope", jefaistout())
team1.add("elonmusklaltruiste", jefaistout())   

# Create a match
simu = VolleySimulation(team1, team2)
