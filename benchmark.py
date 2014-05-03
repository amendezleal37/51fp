from time import time

def mean(array):
	number = 0
	for k in xrange(len(array)):
		number+=array[k]
	number=number/len(array)
	return number


def benchmark(fun,runs):
    init=[0]*runs
    end=[0]*runs
    runtime=[0]*runs
    for k in xrange(runs):
        init[k]=time()
        fun
        end[k]=time()
        runtime[k]=end[k]-init[k]
    return mean(runtime)
    