# etherpad: http://j.mp/uct_swc_0715_2
# code: http://j.mp/swcplot

import sys
import numpy
import matplotlib.pyplot

if len(sys.argv) != 2:
  sys.exit("Expected the name of a data file to plot.")
input_filename = sys.argv[0]

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
