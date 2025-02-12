from typing import List, Dict
from dataclasses import dataclass
import random

@dataclass
class Player:
    name: str
    attack: int
    defense: int
    intensity: int
    
    def get_total_rating(self) -> int:
        return self.attack + self.defense + self.intensity

def create_balanced_teams(players: List[Player], num_teams: int = 3) -> List[List[Player]]:
    # Sort players by total rating in descending order
    sorted_players = sorted(players, key=lambda x: x.get_total_rating(), reverse=True)
    
    # Initialize teams
    teams = [[] for _ in range(num_teams)]
    team_ratings = {
        'attack': [0] * num_teams,
        'defense': [0] * num_teams,
        'intensity': [0] * num_teams
    }
    
    # Distribute players using snake draft order to ensure fairness
    for i, player in enumerate(sorted_players):
        # Find team with lowest total ratings
        team_totals = [sum(ratings) for ratings in zip(
            team_ratings['attack'],
            team_ratings['defense'],
            team_ratings['intensity']
        )]
        
        target_team = team_totals.index(min(team_totals))
        
        # Add player to team
        teams[target_team].append(player)
        team_ratings['attack'][target_team] += player.attack
        team_ratings['defense'][target_team] += player.defense
        team_ratings['intensity'][target_team] += player.intensity
    
    return teams

# Example usage
def main():
    # Create sample players
    players = []
    names = [f"Player{i+1}" for i in range(15)]
    
    for name in names:
        players.append(Player(
            name=name,
            attack=random.randint(1, 5),
            defense=random.randint(1, 5),
            intensity=random.randint(1, 5)
        ))
    
    # Create balanced teams
    balanced_teams = create_balanced_teams(players)
    
    # Print results
    for i, team in enumerate(balanced_teams):
        print(f"\nTeam {i+1}:")
        team_attack = sum(p.attack for p in team)
        team_defense = sum(p.defense for p in team)
        team_intensity = sum(p.intensity for p in team)
        
        print(f"Total ratings - Attack: {team_attack}, Defense: {team_defense}, Intensity: {team_intensity}")
        print("Players:")
        for player in team:
            print(f"{player.name}: A={player.attack}, D={player.defense}, I={player.intensity}")

if __name__ == "__main__":
    main()