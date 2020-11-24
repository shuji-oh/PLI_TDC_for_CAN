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

This repository publishes the source code of the sender identification method based on delay-time using Time-to-Digital Converter for automotive network security. You will be able to find the detailed theory and design in our paper after the ASIACCS'21 conference (June 7-11, 2021).  

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

## Usage (SPI receiver)

```
$ git clone https://github.com/shuji-oh/PLI_TDC_for_CAN  
$ cd PLI_TDC_for_CAN/recv_script  
$ ./build.sh  
$ ./tdc_recv --speed 4000000  
```

## How to compile and configure the verilog HDL programs

At first, please install and run the Quartus Prime on your workstation. Besides, please set up the connectivity from hardware (FPGA) and your workstation in advance. And, after downloading this repository, please perform the following procedures in the Quartus app.  

### Compile  
[File menu] ⇒ [Open Project...] ⇒ [Select `PLI_TDC_for_CAN/hardware/intel_cyclone_5/PLI_TDC.qpf`] ⇒ [Start Compilation]  

### Configure
After above compilation, please transmit the circuit information to the FPGA.  
[Programmer] ⇒ [Start button in the Programmer Window]

## Author

[shuji-oh](https://github.com/shuji-oh)
