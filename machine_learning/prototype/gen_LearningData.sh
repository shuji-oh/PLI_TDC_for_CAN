#!/bin/sh

#echo "mean,stdev,variance,skew,kurtosis,max,min,rms,en,label\n" > delay_time.csv
echo "mean,stdev,variance,skew,kurtosis,max,min,rms,en,fine_stdev,label\n" > delay_time.csv
python3 raw2delay.py panda.dat | sed 's/\ /,/g' | sed 's/$/,ECU0/' | tail -n 9000 >> delay_time.csv
#python3 raw2delay.py minato.dat | sed 's/\ /,/g' | sed 's/$/,ECU1/' | grep -v \^0.0000,0.0000, |tail -n 9000 >> delay_time.csv
python3 raw2delay.py rpi.dat | sed 's/\ /,/g' | sed 's/$/,ECU1/' | grep -v \^0.0000,0.0000, |tail -n 9000 >> delay_time.csv
python3 raw2delay.py ard1.dat | sed 's/\ /,/g' | sed 's/$/,ECU2/' | grep -v \^0.0000,0.0000, | tail -n 9000 >> delay_time.csv
python3 raw2delay.py ard2.dat | sed 's/\ /,/g' | sed 's/$/,ECU3/' | grep -v \^0.0000,0.0000, | tail -n 9000 >> delay_time.csv
python3 raw2delay.py suzuki_ecu.dat | sed 's/\ /,/g' | sed 's/$/,ECU4/' | grep -v \^0.0000,0.0000, | tail -n 9000 >> delay_time.csv
python3 raw2delay.py prius_meter.dat | sed 's/\ /,/g' | sed 's/$/,ECU5/' | tail -n 9000 >> delay_time.csv
python3 raw2delay.py suzuki_meter.dat | sed 's/\ /,/g' | sed 's/$/,ECU6/' | grep -v \^0.0000,0.0000, | tail -n 9000 >> delay_time.csv
