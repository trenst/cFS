#!/usr/bin/env python
import glob
import os
import subprocess as subp



processFoldername = "/home/sdev/src/cfs/build/exe/cpu1/cf"


def countOccurances(objL: list):
    for obj in objL:
        cnt = objL.count(obj)
        if cnt != 1:
            print('dkfjkkkfkkkdkfdlkjfldsfsdafdsaf')


def main():
    libraryFilesExe = glob.glob("*.so", root_dir=processFoldername)
    libraryFilesExe.append(os.path.join('..', 'core-cpu1'))
    objList = []
    objType = []
    addressList = []
    objAllList = []
    for file in libraryFilesExe:
        lib = os.path.join(processFoldername, file)
        cmd = ["readelf", "--dyn-syms", "--wide", lib]
        readelf = subp.run(cmd, capture_output=True)
        fullList = readelf.stdout.decode().splitlines()[3:]
        objList.append([])
        objType.append([])
        addressList.append([])
        for line in fullList:
            lsplit = line.split()
            # Append the symbols which are defined in this library.  UND = undefined
            if lsplit[6] != 'UND':
                objList[-1].append(lsplit[7])
                objAllList.append(lsplit[7])
                addressList[-1].append(lsplit[1])
                objType[-1].append(lsplit[3])

    print(len(objAllList))
    countOccurances(objAllList)



if __name__=='__main__':
    main()