

SIM ?= verilator
TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)


ifeq ($(TOPLEVEL_LANG),verilog)
  VERILOG_SOURCES =$(PWD)/../verilog/mkbitmanip.v
else
  $(error "A valid value (verilog) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

EXTRA_ARGS = --trace --trace-structs

TOPLEVEL := mkbitmanip
MODULE   := test_bitmanip

include $(shell cocotb-config --makefiles)/Makefile.sim



