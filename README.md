# BitManip Extension project

Students are required to read through the Bit Manipulation Spec by RISC-V and implement it in **Bluespec** and verify it using **cocotb**. The spec pdf is present in docs/bitmanip-1.0.0-38-g865e7a7.pdf .

### The repo structure is as follows:
- bbox.bsv - The top module of the design. Has the interface definition and module definition which calls the BitManip calculation.
- src/ - The directory where the files which the student should edit are present here. The files present are
	- compute.bsv - The top function which selects between the functions implemented for the spec depending on the instruction.
	- bbox.defines - The function which has the macro definition used to select between the instructions.
	- bbox_types.bsv - The structures, enum, bsc macors are defined here.
	- Zbb.bsv - A sample implementation of ANDN instruction is present. It is needed to be completed with all the other required instructions.
- bbox_verif/ - The directory where the scripts required for running the cocotb tests are present. The files present are:
	- test_bbox.py - 
	- bbox_ref_model.py - 
- docs/ - The directory where the bitmanip spec pdf and instructions for Tool Setup are mentioned.

### Steps to run:
Make sure you have installed all the required tools as mentioned in docs/Tool_setup.pdf and the python environment is activated.

1. To just generate the verilog
```bash
$ make generate_verilog
```
2. To simulate. NOTE: Does both generate_verilog and simulate.
```bash
$ make simulate
```
3. To clean the build.
```bash
$ make clean_build
```
