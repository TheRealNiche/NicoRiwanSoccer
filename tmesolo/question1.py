from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam
from soccersimulator import VolleySimulation, volley_show_simu

class EchauffementStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"trainee")

    def compute_strategy(self, state, id_team, id_player):
        p1=state.player_state(id_team,id_player).position
        a=state.ball.position
        v1=Vector2D(135,45)
        v2=Vector2D(45,45)
        if (id_team==1):
            return SoccerAction(acceleration=a-p1,shoot=v1-a)
        if (id_team==2):
            return SoccerAction(acceleration=a-p1,shoot=v2-a)

# Create teams
team1 = SoccerTeam(name="bataillon1")
team2 = SoccerTeam(name="bataillon2")

# Add players
team1.add("HAL9000", EchauffementStrategy())  
team2.add("MONOLITH", EchauffementStrategy())  

# Create a match
simu = VolleySimulation(team1, team2)

# Simulate and display the match
volley_show_simu(simu)
