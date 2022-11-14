
This repo shows the code used for Receiver Calibration using [beaglebone black (BBB)](https://beagleboard.org/black) and VectorStar MS4640A VNA.

<div align="center">
  
| File | Description |
|---|---|
| [drive_module.py](https://github.com/SitwalaM/cefim_vna_beagle/blob/main/scripts/drive_module.py) | Main modules that are used to drive the GPIOs|
| [test_vna.py](https://github.com/SitwalaM/cefim_vna_beagle/blob/main/scripts/test_vna.py) | main script that drives digital attenuators from GPIO and saves trace on VNA for each state|
|[led_blink.py](https://github.com/SitwalaM/cefim_vna_beagle/blob/main/scripts/led_blink.py)  | example code to blink LEDs on beaglebone |
  
</div>

# 1. PyViSA

The core of communicating with intruments using Standard Commands for Programmable Instruments(SCPI) using python is the python package [PyVISA](https://pyvisa.readthedocs.io/en/latest/introduction/getting.html). To be able to run PyVISA on the beaglebone black, you will have to remove all unneccesary installations that come with the board like Cloud9 IDE to make space available. Install required python packages using the following command;

```bash
  pip install -r requirements.txt 
```

# 2. Networking Setup for VNA and Board

In this application, the BBB is connected to the VNA via ethernet LAN port. You will have to set the IP address on both the VNA and the BBB to be able to communicate. The VNA IP address is setup as follows: MAIN | System | SYSTEM | Netwk Interface | NETWORK INTERFACE . Further instructions on setting up the IP on the VNA can be found [here](https://dl.cdn-anritsu.com/en-us/test-measurement/ohs/10450-00008L-MS4640A-VectorStar-HELP/index.html#page/Programming_Commands%2FPM_Ch1_GeneralInfo.02.5.html%23).

Similarly, you will have to setup a static IP on the BBB using instructions [here](https://subscription.packtpub.com/book/iot-&-hardware/9781784390204/2/ch02lvl1sec12/setting-up-a-static-ip-on-the-beaglebone). Make sure the IPs on the VNA and the BBB are on the same networks. You can test connectivity by pinging the VNA.


# 3. Getting Instrument Name


# 4. Useful Documentation
