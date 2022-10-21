TOPFILE=bbox.bsv
BSVINCDIR=.:%/Libraries:./src
BSCDEFINES=RV64
VERILOGDIR=verilog/
BUILDDIR=intermediate/

default: generate_verilog

.PHONY: generate_verilog
generate_verilog:
	@mkdir -p $(VERILOGDIR) $(BUILDDIR)
	@bsc -u -verilog -elab -vdir ./verilog -bdir ./intermediate -info-dir ./intermediate +RTS -K40000M -RTS -check-assert  -keep-fires -opt-undetermined-vals -remove-false-rules -remove-empty-rules -remove-starved-rules -remove-dollar -unspecified-to X -show-schedule -show-module-use  -suppress-warnings G0010:T0054:G0020:G0024:G0023:G0096:G0036:G0117:G0015 -D $(BSCDEFINES) -p $(BSVINCDIR) $(TOPFILE)

.PHONY: clean
clean:
	@rm -rf $(VERILOGDIR) $(BUILDDIR)
	@echo "Cleaned"
