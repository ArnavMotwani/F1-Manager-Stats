def outputs(i):
    name = "A" + str(i + 2)
    lvl = "B" + str(i + 2)
    ot = "C" + str(i + 2)
    df = "D" + str(i + 2)
    cn = "E" + str(i + 2)
    fm = "F" + str(i + 2)
    tm = "G" + str(i + 2)
    wm = "H" + str(i + 2)
    return name, lvl, ot, df, cn, fm, tm, wm


def inputs(row):
    cellN = "A" + str(row)
    cellL = "C" + str(row)
    cellO = "D" + str(row)
    cellD = "E" + str(row)
    cellC = "F" + str(row)
    cellF = "G" + str(row)
    cellT = "H" + str(row)
    cellW = "I" + str(row)

    return cellN, cellL, cellO, cellD, cellC, cellF, cellT, cellW
