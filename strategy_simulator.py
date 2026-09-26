def simulate_one_stop(total_laps, first_tyre, second_tyre):
    # Split the race evenly in half
    pit_lap = total_laps // 2
    stint_1 = pit_lap
    stint_2 = total_laps - pit_lap

    # Basic baseline time per lap (90s) + 22s pit stop loss
    estimated_time = (total_laps * 90) + 22

    result = {
        "stint_1": f"{first_tyre} for {stint_1} laps",
        "stint_2": f"{second_tyre} for {stint_2} laps",
        "pit_lap": pit_lap,
        "est_time": estimated_time
    }
    return result


def simulate_two_stop(total_laps, tyre1, tyre2, tyre3):
    # Split race into 3 roughly equal stints
    stint_1 = total_laps // 3
    stint_2 = total_laps // 3
    stint_3 = total_laps - (stint_1 + stint_2)

    pit_1 = stint_1
    pit_2 = stint_1 + stint_2

    # Basic baseline time + 44s for 2 pit stops
    estimated_time = (total_laps * 90) + 44

    result = {
        "stint_1": f"{tyre1} for {stint_1} laps",
        "stint_2": f"{tyre2} for {stint_2} laps",
        "stint_3": f"{tyre3} for {stint_3} laps",
        "pit_1": pit_1,
        "pit_2": pit_2,
        "est_time": estimated_time
    }
    return result
