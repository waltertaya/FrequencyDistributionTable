#class_interval.py
'''
This file calculates the range, number of classes and class interval
'''
def calculate_interval(n, elements):
    smallest = float('inf')
    largest = float('-inf')
    for i in range(n):
        if elements[i] < smallest:
            smallest = elements[i]
        if elements[i] > largest:
            largest = elements[i]
    R = largest - smallest
    from math import ceil, log
    K = ceil(log(n)/log(2))
    C = ceil(R / K)
    return K, C, smallest
