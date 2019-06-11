from __future__ import division

import numpy as np


def get_size_vgg_feat_map(input_W, input_H):
    output_W = input_W
    output_H = input_H
    for i in range(1,6):
        output_H = np.floor(output_H/2)
        output_W = np.floor(output_W/2)

    return output_W, output_H


def rmac_regions(W, H, L):

    ovr = 0.4 # desired overlap of neighboring regions
    steps = np.array([2, 3, 4, 5, 6, 7], dtype=np.float) # possible regions for the long dimension

    w = min(W,H)

    b = (max(H,W) - w)/(steps-1)
    idx = np.argmin(abs(((w ** 2 - w*b)/w ** 2)-ovr)) # steps(idx) regions for long dimension

    # region overplus per dimension
    Wd, Hd = 0, 0
    if H < W:
        Wd = idx + 1
    elif H > W:
        Hd = idx + 1

    regions = []

    for l in range(1,L+1):

        wl = np.floor(2*w/(l+1))
        wl2 = np.floor(wl/2 - 1)

        b = (W - wl) / (l + Wd - 1)
        if np.isnan(b): # for the first level
            b = 0
        cenW = np.floor(wl2 + np.arange(0,l+Wd)*b) - wl2 # center coordinates

        b = (H-wl)/(l+Hd-1)
        if np.isnan(b): # for the first level
            b = 0
        cenH = np.floor(wl2 + np.arange(0,l+Hd)*b) - wl2 # center coordinates

        for i_ in cenH:
            for j_ in cenW:
                # R = np.array([i_, j_, wl, wl], dtype=np.int)
                R = np.array([j_, i_, wl, wl], dtype=np.int)
                if not min(R[2:]):
                    continue

                regions.append(R)

    regions = np.asarray(regions)
    return regions
