#!python
import json
import numpy as np

with open('SPARC_public_simple.json','r') as fid:
    SPARC_geom = json.load(fid)
inner_vv = np.array(SPARC_geom['vv']['inner']['pts'])
outer_vv = np.array(SPARC_geom['vv']['outer']['pts'])

cubit.cmd('reset')
cubit.cmd('undo off')

pts_inner = 0
for i in range(0,inner_vv.shape[0]-1):
    cubit.cmd("create vertex location {0} 0.0 {1}".format(inner_vv[i,0],inner_vv[i,1]))
    pts_inner += 1

pts_outer = 0
for i in range(0,outer_vv.shape[0]-1):
    cubit.cmd("create vertex location {0} 0.0 {1}".format(outer_vv[i,0],outer_vv[i,1]))
    pts_outer += 1

offset = 0
cubit.cmd("create Curve spline location vertex {0} to {1} {2} delete".format(offset+1,offset+pts_inner,offset+1))

offset += pts_inner
cubit.cmd("create Curve spline location vertex {0} to {1} {2} delete".format(offset+1,offset+pts_outer,offset+1))

cubit.cmd("sweep curve all zaxis angle 360")

cubit.cmd("brick x 0.7 y 4 z 1.0")
cubit.cmd("move Volume 3  x 0 y 4.0 z 0.0 include_merged")
cubit.cmd("modify curve 13 11 7 9 blend radius .1")
cubit.cmd('Volume 3 copy rotate 20 about z repeat 17')
cubit.cmd('subtract body 3 to 21 from body 1 2 ')

cubit.cmd("set trimesher coarse off")
cubit.cmd("set trimesher geometry sizing off")
cubit.cmd("surface all scheme trimesh")
cubit.cmd("surface all size 0.1")
cubit.cmd("mesh surface all")

cubit.cmd("set duplicate block elements off")
cubit.cmd("block 1 add surface in body 1")
cubit.cmd("block 2 add surface in body 2")

cubit.cmd("set large exodus file on")
cubit.cmd('export Genesis "SPARC_public-ThinCurr_approx.g" overwrite block all')

