
#Reference model
# if instr has single operand, take rs1 as operand
def bbox_rm(instr, rs1, rs2, XLEN):
    valid = '0'
    if instr == 1:
        res = rs1 & ~rs2
        valid = '1'
    ##elif instr == 2:

    

    if XLEN == 32:
        result = '{:032b}'.format(res)
    elif XLEN == 64:
        result = '{:064b}'.format(res)


    return valid+result

