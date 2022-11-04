# list connections using pyvisa
import pyvisa
import itertools
from drive_module import *
import Adafruit_BBIO.GPIO as GPIO

# connection
rm = pyvisa.ResourceManager()
print(rm.list_resources())
inst = rm.open_resource('TCPIP0::10.0.0.2::5001::SOCKET')

# Initialize
inst.read_termination = "\n"
inst.write_termination = "\n"
inst.timeout = 500

# print instrument IDN
#print(inst.query("*IDN?"))

output = drive_attenuator(1,1)
print(output)


# check number of active traces
print(inst.query(":CALC1:PAR:COUN?"))


# write csvs of first trace
states = list(itertools.product(range(64),range(64)))

port = "USB"
freq=29
input ="LSB"
for state in states[:5]:
  atten_1 = state[0]
  atten_2 = state[1]

  drive_attenuator(atten_1,1)
  drive_attenuator(atten_1,2)
  print("#######"+"state" + str(state) + "Configured" + "#######")
  time.sleep(2)

  print("########### Waiting to Write File#######")
  file_name = "Port="+port+"_LO="+str(freq)+"_atten_1="+ str(atten_1) + "_atten_2="+ str(atten_2)+ "_input=" + input + ".csv"

  # write csv of first trace
  inst.write(":MMEM:STOR:MDATA 'C:\sitwala\ '+ file_name")

  print("######### " + file_name + " has been saved" + "#########")

  GPIO.cleanup()
