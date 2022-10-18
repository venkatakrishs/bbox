import string
import random
import cocotb
import logging as _log
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.binary import BinaryValue
from cocotb.clock import Clock

from bitmanip_ref_model import bitmanip_rm

#// Ports:
#// Name                         I/O  size props
#// bbox_out                       O    65
#// CLK                            I     1 unused
#// RST_N                          I     1 unused
#// instr                          I    32
#// rs1                            I    64
#// rs2                            I    64
#//
#// Combinational paths from inputs to outputs:
#//   (instr, rs1, rs2) -> bbox_out

'''
#Reference model
def bitmanip_rm(instr, rs1, rs2):
    if instr == 1:
        res = rs1 & ~rs2
        result = '{:064b}'.format(res)
        return '1'+result
'''
#generates clock and reset
async def initial_setup(dut):
	cocotb.start_soon(Clock(dut.CLK, 1, units='ns').start())
        
	dut.RST_N.value = 0
	await RisingEdge(dut.CLK)
	await RisingEdge(dut.CLK)
	dut.RST_N.value = 1


#drives input data to dut
async def input_driver(dut, instr, rs1, rs2):
    await RisingEdge(dut.CLK)
    dut.instr.value = instr
    dut.rs1.value = rs1
    dut.rs2.value = rs2
    await RisingEdge(dut.CLK)
    dut._log.info("---------------- DUT Input Info -----------------------")
    dut._log.info("instr = %s  rs1 = %s rs2 = %s",hex(dut.instr.value), hex(dut.rs1.value), hex(dut.rs2.value))
    dut._log.info("-------------------------------------------------------")
#monitors dut output
async def output_monitor(dut):
    while True:
        #print(dut.instr.value, dut.rs1.value, dut.rs2.value)
        await RisingEdge(dut.CLK)
        if(dut.bbox_out.value[0]): break

    dut_result = dut.bbox_out.value
    return dut_result

#compares output of dut and rm
async def scoreboard(dut, dut_result, rm_result):
    dut._log.info("------------ Compare DUT o/p & Ref Model o/p ----------")
    dut._log.info("Expected output  = %s", rm_result)
    dut._log.info("DUT output       = %s", dut_result)
    assert rm_result == str(dut_result),"Failed"
    dut._log.info("-------------------------------------------------------")


#testbench 
async def TB(dut, instr, rs1, rs2):
    rm_result = bitmanip_rm(instr, rs1, rs2)
    
    await input_driver(dut, instr, rs1, rs2)
    dut_result = await output_monitor(dut)
    
    await scoreboard(dut, dut_result, rm_result)	

#test vectors
@cocotb.test()
async def test_addn(dut):
    await initial_setup(dut)
    for i in range (10):
        instr = 1
        rs1 = random.randint(0,2**64) 
        rs2 = random.randint(0,2**64)
        await TB(dut, instr, rs1, rs2)
@cocotb.test()
async def test_addn_2(dut):

    await initial_setup(dut)
    instr = 1
    rs1 = 0x1111
    rs2 = 0x1011
    await TB(dut, instr, rs1, rs2)

