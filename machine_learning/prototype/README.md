PLI-TDC: CAN bus prototype environment
====

## The detail of files  

* ard1.dat              : raw data of delay-time (Arduino UNO)  
* ard2.dat              : raw data of delay-time (Arduino UNO)  
* minato.dat            : raw data of delay-time (Raspberry Pi)  
* panda.dat             : raw data of delay-time (Panda OBD-II Interface)  
* prius_meter.dat       : raw data of delay-time (Car A Combination Meter)  
* rpi.dat               : raw data of delay-time (Raspberry Pi)  
* suzuki_ecu.dat        : raw data of delay-time (Car B ECU)  
* suzuki_meter.dat      : raw data of delay-time (Car B Combination Meter)  
* delay_time.csv        : train and test data for rf.py and grid_search_rf.py  
* gen_LearningData.sh   : script to generate delay_time.csv  
* raw2delay.py          : script to generate delay_time.csv  
* rf.py                 : script to run random forest classifier 
* grid_search_rf.py     : script for grid seaching the hyperparameters
* rf_confusion.pdf      : result pdf

## Usage  

```
$ ./gen_LearningData.sh  

$ rf.py  
or  
$ grid_search_rf.py  
```
