from typing import List, Dict
from dataclasses import dataclass
import random
import csv

@dataclass
class Player:
    name: str
    attack: float
    defense: float
    intensity: float
    
    def get_total_rating(self) -> int:
        return self.attack + self.defense + self.intensity

def load_players_from_csv(filename: str) -> List[Player]:
    players = []
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            players.append(Player(
                name=row['name'],
                attack=float(row['attack'].replace(',', '.')),
                defense=float(row['defense'].replace(',', '.')),
                intensity=float(row['intensity'].replace(',', '.'))
            ))
    return players

def create_balanced_teams(players: List[Player], num_teams: int = 3) -> List[List[Player]]:
    # Sort players by total rating in descending order
    sorted_players = sorted(players, key=lambda x: x.get_total_rating(), reverse=True)
    
    # Calculate minimum number of teams needed
    min_teams_needed = (len(sorted_players) + 4) // 5  # Round up division
    num_teams = max(num_teams, min_teams_needed)
    
    # Initialize teams
    teams = [[] for _ in range(num_teams)]
    team_ratings = {
        'attack': [0] * num_teams,
        'defense': [0] * num_teams,
        'intensity': [0] * num_teams
    }
    
    # Distribute players using snake draft order to ensure fairness
    for i, player in enumerate(sorted_players):
        # Find team with lowest total ratings among teams with less than 5 players
        team_totals = [
            sum(ratings) if len(teams[idx]) < 5 else float('inf')
            for idx, ratings in enumerate(zip(
                team_ratings['attack'],
                team_ratings['defense'],
                team_ratings['intensity']
            ))
        ]
        
        target_team = team_totals.index(min(team_totals))
        
        # Add player to team
        teams[target_team].append(player)
        team_ratings['attack'][target_team] += player.attack
        team_ratings['defense'][target_team] += player.defense
        team_ratings['intensity'][target_team] += player.intensity

    return teams

def main():
    # Load players from CSV
    players = load_players_from_csv('/mnt/data/players.csv')
    
    # Create balanced teams
    balanced_teams = create_balanced_teams(players, num_teams=5)
    
    # Print results
    for i, team in enumerate(balanced_teams):
        print(f"\nTeam {i+1}:")
        team_attack = sum(p.attack for p in team)
        team_defense = sum(p.defense for p in team)
        team_intensity = sum(p.intensity for p in team)
        
        print(f"Total ratings - Attack: {team_attack/5}, Defense: {team_defense/5}, Intensity: {team_intensity/5}")
        print("Players:")
        for player in team:
            print(f"{player.name}: A={player.attack}, D={player.defense}, I={player.intensity}")

if __name__ == "__main__":
    main()