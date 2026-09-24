# Project Statement: F1 Race Analytics & Strategy Dashboard
# Problem Statement
Formula 1 tracking involves complex rules, multi-tier scoring systems, and dynamic strategy considerations. Beginners and motorsport enthusiasts often lack a clean, offline platform to record Grand Prix results, dynamically evaluate driver and constructor standings, and run race stint simulations.

# Scope of the Project
This application provides a lightweight, offline first SQLite analytics engine. 
It enables users to record race schedules, log finishing positions, compute championship leaderboards using official FIA points rules (top 10 plus fastest lap bonus), and run tyre strategy comparisons.

# Target Users
- Motorsport fans interested in tracking race weekends and points distributions.
- Users exploring simple numerical simulations for pit stop lap windows.

# High Level Features
- Grand Prix Ingestion: Add races and record driver finishing orders.
- Standings Engine: Automatic points tallies for both Drivers and Constructors based on standard FIA scoring.
- Strategy Simulator: Compares 1-stop and 2-stop stint durations across Soft, Medium, and Hard tyre compounds.
