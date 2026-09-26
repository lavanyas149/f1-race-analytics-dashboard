from database import get_connection

# Points mapping for top 10 finishers
POINTS = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}


def get_driver_standings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT driver_name, team_name, position, fastest_lap FROM results")
    all_results = cursor.fetchall()
    conn.close()

    # Dictionary to store stats for each driver
    table = {}

    for row in all_results:
        driver = row[0]
        team = row[1]
        pos = row[2]
        fl = row[3]

        if driver not in table:
            table[driver] = {"team": team, "points": 0, "wins": 0}

        # Add points if finished in top 10
        if pos in POINTS:
            table[driver]["points"] += POINTS[pos]

        # Add 1 bonus point for fastest lap if in top 10
        if fl == 1 and pos <= 10:
            table[driver]["points"] += 1

        # Check win
        if pos == 1:
            table[driver]["wins"] += 1

    return table


def get_constructor_standings():
    # Sum up points from drivers for each team
    driver_table = get_driver_standings()
    team_table = {}

    for driver, stats in driver_table.items():
        team = stats["team"]
        pts = stats["points"]

        if team not in team_table:
            team_table[team] = 0
        team_table[team] += pts

    return team_table
