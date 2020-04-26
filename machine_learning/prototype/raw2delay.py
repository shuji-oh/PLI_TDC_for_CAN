import sys
from statistics import mean, median, variance, stdev
from scipy.stats import skew, kurtosis
from functools import reduce
from math import sqrt

def rms(xs):
    return sqrt(reduce(lambda a, x: a + x * x, xs, 0) / len(xs))

def en(xs):
    return reduce(lambda a, x: a + x * x, xs, 0) / len(xs)

params = sys.argv
sum_delay_list = []
sum_fine_delay_list = []
count = 0
with open(params[1],'r') as f:
    for row in f:
    	if '[packet_' == row[0:8]:
            if count > 2:
                print('{:.4f}'.format(mean(sum_delay_list)),\
                      '{:.4f}'.format(stdev(sum_delay_list)),\
                      '{:.4f}'.format(variance(sum_delay_list)),\
                      '{:.4f}'.format(skew(sum_delay_list)),\
                      '{:.4f}'.format(kurtosis(sum_delay_list)),\
                      '{:.4f}'.format(max(sum_delay_list)),\
                      '{:.4f}'.format(min(sum_delay_list)),\
                      '{:.4f}'.format(rms(sum_delay_list)),\
                      '{:.4f}'.format(en(sum_delay_list)),\
                      '{:.4f}'.format(stdev(sum_fine_delay_list)),\
                      )
            sum_delay_list.clear()
            sum_fine_delay_list.clear()
            count = 0
    	else :
            row_spt             = row.split(',')
            row_id_spt          = row_spt[0].split(':')
            row_coarse_time_spt = row_spt[1].split(':')
            row_fine_time_spt   = row_spt[2].split(':')
            coarse_time         = float(int(row_coarse_time_spt[1], 16) * 20)
            fine_time           = float(int(row_fine_time_spt[1], 16) * 0.154)
            elapsed_time        = coarse_time + fine_time
            #elapsed_time        = coarse_time
            #print(coarse_time,fine_time,elapsed_time)

            ideal_time = int((elapsed_time+500)/2000)*2000
            delay_time = elapsed_time - ideal_time
            sum_delay_list.append(delay_time)
            sum_fine_delay_list.append(fine_time)
            count += 1
