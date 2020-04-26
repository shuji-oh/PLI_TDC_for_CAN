#!/bin/sh

echo "mean,stdev,variance,skew,kurtosis,max,min,rms,en,fine_stdev,label\n" > delay_time.csv
# power steering
python3 raw2delay.py delay_262.txt | sed 's/\ /,/g' | sed 's/$/,ECU0/' | tail -n 1000 >> delay_time.csv 
# combination meter
python3 raw2delay.py delay_meter.txt | sed 's/\ /,/g' | sed 's/$/,ECU1/' | tail -n 1000 >> delay_time.csv
# steering
python3 raw2delay.py delay_025.txt | sed 's/\ /,/g' | sed 's/$/,ECU2/' | tail -n 1000 >> delay_time.csv
# skid control
python3 raw2delay.py delay_0B4.txt | sed 's/\ /,/g' | sed 's/$/,ECU3/' | tail -n 1000 >> delay_time.csv
# transmission control
python3 raw2delay.py delay_127.txt | sed 's/\ /,/g' | sed 's/$/,ECU4/' | tail -n 1000 >> delay_time.csv
# engine control
python3 raw2delay.py delay_1C4.txt | sed 's/\ /,/g' | sed 's/$/,ECU5/' | tail -n 1000 >> delay_time.csv
# unkown
python3 raw2delay.py delay_1CE.txt | sed 's/\ /,/g' | sed 's/$/,ECU6/' | tail -n 1000 >> delay_time.csv
