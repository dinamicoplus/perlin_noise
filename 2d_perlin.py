import matplotlib.pyplot as plt
import math,random as r
import numpy as np

def bilinear_interpolate(x1,y1,x2,y2,v1,v2,v3,v4,tx,ty):
	area_v1=math.fabs((tx-x1)*(ty-y1))*v4
	area_v2=math.fabs((tx-x2)*(ty-y1))*v3
	area_v3=math.fabs((tx-x1)*(ty-y2))*v2
	area_v4=math.fabs((tx-x2)*(ty-y2))*v1

	area_total=(x2-x1)*(y2-y1)
	return (area_v1+area_v2+area_v3+area_v4)/area_total

def perlin_octave_2D(frequency, amplitude, length):
	print "----------------------"
        print "- frequency: ",frequency
        print "- amplitude: ",amplitude
        print "- length: ",length
        print "----------------------"

	wave = np.zeros([length+1,length+1],dtype=np.float32)
	step_length=int(math.floor(length/frequency))
	for i in xrange(0,length+1,step_length):
		for j in xrange(0,length+1,step_length):
			wave[i][j]=(amplitude/2)-(r.random()*amplitude)
#			print i,",",j,": ", wave[i][j]
			if i>=step_length and j>=step_length:
				for a in xrange(i-(step_length),i):
					for b in xrange(j-(step_length),j):
						x1=i-(step_length)
						x2=i
						y1=j-(step_length)
						y2=j
						wave[a][b]=bilinear_interpolate(x1,y1,x2,y2,wave[x1][y1],wave[x2][y1],wave[x1][y2],wave[x2][y2],a,b)
#	print wave
	return wave

length=256
final_wave= np.zeros([length+1,length+1])
for i in range(8):
	current_pow=math.pow(2,i)
	octave=perlin_octave_2D(current_pow,length/current_pow,length)
	final_wave+=octave
plt.imshow(final_wave)
plt.draw()
plt.show()
