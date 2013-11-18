./mkpattern --pattern=./patterns/$1.py --clientrecord=24 ./output/$1.svg
inkscape --file=./output/$1.svg --verb=ZoomPage --select=A.cuttingline --select=B.cuttingline --select=C.cuttingline --select=D.cuttingline --select=E.cuttingline --select=F.cuttingline --select=G.cuttingline --verb=SelectionOffset --verb=EditDeselect --verb=FileSave
