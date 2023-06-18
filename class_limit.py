#class_limit.py
'''
This file contains the formulae for calculating class limits
'''
def calcute_limit(n, elements):
    from class_interval import calculate_interval
    C, K, smallest = calculate_interval(n, elements)
    class_lower = []
    class_upper = []
    class_midpoint = []
    for i in range(K):
        lower = smallest + (i * C)
        upper = lower + C - 1
        midpoint = (lower + upper) / 2
        class_lower.append(lower)
        class_upper.append(upper)
        class_midpoint.append(midpoint)
    return class_lower, class_upper, class_midpoint
