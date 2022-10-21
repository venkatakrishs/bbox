import string
import random
import cocotb
import logging as _log
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.regression import TestFactory

from bitmanip_ref_model import bitmanip_rm

#// DUT Ports:
#// Name                         I/O  size 
#// bbox_out                       O    65/33
#// CLK                            I     1 
#// RST_N                          I     1 
#// instr                          I    32
#// rs1                            I    64/32
#// rs2                            I    64/32
#//   (instr, rs1, rs2) -> bbox_out


#generates clock and reset
async def initial_setup(dut):
	cocotb.start_soon(Clock(dut.CLK, 1, units='ns').start())
        
	dut.RST_N.value = 0
	await RisingEdge(dut.CLK)
	dut.RST_N.value = 1


#drives input data to dut
async def input_driver(dut, instr, rs1, rs2, single_opd):
    await RisingEdge(dut.CLK)
    dut.instr.value = instr
    dut.rs1.value = rs1
    dut._log.info("---------------- DUT Input Info -----------------------")
    if single_opd == 1:
        await RisingEdge(dut.CLK)
        dut._log.info("instr = %s  rs1 = %s ",hex(dut.instr.value), hex(dut.rs1.value))

    else :
        dut.rs2.value = rs2
        await RisingEdge(dut.CLK)
        dut._log.info("instr = %s  rs1 = %s rs2 = %s",hex(dut.instr.value), hex(dut.rs1.value), hex(dut.rs2.value))
    dut._log.info("-------------------------------------------------------")

#monitors dut output
async def output_monitor(dut):
    while True:
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

#Testbench
async def TB(dut, XLEN, instr, instr_name, single_opd, num_of_tests):
    await initial_setup(dut)
    dut._log.info("*******************************************************")
    dut._log.info("------------- Test %r of RV%d starts --------------" %(instr_name,XLEN))
    dut._log.info("*******************************************************")
    for i in range (num_of_tests):
        rs1 = random.randint(0,(2**XLEN)-1) 
        rs2 = random.randint(0,(2**XLEN)-1)
        rm_result = bitmanip_rm(instr, rs1, rs2, XLEN)
    
        await input_driver(dut, instr, rs1, rs2, single_opd)
        dut_result = await output_monitor(dut)
    
        await scoreboard(dut, dut_result, rm_result)	
    dut._log.info("*******************************************************")
    dut._log.info("------------- Test %r of RV%d ends ----------------" %(instr_name,XLEN))
    dut._log.info("*******************************************************")


# generates sets of tests based on the different permutations of the possible arguments to the test function
tf = TestFactory(TB)

base = 'RV64'

if base == 'RV32':
    tf.add_option('XLEN', [32])
    tf.add_option(('instr','instr_name','single_opd'), [(1, 'addn', 0)])
    ##To run multiple instr - tf.add_option(((('instr','instr_name','single_opd'), [(1, 'addn', 0),(2,'clz',1),(...)])

elif base == 'RV64':
    tf.add_option('XLEN', [64])
    tf.add_option(('instr','instr_name','single_opd'), [(1, 'addn', 0)])
    ##To run multiple instr - tf.add_option(((('instr','instr_name','single_opd'), [(1, 'addn', 0),(2,'clz',1),(...)])

tf.add_option('num_of_tests',[10])
tf.generate_tests()
