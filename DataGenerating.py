# -*- coding: utf-8 -*-

import plistlib
from plistlib import writePlist
import datetime
from datetime import time
from pickle import dump


data = '''人;; にん;; To count the number of people;; 1:ひとり,2:ふたり,4:よにん,7:しちにん
本;; ほん;; To count long, cylindrical objects such as bottles or chopsticks;; 1:いっぽん,3:さんぼん,6:ろっぽん,0:じゅっぽん 
冊;; さつ;; To count bound objects usually books;; 1:いっさつ,8:はっさつ,0:じゅっさつ 
枚;; まい;; To count thin objects such as paper or shirts;; 
匹;; ひき;; To count small animals like cats or dogs;; 1:いっぴき,3:さんびき,6:ろっぴき,8:はっぴき,0:じゅっぴき
歳;; さい;; To count the age of a living creatures such as people;; 1:いっさい,8:はっさい,10:じゅっさい
'''

pl = {}

for l in data.split('\n'):
	counter,reading,meaning,exception_data = l.split(';; ')
	counter = unicode(counter,'utf-8')
	reading = unicode(reading,'utf-8')
	exceptions = {}
	for a in exception_data.split(','):
		if len(a) > 0:
			number,special_reading = a.split(':')
			#number = int(number)
			exceptions[number] = unicode(special_reading,'utf-8')
	pl[counter] = {'Counter':counter, 'Reading':reading, 'Meaning':meaning,'Exceptions':exceptions}

print pl
#pl = {u'本':{'Counter':u'本','Reading':u'ほん','Meaning':'To count long, cylindrical objects such as bottles or chopsticks', 'Exceptions':{}}}
# unicode keys are possible, but a little awkward to use:
#pl[u'\xc5benraa'] = "That was a unicode key."
writePlist(pl, "test.pblist")