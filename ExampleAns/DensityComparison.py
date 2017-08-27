
import numpy as np

def DensityCalc(p,m,b):

    r=np.ones(len(p))
    for i in range(len(m)):
        r[i]=np.sqrt(p[i,0]**2+p[i,1]**2+p[i,2]**2)

    d=np.ones(len(b))

    for i in range(len(b)-1):

        d[i]=np.sum(m[(r>b[i])&(r<b[i+1])])/(b[i]**3-b[i+1]**3)*3/4*np.pi

    return d


def DensityGood(positions,masses,bins):
    # Calculates the density of a set of particles, centred on the origin
    # with a set of given cartesian positions and masses.
    # The bin edges are given by bins

    if (type(masses)==float) or (type(masses)==int):
        masses=np.ones(len(positions))*masses

    if positions.ndim>1:
        # Calculate the radial positions of the particles
        radialPositions=np.sqrt(np.sum(positions**2,axis=1))
    else:
        radialPositions=positions


    # Calculate the volume of each bin
    volumes=(4.*np.pi/3.)*(bins[1:]**3-bins[:-1]**3)

    # Bin the radial data
    massesPerBin,bin_edges=np.histogram(
                                        radialPositions,
                                        bins=bins,
                                        weights=masses
                                        )

    densities=massesPerBin/volumes

    return densities


###############################
# Testing

import time

Npart=int(1e4)
pos=np.random.random(size=[Npart,3])
mass=np.ones(Npart)
bins=np.linspace(0.,1.,20)

t0=time.time()

densBad=DensityCalc(pos,mass,bins)

t1=time.time()

densGood=DensityGood(pos,mass,bins)

t2=time.time()

print 'Bad:  ',t1-t0
print 'Good: ',t2-t1
print 'Speed up: ',(t1-t0)/(t2-t1)