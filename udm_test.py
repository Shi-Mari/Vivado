# -*- coding:utf-8 -*-
#from __future__ import division

import math
import udm
from udm import *

def sin_hw(x):
    
    div6 = 0x2a
    div120 = 0x02
    term0 = x
    
    # stage 0
    pow2 = (x * x) >> 8

    # stage 1
    pow3 = (pow2 * x) >> 8

    # stage 2
    term1 = (pow3 * div6) >> 8
    pow5 = (pow2 * pow3) >> 8

    # stage 3
    term2 = (pow5 * div120) >> 8
    term0_minus_term1 = term0 - term1

    # stage 4
    y = term0_minus_term1 + term2
    return y

#generating test stimulus

udm = udm('COM12', 921600)
print("")

CSR_LED_ADDR    = 0x00000000
CSR_SW_ADDR     = 0x00000004
TESTMEM_ADDR    = 0x80000000
TAILOR_ADDR     = 0x00000008

for index in range(0, 804, 134):
    udm.wr32(TAILOR_ADDR, index)
    print("Got read: ", (udm.rd32(TAILOR_ADDR))/256)
    print("Expected read: ", (sin_hw(index)/256))
    if (udm.rd32(TAILOR_ADDR) == sin_hw(index)):
        print("RIGHT")
    else:
        print("ERROR")

udm.disconnect()

