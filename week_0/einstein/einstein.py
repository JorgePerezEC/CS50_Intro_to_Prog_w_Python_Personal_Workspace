def Energy_frm(m = 0):
    c = 300000000
    E = m * pow(c,2)
    return E

masa = int(input("m: "))
print(f"E: {Energy_frm(masa)}")
