PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter
====

[Shuji Ohira, Araya Kibrom Desta, Ismail Arai, Kazutoshi Fujikawa, "PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks," In Proceedings of the 2021 ACM Asia Conference on Computer and Communications Security (ASIA CCS ’21), pp.1-11, June. 2021.]()

```
@inproceedings{ohira2020pli-tdc,
  title={PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks},
  author={Ohira, Shuji and Kibrom Desta, Araya and Arai, Ismail and Fujikawa, Kazutoshi},
  booktitle={Proceedings of the 2021 ACM Asia Conference on Computer and Communications Security},
  pages={1--11},
  year={2021},
  organization={ACM}
}
```

## Introduction

The code consists of three parts:  

1. Hardware source programs written by Verilog HDL for intel FPGA cyclone III and V.  
2. Machine learning scripts implemented by Python 3 and the Proof-of-Concept data.  
3. SPI receiver programs implemented by C for receiving the raw delay-time data.  

## Python Version

3.8.6  

## Quartus Version

Quartus Prime (v17.0.0 Lite Edition)  

## Usage (machine learning)

```
$ git clone https://github.com/shuji-oh/PLI_TDC_for_CAN  
$ cd PLI_TDC_for_CAN  
$ pip3 install -r requirements.txt  
$ cd machine_learning/prototype  
$ python3 rf.py  
```

## Author

[shuji-oh](https://github.com/shuji-oh)
