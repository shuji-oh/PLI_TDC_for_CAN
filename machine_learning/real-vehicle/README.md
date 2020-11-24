PLI-TDC: real-vehicle CAN bus environment
====

## The detail of files  

* delay_0B4.dat         : raw data of delay-time (Skid Control ECU)  
* delay_1C4.dat         : raw data of delay-time (Engine Control ECU)  
* delay_1CE.dat         : raw data of delay-time (Unknown ECU)  
* delay_025.dat         : raw data of delay-time (Steering ECU)  
* delay_127.dat         : raw data of delay-time (Transmission Control ECU)  
* delay_262.dat         : raw data of delay-time (Power Steering ECU)  
* delay_meter.dat       : raw data of delay-time (Combination Meter ECU)  
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
