from database import get_connection


def add_new_race(race_name, laps):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO races (name, laps) VALUES (?, ?)",
                   (race_name, laps))
    conn.commit()
    conn.close()


def get_all_races():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, laps FROM races")
    races = cursor.fetchall()
    conn.close()
    return races


def get_all_drivers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, team FROM drivers")
    drivers = cursor.fetchall()
    conn.close()
    return drivers


def save_result(race_id, driver_name, team_name, position, fastest_lap):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO results (race_id, driver_name, team_name, position, fastest_lap)
        VALUES (?, ?, ?, ?, ?)
    """, (race_id, driver_name, team_name, position, fastest_lap))
    conn.commit()
    conn.close()


def get_race_results(race_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT position, driver_name, team_name, fastest_lap
        FROM results
        WHERE race_id = ?
        ORDER BY position ASC
    """, (race_id, ))
    rows = cursor.fetchall()
    conn.close()
    return rows
