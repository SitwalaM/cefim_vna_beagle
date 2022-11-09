
This repo shows the code used for Receiver Calibration using [beaglebone black](https://beagleboard.org/black) and VectorStar MS4640A VNA.

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


# 3. Getting Instrument Name


# 4. Useful Documentation
