# etherpad: http://j.mp/uct_swc_0715_2
# code: http://j.mp/swcplot

import glob
import numpy
import matplotlib.pyplot

filename_list = glob.glob('data/inf*.csv')

for input_filename in filenames_list:
  data = numpy.loadtxt(fname=input_filename, delimiter=',')
  
  fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
  
  axes1 = fig.add_subplot(1, 3, 1)
  axes2 = fig.add_subplot(1, 3, 2)
  axes3 = fig.add_subplot(1, 3, 3)
  
  axes1.set_ylabel('average')
  axes1.plot(data.mean(axis=0))
  
  axes2.set_ylabel('max')
  axes2.plot(data.max(axis=0))
  
  axes3.set_ylabel('min')
  axes3.plot(data.min(axis=0))
  
  fig.tight_layout()
  
  matplotlib.pyplot.show(fig)
