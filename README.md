PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter
====

[Shuji Ohira, Araya Kibrom Desta, Ismail Arai, Kazutoshi Fujikawa, "PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks," In Proceedings of the 2021 ACM Asia Conference on Computer and Communications Security (ASIA CCS ’21), pp.176–186, June. 2021.](https://doi.org/10.1145/3433210.3437530)

```
@inproceedings{ohira2021pli-tdc,
  title={PLI-TDC: Super Fine Delay-Time Based Physical-Layer Identification with Time-to-Digital Converter for In-Vehicle Networks},
  author={Ohira, Shuji and Kibrom Desta, Araya and Arai, Ismail and Fujikawa, Kazutoshi},
  booktitle={Proceedings of the ACM Asia Conference on Computer and Communications Security (ASIACCS)},
  pages={176--186},
  year={2021},
  doi={10.1145/3433210.3437530},
  organization={ACM}
}
```

## Introduction

This repository publishes the source code of the sender identification method based on delay-time using Time-to-Digital Converter for automotive network security. You will be able to find the detailed theory and design in our paper after the ASIACCS'21 conference (June 7-11, 2021).  

The code consists of three parts:  

1. Hardware source programs written by Verilog HDL for intel DE0-CV Cyclone V FPGA.  
2. Machine learning scripts implemented by Python 3 and the Proof-of-Concept data.  
3. SPI receiver programs implemented by C for receiving the raw delay-time data.  

## Python Version

3.8.6 or later  

## Quartus Version

Quartus Prime Lite Edition (v17.0.0 or later)  

## Required Hardware  

* Intel DE0-CV Cyclone V Board  
* Raspberry Pi Model B or B+  
* temperature sensor (DS18B20)  
* CAN transciever (mcp2551)  

According to the our Quartus Prime Settings File ([`PLI_TDC_for_CAN/hardware/intel_cyclone_5/PLI_TDC.qsf`](https://github.com/shuji-oh/PLI_TDC_for_CAN/blob/master/hardware/intel_cyclone_5/PLI_TDC.qsf)), you can set up the wiring as the following figure.  

<img src="https://user-images.githubusercontent.com/27995559/100208862-87f60780-2f4c-11eb-85bd-4a7d4bf1d2eb.png" width="600px">

DS18B20 resistor: 4.7K Ohm or 10K Ohm resistor

## Usage (machine learning)

```
$ git clone https://github.com/shuji-oh/PLI_TDC_for_CAN  
$ cd PLI_TDC_for_CAN  
$ pip3 install -r requirements.txt  
$ cd machine_learning/prototype  
$ python3 rf.py  
```

## Usage (SPI receiver)
Our method employs the temperature characteristic as one of the features to be robust in the temperature concept drift. So, please set up the raspberry pi model B or B+ and DS18B20 temperature sensor based on [some articles](https://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/). After the setting, you can build and execute the SPI receiver program on your raspberry pi.

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
