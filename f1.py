def  narx_chegirma(narx, foiz):
    return narx - (narx*foiz/100)

print(narx_chegirma(100000,20))