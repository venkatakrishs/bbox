
#Reference model

def bitmanip_rm(instr, rs1, rs2):
    if instr == 1:
        res = rs1 & ~rs2
        result = '{:064b}'.format(res)
        return '1'+result

