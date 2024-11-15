teams = ['AB', 'BC', 'MN', 'SK', 'ON', 'QC', 'PE', 'NS', 'NB', 'NL', 'YT', 'NT', 'NU']
games = [
    {'home': 'BC', 'homeScore': 0, 'away': 'YT', 'awayScore': 0}, 
    {'home': 'NU', 'homeScore': 2, 'away': 'NS', 'awayScore': 2}, 
    {'home': 'PE', 'homeScore': 0, 'away': 'YT', 'awayScore': 2}, 
    {'home': 'NU', 'homeScore': 1, 'away': 'YT', 'awayScore': 3},
    {'home': 'NT', 'homeScore': 3, 'away': 'ON', 'awayScore': 1},
    {'home': 'NU', 'homeScore': 2, 'away': 'ON', 'awayScore': 1},
    
]

teamData = {
    'AB': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'BC': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'MN': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'SK': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'ON': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'QC': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'PE': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'NS': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'NB': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'NL': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'YT': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'NT': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
    'NU': {'gamesPlayed': 0, 'wins': 0, 'losses': 0, 'ties': 0, 'goalsFor': 0, 'goalsAgainst': 0},
}


for game in games:
    home_team = game['home']
    away_team = game['away']
    home_score = game['homeScore']
    away_score = game['awayScore']
    
  
    teamData[home_team]['gamesPlayed'] += 1
    teamData[away_team]['gamesPlayed'] += 1
    
   
    teamData[home_team]['goalsFor'] += home_score
    teamData[away_team]['goalsFor'] += away_score
    teamData[home_team]['goalsAgainst'] += away_score
    teamData[away_team]['goalsAgainst'] += home_score
    
 
    if home_score > away_score:
        teamData[home_team]['wins'] += 1
        teamData[away_team]['losses'] += 1
    elif home_score < away_score:
        teamData[away_team]['wins'] += 1
        teamData[home_team]['losses'] += 1
    else:
        teamData[home_team]['ties'] += 1
        teamData[away_team]['ties'] += 1


def tests():
    assert teamData['BC']['gamesPlayed'] == 12
    assert teamData['BC']['wins'] == 5
   

tests()


for team, stats in teamData.items():
    print(f"{team}: {stats}")
