import itertools
import itertools
import Adafruit_BBIO.GPIO as GPIO


class PinStates:

    def __init__(self, n, list_pins,full_pin_list):
      self.n = n
      self.list_pins = list_pins
      self.full_pin_list = full_pin_list


    def get_drive_bits(self):
      """returns integer in 6 bits binary"""
      
      data = bin(self.n).replace("0b", "")
      padding_n = 6 - len(data)
      pad = list(itertools.repeat("0", padding_n))# pad to 6 bits

      padded = ""
      for i in range(0,len(pad)):
        padded = padded+pad[i]

      return padded + data
        
    def get_pin_dictionary(self):
      """returns dictionary of pin digits to write"""

      padded_data = self.get_drive_bits()[::-1]
      output = {}
      for i,pin in enumerate(self.list_pins):
        output[pin] = padded_data[i]

      return output

    def get_full_pin_states(self):
      """ returns dictionary for the full pins (10 bits) """

      pin_dictionary = self.get_pin_dictionary()
      for i in range(2,6):

        pin = self.list_pins[i]
        value = pin_dictionary[pin]
        inv_value = abs(int(value) -1)
        index_in_full = self.full_pin_list.index(pin)
        inv_pin = self.full_pin_list[index_in_full-1]

        pin_dictionary[inv_pin] = inv_value

      # change strings to ints
      pin_dictionary= dict([a, int(x)] for a, x in pin_dictionary.items())

      return  pin_dictionary 



def drive_attenuator(int_setting, attenuator_number):

  attenuator_pins = []
  if attenuator_number == 1:

    for number in range(3,23,2):
      pin = "P8"
      attenuator_pins.append(pin+"_{}".format(number))
  else:
    for number in range(4,24,2):
      pin = "P8"
      attenuator_pins.append(pin+"_{}".format(number))

  attenuator_subset = list(itertools.compress(attenuator_pins,[1,1,0,1,0,1,0,1,0,1]))
  pin_states = PinStates(int_setting, attenuator_subset,  attenuator_pins)

  for pin in pin_states.get_full_pin_states():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, pin_states.get_full_pin_states()[pin])

  return pin_states.get_full_pin_states()
