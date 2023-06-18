#frequency.py
'''
This file is used to calculate frequency of the classes in the distribution
'''
def count_frequency(n, elements):
    from class_interval import calculate_interval
    C, K, smallest = calculate_interval(n, elements)
    from class_limit import calcute_limit
    class_lower, class_upper, class_midpoint = calcute_limit(n, elements)
    class_count = [0] * K  
    for i in range(n):
        for j in range(K):
            if elements[i] >= class_lower[j] and elements[i] <= class_upper[j]:
                class_count[j] += 1 
                break
    return class_count, C, K
