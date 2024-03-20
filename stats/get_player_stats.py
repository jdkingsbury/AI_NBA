from db.retrieve_data import retrieve_and_calculate_data

def get_player_stats(player_id, season_id):
    stats = {
        "ppg": retrieve_and_calculate_data('get_total_points_and_games_played', 'ppg', player_id, season_id),
        "rpg": retrieve_and_calculate_data('get_total_rebounds_and_games_played', 'rpg', player_id, season_id),
        "apg": retrieve_and_calculate_data('get_total_assists_and_games_played', 'apg', player_id, season_id),
        "spg": retrieve_and_calculate_data('get_total_steals_and_games_played', 'spg', player_id, season_id),
        "bpg": retrieve_and_calculate_data('get_total_blocks_and_games_played', 'bpg', player_id, season_id),
        "tov": retrieve_and_calculate_data('get_total_turnovers_and_games_played', 'tov', player_id, season_id),
        "fg_percent": retrieve_and_calculate_data('get_total_field_goals_made_and_attempted', 'fg_percent', player_id, season_id),
        "three_point_percent": retrieve_and_calculate_data('get_total_three_pointers_made_and_attempted', 'three_point_percent', player_id, season_id),
        "ft_percent": retrieve_and_calculate_data('get_total_free_throws_made_and_attempted', 'ft_percent', player_id, season_id),
    }
    return stats