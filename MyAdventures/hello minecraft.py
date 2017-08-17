import mcpi.minecraft as minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

bridge = []

def buildBridge():
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x,pos.y-1,pos.z)
    if b == block.AIR.id or b == block.WATER_FLOWING.id or b == block.WATER_STATIONARY.id:
        mc.setBlock(pos.x,pos.y-1,pos.z,block.GLASS.id)
        coordinate = [pos.x,pos.y-1,pos.z]
        bridge.append(coordinate)

    elif b != block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0],coordinate[1],coordinate[2],block.AIR.id)
            time.sleep(0.25)

while True:
    time.sleep(0.25)
    buildBridge()
mc = minecraft.Minecraft.create()

mc.postToChat("Hello Minecraft World")

import time

while(1):
    pos = mc.player.getTilePos()

    print(pos.x)
    print(pos.y)
    print(pos.z)

    from led import *

    if pos.y > 5:
        green_led(1)
    else:
        green_led(0)

    time.sleep(5)
