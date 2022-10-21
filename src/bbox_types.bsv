package bbox_types;

`ifdef RV64
   typedef 64 XLEN;
   typedef 32 XLEN_BY_2;
`else
   typedef 32 XLEN;
`endif

typedef struct {
  Bit#(32) instr;
  Bit#(XLEN) rs1;
  Bit#(XLEN) rs2;
} BBoxInput deriving (Bits, Eq, FShow);

typedef struct {
  Bool valid;
  Bit#(XLEN) data;
} BBoxOutput deriving (Bits, Eq, FShow);

endpackage: bbox_types
