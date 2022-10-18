/****** Imports *******/
`include "bbox.defines"
import bbox_types :: *;
`include "Zbb.bsv"
/*********************/

function BBoxOutput fn_compute(BBoxInput inp);
  Bit#(XLEN) result;
  Bool valid;
  case(inp.instr) matches
    `ANDN: begin
      result = fn_andn(inp.rs1, inp.rs2);
      valid = True;
    end
    default: begin
      result = 0;
      valid = False;
    end
  endcase
  return BBoxOutput{valid: valid, data: result};
endfunction
