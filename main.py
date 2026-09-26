from database import setup_database
from race_manager import add_new_race, get_all_races, get_all_drivers, save_result, get_race_results
from standings_service import get_driver_standings, get_constructor_standings
from strategy_simulator import simulate_one_stop, simulate_two_stop
from validators import is_valid_position, is_valid_compound, is_valid_laps


def show_menu():
    print("\n------------------------ F1 ---------------------------")
    print("   FORMULA 1 RACE DASHBOARD    ")
    print("------------------------ F1 ---------------------------")
    print("1. View Championship Standings")
    print("2. Add a New Grand Prix")
    print("3. Enter Race Result")
    print("4. View Results of a Race")
    print("5. Tyre Strategy Simulator")
    print("6. Exit")


def main():
    setup_database()

    while True:
        show_menu()
        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            print("\n--- DRIVER STANDINGS ---")
            drivers = get_driver_standings()
            if not drivers:
                print("No results logged yet.")
            else:
                for name, data in drivers.items():
                    print(
                        f"Driver: {name:<18} | Team: {data['team']:<12} | Points: {data['points']:<4} | Wins: {data['wins']}"
                    )

            print("\n--- CONSTRUCTOR STANDINGS ---")
            teams = get_constructor_standings()
            for team, points in teams.items():
                print(f"Team: {team:<15} | Total Points: {points}")

        elif choice == "2":
            name = input("Enter Grand Prix name (e.g. Monza GP): ").strip()
            laps = input("Enter total laps (e.g. 53): ").strip()

            if is_valid_laps(laps):
                add_new_race(name, int(laps))
                print(">> Race successfully added!")
            else:
                print(">> Invalid laps entered. Must be between 10 and 100.")

        elif choice == "3":
            races = get_all_races()
            if not races:
                print(">> Please add a race first using Option 2.")
                continue

            print("\nAvailable Races:")
            for r in races:
                print(f"ID: {r[0]} | Name: {r[1]} ({r[2]} laps)")
            race_id = input("Enter Race ID: ").strip()

            drivers = get_all_drivers()
            print("\nDrivers:")
            for d in drivers:
                print(f"ID: {d[0]} | {d[1]} ({d[2]})")
            driver_id = input("Enter Driver ID: ").strip()

            pos = input("Enter finish position (1-20): ").strip()
            if not is_valid_position(pos):
                print(">> Invalid position. Enter a number between 1 and 20.")
                continue

            fl_choice = input(
                "Did this driver get fastest lap? (y/n): ").strip().lower()
            fastest_lap = 1 if fl_choice == "y" else 0

            # Find matching driver details
            selected_driver = None
            for d in drivers:
                if str(d[0]) == driver_id:
                    selected_driver = d
                    break

            if selected_driver:
                save_result(int(race_id), selected_driver[1],
                            selected_driver[2], int(pos), fastest_lap)
                print(">> Result recorded successfully!")
            else:
                print(">> Driver ID not found.")

        elif choice == "4":
            races = get_all_races()
            for r in races:
                print(f"ID: {r[0]} | {r[1]}")
            r_id = input("Enter Race ID to view: ").strip()

            results = get_race_results(int(r_id))
            print("\n--- RACE RESULTS ---")
            for res in results:
                fl = "Yes (+1 pt)" if res[3] == 1 else "No"
                print(
                    f"P{res[0]:<2} | {res[1]:<18} | {res[2]:<12} | Fastest Lap: {fl}"
                )

        elif choice == "5":
            laps = input("Enter total race laps to simulate: ").strip()
            if not is_valid_laps(laps):
                print(">> Invalid lap count.")
                continue

            c1 = input("Tyre 1 (SOFT/MEDIUM/HARD): ").strip().upper()
            c2 = input("Tyre 2 (SOFT/MEDIUM/HARD): ").strip().upper()

            if is_valid_compound(c1) and is_valid_compound(c2):
                plan = simulate_one_stop(int(laps), c1, c2)
                print(f"\n[1-STOP PLAN]")
                print(f"  Stint 1: {plan['stint_1']}")
                print(f"  Pit Stop: Lap {plan['pit_lap']}")
                print(f"  Stint 2: {plan['stint_2']}")
                print(f"  Estimated Race Time: {plan['est_time']} seconds")
            else:
                print(">> Invalid tyre compounds.")

        elif choice == "6":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice, please select 1 to 6.")


if __name__ == "__main__":
    main()
