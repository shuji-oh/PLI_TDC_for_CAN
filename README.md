PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter
====

## Overview

[Shuji Ohira, Araya Kibrom Desta, Tomoya Kitagawa, Ismail Arai, Kazutoshi Fujikawa, "PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks," In Proceedings of the 16th ACM Asia Conference on Computer and Communications Security (ASIA CCS ’21), pp.1-11, June. 2021.]()

```
@inproceedings{ohira2020pli-tdc,
  title={PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks},
  author={Ohira, Shuji and Kibrom Desta, Araya and Arai, Ismail and Fujikawa, Kazutoshi},
  booktitle={Proceedings of the 16th ACM Asia Conference on Computer and Communications Security},
  pages={1--11},
  year={2021},
  organization={ACM}
}
```

## Directory Structure

PLI_TDC_for_CAN  
┣━ hardware  
┃   ┣━ c5 (for Cyclone 5)  
┃   ┃	┣━ main.v  
┃   ┃	┣━ fifo.v  
┃   ┃	┣━ spi.v  
┃   ┃	┣━ out_hex.v  
┃   ┃	┣━ measure_time.v  
┃   ┃	┣━ adder.v  
┃	┃   ┗━ tapped_delay_tdc.v  
┃	┗━ c3 (for Cyclone 3)  
┃   	┣━ main.v  
┃   	┣━ fifo.v  
┃   	┣━ spi.v  
┃   	┣━ out_hex.v  
┃   	┣━ measure_time.v  
┃   	┣━ adder.v  
┃	    ┗━ tapped_delay_tdc.v  
┣━ machine_learning  
┃	┣━ prototype  
┃   ┃   ┣━ rf.py  
┃   ┃   ┣━ grid_search_rf.py  
┃   ┃   ┣━ raw2delay.py  
┃   ┃   ┣━ gen_LearningData.sh  
┃	┃   ┗━ delay_time.py  
┃	┗━ real-vehicle  
┃       ┣━ rf.py  
┃       ┣━ grid_search_rf.py  
┃       ┣━ raw2delay.py  
┃       ┣━ gen_LearningData.sh  
┃	    ┗━ delay_time.csv  
┗━ recv_script  
	┣━ build.sh  
    ┣━ tdc_recv.c  
	┗━ temp_read.c  

## Requirement

python3  
Quartus (Quartus Prime 17.0)  

## Usage (machine learning)

$ git clone https://github.com/shuji-oh/Divider  
$ cd machine_learning/prototype  
$ python3 knn.py  

## Author

[shuji-oh](https://github.com/shuji-oh)
