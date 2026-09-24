# F1 Race Analytics & Strategy Dashboard
 
A beginner friendly, modular Python command line dashboard designed to log Formula 1 race results, calculate championship standings, and simulate pit-stop strategies.

#Overview
1. Race Ingestion: Manage Grand Prix events, default driver rosters, and finishing orders.
2. Standings Engine: Compute driver and constructor standings using official FIA scoring.
3. Strategy Simulator: Calculate stint lengths and pit stop windows across Soft, Medium, and Hard compounds.

#Technologies Used
- Programming Language: Python 3.x
- Database: SQLite3 (standard library)
- Architecture: Modular programming (functions, lists, dictionaries)

#Project Structure
- `database.py`: Handles SQLite database initialization and default driver records.
- `race_manager.py`: Functions to create races and insert finishing results.
- `standings_service.py`: Computes Driver and Constructor Championship leaderboards.
- `strategy_simulator.py`: Numerical model for tyre stint calculations.
- `validators.py`: Input validation for race laps, positions, and compounds.
- `test_f1.py`: Unit test assertions for core calculations.
- `main.py`: Command line interactive menu interface.

#Installation & Execution
1. Clone or download this repository:
   ```bash
   git clone <YOUR-REPOSITORY-URL>
   cd f1-race-analytics-dashboard
