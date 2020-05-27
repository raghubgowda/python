def lbs_to_kg(weight: float):
    if weight > 0.0:
        return weight * 0.45
    else:
        return 0.0


def kg_to_lbs(weight: float):
    if weight > 0.0:
        return weight / 0.45
    else:
        return 0.0
