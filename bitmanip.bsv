package bitmanip;

/* This file is useful to include Debug statements 
   Usage: 
   logLevel(<name>, <verbosity_level>, $format("Intermediate step1: %d, step2: %d", step1_value, step2_value))
   The <name> field is better to be file name.
   The <verbosity_level> is better to be 0 for all debug statements to be printed. 

   NOTE: There is no semicolon at the end.
*/
`include "Logger.bsv" 

//This file does the BitManip computation and returns the result. 
`include "compute.bsv"

// This file has the structures being used.
// Any new structures or enum or union tagged can be included here.
import bbox_types :: *;

interface Ifc_bitmanip;
  method ActionValue#(BBoxOutput) mav_inputs(BBoxInput inp);
endinterface

(*synthesize*)
module mkbitmanip(Ifc_bitmanip);
    method ActionValue#(BBoxOutput) mav_inputs(BBoxInput inp);
      return fn_compute(inp);
    endmethod
endmodule: mkbitmanip

endpackage: bitmanip
