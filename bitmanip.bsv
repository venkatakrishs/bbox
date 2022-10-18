package bitmanip;

/* INCLUDE: Logger.bsv
   This file is useful to include Debug statements 
   Usage: 
   logLevel(<name>, <verbosity_level>, $format("Intermediate step1: %d, step2: %d", step1_value, step2_value))
   The <name> field is better to be file name.
   The <verbosity_level> is better to be 0 for all debug statements to be printed. 

   While simulation, to print the debug statements need to include some statements like below in the sim executable:
   ./out +m<name> +l<verbosity_level>

   NOTE: There is no semicolon at the end.
*/
`include "Logger.bsv" 

//This file does the BitManip computation and returns the result. 
`include "compute.bsv"

// This file has the structures being used.
// Any new structures or enum or union tagged can be included here.
import bbox_types :: *;

interface Ifc_bitmanip;
  (*result = "bbox_out"*)
  (*prefix = ""*)
  (*always_ready, always_enabled*)
  method ActionValue#(BBoxOutput) mav_inputs(Bit#(32) instr, Bit#(XLEN) rs1, Bit#(XLEN) rs2);
endinterface

(*synthesize*)
module mkbitmanip(Ifc_bitmanip);
    method ActionValue#(BBoxOutput) mav_inputs(Bit#(32) instr, Bit#(XLEN) rs1, Bit#(XLEN) rs2);
      let bbox_inp = BBoxInput { instr : instr,
                                 rs1   : rs1,
                                 rs2   : rs2
                               };
      return fn_compute(bbox_inp);
    endmethod
endmodule: mkbitmanip

endpackage: bitmanip
