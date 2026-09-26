import sqlite3


def get_connection():
    # Connects to our local database file
    return sqlite3.connect("f1_system.db")


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Table 1: Drivers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            team TEXT
        )
    """)

    # Table 2: Races
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS races (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            laps INTEGER
        )
    """)

    # Table 3: Results
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            race_id INTEGER,
            driver_name TEXT,
            team_name TEXT,
            position INTEGER,
            fastest_lap INTEGER
        )
    """)

    conn.commit()

    # Pre-populate default drivers if table is empty
    cursor.execute("SELECT COUNT(*) FROM drivers")
    count = cursor.fetchone()[0]
    if count == 0:
        default_drivers = [("Max Verstappen", "Red Bull Racing"),
                           ("Isack Hadjar", "Red Bull Racing"),
                           ("Lewis Hamilton", "Ferrari"),
                           ("Charles Leclerc", "Ferrari"),
                           ("Lando Norris", "McLaren"),
                           ("Oscar Piastri", "McLaren"),
                           ("George Russell", "Mercedes"),
                           ("Kimi Antonelli", "Mercedes"), 
                           ("Carlos Sainz", "Williams"), 
                           ("Alexander Albon", "Williams"),
                           ("Liam Lawson", "Racing Bulls"),
                           ("Arvid Lindblad", "Racing Bulls"),
                           ("Esteban Ocon", "Haas F1 Team"),
                           ("Oliver Bearman", "Haas F1 Team"),
                           ("Pierre Gasly", "Alpine"),
                           ("Franco Colapinto", "Alpine"),
                           ("Fernando Alonso", "Aston Martin"), 
                           ("Lance Stroll", "Aston Martin"), 
                           ("Nico Hülkenberg", "Audi"),
                           ("Gabriel Bortoleto", "Audi"), 
                           ("Sergio Pérez", "Cadillac"),
                           ("Valtteri Bottas", "Cadillac")
                           ]
        cursor.executemany("INSERT INTO drivers (name, team) VALUES (?, ?)",
                           default_drivers)
        conn.commit()

    conn.close()
