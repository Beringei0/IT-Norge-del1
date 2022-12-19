import wmi
w = wmi.WMI()
for p in w.Win32_Product():
    print( r"\newcommand*{\Title}", "{" + p.Version +"}")
    print( r"\newcommand*{\Title}", "{" + p.Vendor +"}")
    print( r"\newcommand*{\Title}", "{" + p.Caption +"}")
    print("\hline")
