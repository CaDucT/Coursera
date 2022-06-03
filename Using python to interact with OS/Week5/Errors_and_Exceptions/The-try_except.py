def character_frequeny(filename):
    try:
        f = open(filename)
    except OSError:
        return None

