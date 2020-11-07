Divider: Delay-Time Based Sender Identification in Automotive Networks
====

## Overview

Divider is sender Identification method based on delay caused by CAN transceiver.

[Shuji Ohira, Araya Kibrom Desta, Tomoya Kitagawa, Ismail Arai, Kazutoshi Fujikawa, "PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks," In Proceedings of the 16th ACM Asia Conference on Computer and Communications Security (ASIA CCS ’21), pp.1-11, June. 2021.](https://arxiv.org/pdf/2008.10941.pdf)

```
@inproceedings{ohira2020Divider,
  title={PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks},
  author={Ohira, Shuji and Kibrom Desta, Araya and Arai, Ismail and Fujikawa, Kazutoshi},
  booktitle={Proceedings of the 16th ACM Asia Conference on Computer and Communications Security},
  pages={1--11},
  year={2021},
  organization={ACM}
}
```

## Description



## Directory Structure

PLI_TDC_for_CAN  
┣━ hardware  
┃	┣━ main.v  
┃	┣━ fifo.v  
┃	┣━ spi.v  
┃	┣━ out_hex.v  
┃	┣━ measure_time.v  
┃	┗━ run.sh  
┣━ machine_learning  
┃	┣━ prototype  
┃   ┃   ┣━ knn.py  
┃   ┃   ┣━ raw2delay.py  
┃   ┃   ┣━ gen_LearningData.sh  
┃	┃   ┗━ delay_time.py  
┃	┗━ real-vehicle  
┃       ┣━ knn.py  
┃       ┣━ raw2delay.py  
┃       ┣━ gen_LearningData.sh  
┃	    ┗━ delay_time.csv  
┗━ recv_script  

## Requirement

python3  
Quartus (Quartus Prime 17.0)  

## Usage (machine learning)

$ git clone https://github.com/shuji-oh/Divider  
$ cd machine_learning/prototype  
$ python3 knn.py  

## Author

[shuji-oh](https://github.com/shuji-oh)
