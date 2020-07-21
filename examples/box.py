from __future__ import absolute_import, division, print_function

import math
import time

import meshcat

vis = meshcat.Visualizer(zmq_url="tcp://127.0.0.1:6000")

box = meshcat.geometry.Box([0.5, 0.5, 0.5])
material = meshcat.geometry.MeshBasicMaterial(color=0xff0000)
vis.set_object(box, material)

draw_times = []

for i in range(200):
    theta = (i + 1) / 100 * 2 * math.pi
    now = time.time()
    vis.set_transform(meshcat.transformations.rotation_matrix(theta, [0, 0, 1]))
    draw_times.append(time.time() - now)
    time.sleep(0.01)

print(sum(draw_times) / len(draw_times))


