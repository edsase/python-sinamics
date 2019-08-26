# Libraries in Main/ folder.
import sinamics
from sinamics_graph import graph


# Defining g120 as object of Sinamics class.
g120 = sinamics.Sinamics()

# Connecting.
g120.connect('192.168.0.14')

# Checking request time.
print("Time for a S7 request: ", g120.get_req_time())

# Reading link DC value.
print("Link DC value is: ", g120.read_parameter(26, 'f'))

# Setting ON/Off1 source as DI0 and setpoint source as AI0.
g120.write_parameter(840, '722.0', 'I/B')
g120.write_parameter(1070, '755.0', 'I/B')

# Getting a trace of inverter speed (r0021) and current (r0027)
# filttered values.
param_array = [[21, 'f'], [27, 'f']]
graph_time = 10000
graph(g120, param_array, graph_time, medfilt=True,
      save=True, filepath='/home/ggjm/Desktop/graph1.jpg')

# Returning inverter to factory defaults.
g120.write_parameter(10, 30, 'h')
g120.write_parameter(970, 1, 'H')

# New comissioning.
g120.write_parameter(10, 1, 'h')
g120.write_parameter(15, 12, 'I') # macro 15.
# {
#    Insert write_parameter calls with p0010 = 1
#    to motor nameplate data and etc.
# }

# Destroying object created:
g120.destroy()
