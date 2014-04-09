# -*- coding: utf-8 -*-

import re
import plistlib

class countingData:
	regular = (u'じゅう',u'いち',u'に',u'さん',u'よん',u'ご',u'ろく',u'なな',u'はち',u'きゅう')
	def allData(self):
		data = {}
		for i in range(0,10):
			if i not in self.exceptions.keys():
				data[i] = self.regular[i] + self.reading
			else:
				data[i] = self.exceptions[i]
		return data

	def __init__(self, exceptions, counter, reading, meaning=''):
		self.exceptions = exceptions
		self.counter = counter
		self.reading = reading
		self.meaning = meaning
		self.data = self.allData()

	def __getitem__(self,int):
		return self.data[int]

	def errorType(self,int):
		'''
			Error types
			Type 1: the reading of number is off
			Type 2: the reading of the counter is off
			Type 3: everything is off
		'''
		if int not in self.exceptions.keys(): return 0
		# Checking for error type 1
		if not self.exceptions[int].startswith(self.regular[int]):
			# checking for error type 2
			if not self.exceptions[int].endswith(self.reading):
				return 3
			else:
				return 1
		# if we don't have error type 1, then we have error type 2
		else:
			return 2

	# Returns a word 
	def divided(self,int):
		error = self.errorType(int)
		if error == 0:
			return self[int]
		if error == 3:
			return '*'+self[int]+'*'
		if error == 1:
			number = re.sub('\\' + self.reading + '$', '', self[int])
			return '*'+number+'*'+self.reading
		if error == 2:
			counter = re.sub('^' + self.regular[int], '', self[int])
			return self.regular[int] + '*'+counter+'*'
'''
人, にん, To count the number of people, 1:ひとり,2:ふたり,4:よにん,7:しちにん
本, ほん, To count long, cylindrical objects such as bottles or chopsticks, 1:いっぽん,3:さんぼん,6:ろっぽん,0:じゅっぽん 
冊, さつ, To count bound objects usually books, 1:いっさつ,8:はっさつ,0:じゅっさつ 
枚, まい, To count thin objects such as paper or shirts,
匹, ひき, To count small animals like cats or dogs, 1:いっぴき,3:さんびき,6:ろっぴき,8:はっぴき,0:じゅっぴき
'''

counters = []

data = plistlib.readPlist('counting.plist')

for key in data.keys():
	# Get all the exceptions
	excep = {}
	exceptions = data[key]['Exceptions']
	for i in exceptions.keys():
		excep[int(i)] = exceptions[i]
	meaning = unicode(data[key]['Meaning'])
	reading = unicode(data[key]['Reading'])
	counter = unicode(data[key]['Counter'])
	print meaning, reading, counter
	print excep
	for k in excep.keys():
		print k, excep[k]
	counters.append( countingData(exceptions=excep, counter = counter,reading = reading, meaning=meaning))





