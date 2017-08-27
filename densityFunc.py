
import numpy as np
# Function to calculate the density of a collection of particles

def DensityCalc(p,m,b):

    r=np.ones(len(p))
    for i in range(len(m)):
        r[i]=np.sqrt(p[i,0]**2+p[i,1]**2+p[i,2]**2)

    d=np.ones(len(b))

    for i in range(len(b)-1):

        d[i]=np.sum(m[(r>b[i])&(r<b[i+1])])/(b[i]**3-b[i+1]**3)*3/4*np.pi

    return d


# Example input
Npart=int(1e4)
pos=np.random.random(size=[Npart,3])
mass=np.ones(Npart)
bins=np.linspace(0.,1.,20)

# Run the function
density=DensityCalc(pos,mass,bins)

# Example test
def test_numbers_3_4():
    assert 3*4 == 12 