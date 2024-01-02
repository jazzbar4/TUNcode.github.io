def setActiveInPhase(analysis, shape, shape_sets, stages, boolean):
    results = []
    for shape_set in shape_sets:
        for stage in stages:
            result = f'setActiveInPhase("{analysis}", "{shape}", ["{shape_set}"], ["{stage}"], {boolean})'
            results.append(result)
    return results




