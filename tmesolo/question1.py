from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu

class EchauffementStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"trainee")

    def compute_strategy(self, state, id_team, id_player):
        a=state.player_state(id_team,id_player).position
        b=state.ball.position
        v1=Vector2D(135,45)
        v2=Vector2D(45,45)
        if (id_team==1):
            return SoccerAction(acceleration=b-a,shoot=v1-b)
        if (id_team==2):
            return SoccerAction(acceleration=b-a,shoot=v2-b)

# Create teams
team1 = SoccerTeam(name="bataillon1")
team2 = SoccerTeam(name="bataillon2")

# Add players
team1.add("dylan", EchauffementStrategy())  
team2.add("kevin", EchauffementStrategy())  

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
