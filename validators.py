#Simple input checkers using basic if statements.


def is_valid_position(pos):
    # Check if position is an integer between 1 and 22
    if pos.isdigit():
        val = int(pos)
        if 1 <= val <= 22:
            return True
    return False


def is_valid_compound(compound):
    # Only allow Soft, Medium, Wet or Hard
    clean = compound.strip().upper()
    if clean in ["SOFT", "MEDIUM", "HARD", "WET"]:
        return True
    return False


def is_valid_laps(laps):
    # Check if laps is a reasonable positive number
    if laps.isdigit():
        val = int(laps)
        if 10 <= val <= 100:
            return True
    return False
