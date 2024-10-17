import scipy as sc
import random

LIST = []

for i in range(0, 50):
    LIST.append(random.randint(10, 30))

import scipy as sc
import random

LIST = []

for i in range(0, 50):
    LIST.append(random.randint(10, 30))


LIST_AVERAGE = sum(LIST) / len(LIST)
LIST_SD = sc.stats.tstd(LIST)
DEGREE_F = len(LIST) - 1

CONF_INTERVAL = sc.stats.t.interval(0.95, DEGREE_F, loc=LIST_AVERAGE, scale=LIST_SD)
CONF_INTERVAL2 = sc.stats.norm.interval(0.95, loc=LIST_AVERAGE, scale=LIST_SD)



print('List: ',LIST)
print('Average: ',LIST_AVERAGE)
print('Std: ',LIST_SD)
print('CONF_INTERVAL: ',CONF_INTERVAL)
print('CONF_INTERVAL-NORMAL: ',CONF_INTERVAL2)
LIST_AVERAGE = sum(LIST) / len(LIST)
LIST_SD = sc.stats.tstd(LIST)
DEGREE_F = len(LIST) - 1

CONF_INTERVAL = sc.stats.t.interval(0.95, DEGREE_F, loc=LIST_AVERAGE, scale=LIST_SD)
CONF_INTERVAL2 = sc.stats.norm.interval(0.95, loc=LIST_AVERAGE, scale=LIST_SD)

print('List: ',LIST)
print('Average: ',LIST_AVERAGE)
print('Std: ',LIST_SD)
print('CONF_INTERVAL: ',CONF_INTERVAL)
print('CONF_INTERVAL-NORMAL: ',CONF_INTERVAL2)