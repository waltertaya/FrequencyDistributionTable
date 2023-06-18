n = eval(input('Enter the number of elements in the distribution: '))
elements = []
print('Key in the elements in the distribution: ')
for i in range(n):
    element = eval(input(' '))
    elements.append(element)

from class_interval import calculate_interval
from class_limit import calcute_limit
from frequency import count_frequency
C, K, smallest = calculate_interval(n, elements)
class_lower, class_upper, class_midpoint = calcute_limit(n, elements)
class_count, C, K = count_frequency(n, elements)

print('Frequency Distribution Table')
classes = []
for i in range(K):
    classes.append((class_lower[i], class_upper[i]))

import pandas as pd
table_data = {
    'class': classes,
    'midpoints': class_midpoint,
    'frequency': class_count
}
df = pd.DataFrame(table_data)
print(df)
