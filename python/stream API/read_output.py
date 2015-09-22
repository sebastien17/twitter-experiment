__author__ = 'mirko'
# -*- coding: utf-8 -*-
import json
import glob
import gzip



filelist = sorted(glob.glob("*.out.gz"))


for file in filelist:
    print file
    infile = gzip.open(file, 'rb')

    try:

        for row in infile:
            data = json.loads(row)

    except Exception,e:
        print 'exeption in file '+str(e)

