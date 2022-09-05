def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time is None:
        return None
    for i in permanence_period:
        if type(i[0]) != int or type(i[1]) != int:
            return None
        if i[0] <= target_time <= i[1]:
            counter += 1
    return counter
