from soccersimulator import Strategy, SoccerAction, Vector2D, SoccerTeam, Simulation, show_simu
from strategies import attaquant4vs4, strategy1v1, att2vs2, gardien2vs2, centre, defenseur


def get_team(nb_players):
	team = SoccerTeam(name="NICOLETOUTP800")
	if nb_players == 1:
		team.add("LilPumP", strategy1=v1())
	if nb_players == 2:
		team.add("elon", att2vs2())
		team.add("castaner",gardien2vs2())

	if nb_players == 4:
		team.add("Gardi1", gardien2vs2())
		team.add("Def", defenseur())
		team.add("Mil", centre())
		team.add("Att", attaquant4vs4())
	return team
#	
	
if __name__ == '__main__':

		team1 = get_team(4)
		team2 = get_team(4)
		
		simu = Simulation(team1, team2)
		
		show_simu(simu)
