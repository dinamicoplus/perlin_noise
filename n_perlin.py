import matplotlib.pyplot as plt
import math,random as r
import numpy as np

F = plt.figure(1, (5.5, 3.5))

def linear_interpolate(x1,y1,x2,y2,x):
	return float(float(x-x1)*float(y2-y1)/(x2-x1))+y1

def perlin_octave(frequency, amplitude, length):
	print "----------------------"
	print "- frequency: ",frequency
	print "- amplitude: ",amplitude
	print "- length: ",length
	print "----------------------"

	wave = np.zeros(length,dtype=np.float32)
	step_length=int(math.floor(length/frequency))
	for i in xrange(0,length,step_length):
		wave[i]=(amplitude/2)-(r.random()*amplitude)
		print i, ", ", wave[i]
		if i>=step_length:
			for j in xrange(i-(step_length-1),i):
				x1 = i-(step_length)
				x2 = i
				wave[j]=linear_interpolate(x1,wave[x1],x2,wave[x2],j)
	last=length-1
	wave[last] = (amplitude/2)-(r.random()*amplitude)
	for i in xrange(last-(step_length-1),last):
		x1=last-(step_length)
		x2=last
		wave[i]=linear_interpolate(x1,wave[x1],x2,wave[x2],i)
	return wave
lenght=256
n_octaves=9
perlin_wave = np.zeros(lenght)
for i in range(1,n_octaves):
	current_pow=math.pow(2,i)
	octave=perlin_octave(current_pow,lenght/current_pow,lenght)
	for j in range(perlin_wave.size):
		perlin_wave[j]+=octave[j]
	
x = np.arange(0,256)
y = perlin_wave
plt.plot(x,y)
plt.draw()
plt.show()
