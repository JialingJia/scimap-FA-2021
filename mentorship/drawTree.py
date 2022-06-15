import numpy as np
import json
from pathlib import Path  
from math import cos, sin

SCALE = 1
CURL = 15

def rot(v, theta):
    theta = np.deg2rad(theta)
    mat = np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])
    return np.dot(mat, v)


def unfurl(X, base_vector=np.array([0, 1]), origin=np.array([0, 0]), depth=None, cdepth=0):
    vs = []

    if 'children' not in X:
        return []

    if depth is not None:
        if cdepth >= depth:
            return []

    girls = [c for c in X['children'] if c['gender'] == 'woman']
    boys = [c for c in X['children'] if c['gender'] == 'man']
    unknown = [c for c in X['children'] if c['gender'] == 'unknown']

    #print(origin, base_vector)

    #print(len(girls), len(boys))

    for ci, c in enumerate(girls):
        #new_v = rot( base_vector, -CURL * (ci+1) )# / len(girls) )
        new_v = rot(base_vector, -CURL * (ci+1) / len(girls))
        new_v = new_v * SCALE
        #print( np.power((new_v**2).sum(), 0.5) )

        vs.append((origin, origin+new_v, "#ff5f91", c["name"]))
        vs += unfurl(c, new_v, origin+new_v, depth, cdepth+1)

    for ci, c in enumerate(boys):
        #new_v = rot( base_vector, CURL * (ci+1) )# / len(boys) )
        new_v = rot(base_vector, CURL * (ci+1) / len(boys))
        new_v = new_v * SCALE
        #print( np.power((new_v**2).sum(), 0.5) )

        vs.append((origin, origin+new_v, "#73ffda", c["name"]))
        vs += unfurl(c, new_v, origin+new_v, depth, cdepth+1)

    for ci, c in enumerate(unknown):
        #new_v = rot( base_vector, CURL * (ci+1) )# / len(boys) )
        new_v = rot(base_vector, 0)
        new_v = new_v * SCALE
        #print( np.power((new_v**2).sum(), 0.5) )

        vs.append((origin, origin+new_v, "grey",  c["name"]))
        vs += unfurl(c, new_v, origin+new_v, depth, cdepth+1)

    return vs
