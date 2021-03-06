from pandaboxlib import PandA
import numpy as np 

host = 'pandabox'

panda = PandA(host)
panda.connect_to_panda()

panda.query('CLOCKS.A_PERIOD=.05')
panda.query('CLOCKS.A_PERIOD.UNITS=s')

panda.query('PGEN1.TRIG=CLOCKS.OUTA')
panda.query('PGEN1.CYCLES=1')

num_pts = 1001
pos_i = 0
pos_f = 1000
pos = np.linspace(pos_i, pos_f, num=num_pts)

pos_cmd = ['%d\n' % p for p in pos]
print pos_cmd

panda.query('PGEN1.TABLE<\n'+''.join(pos_cmd))
panda.query('PCOMP1.INP=PGEN1.OUT')
panda.query('PCOMP1.START=10')

step_size = 10 
pnum = (pos_f - pos_i) / step_size
print 'pnum: ', pnum

panda.query('PCOMP1.PRE_START=-1')
panda.query('PCOMP1.STEP=%d' % (step_size))
panda.query('PCOMP1.PULSES=%d' % (pnum))
panda.query('PCOMP1.WIDTH=1')
panda.query('PCOMP1.RELATIVE=Absolute')
panda.query('PCOMP1.DIR=Positive')

panda.query('TTLOUT1.VAL=PCOMP1.OUT')


panda.query('PCOMP1.ENABLE=ZERO')
panda.query('PCOMP1.ENABLE=ONE')
panda.query('PGEN1.ENABLE=ONE')
panda.query('COUNTER1.ENABLE=ZERO')
panda.query('COUNTER1.ENABLE=ONE')

