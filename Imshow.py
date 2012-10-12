from pylab import figure
from matplotlib import pyplot
from scipy import zeros
from pylab import *
numberOfTimeSteps = 100
summ = zeros((numberOfTimeSteps,100,100))
##figure()
##pyplot.imshow(summ,interpolation='nearest')
##pyplot.show()
for i in range(len(summ)):
    summ[i][i] = 1
    pyplot.imshow(summ[i],interpolation='nearest')
    filename = str('test_img%d' % i) + '.png'
    savefig(filename, dpi=100)
    print 'Wrote file', filename
    clf()
