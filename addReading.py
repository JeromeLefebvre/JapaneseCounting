# -*- coding: utf-8 -*-

import unittest
import re

'''
Find out where to add 幾（いく）

'''
oneToTenKanji = {10: u'じゅう', 1: u'いち', 2: u'に', 3: u'さん',
                 4: u'よん', 5: u'ご', 6: u'ろく', 7: u'なな', 8: u'はち', 9: u'きゅう'}
oneToTenReading = {10: u'十', 1: u'一', 2: u'二', 3: u'三',
                   4: u'四', 5: u'五', 6: u'六', 7: u'七', 8: u'八', 9: u'九'}
dakuten = {'た': 'だ', 'そ': 'ぞ', 'せ': 'ぜ', 'ヘ': 'ベ', 'す': 'ず', 'し': 'じ', 'さ': 'ざ', 'ヒ': 'ビ', 'け': 'げ', 'く': 'ぐ', 'ホ': 'ぼ', 'き': 'ぎ', 'か': 'が', 'ト': 'ド', 'テ': 'デ', 'ツ': 'ヅ', 'セ': 'ゼ', 'タ': 'ダ', 'ソ':
           'ゾ', 'ほ': 'ぼ', 'へ': 'べ', 'ク': 'グ', 'シ': 'ジ', 'ハ': 'バ', 'ふ': 'ぶ', 'ひ': 'び', 'ケ': 'ゲ', 'は': 'ば', 'キ': 'ギ', 'カ': 'ガ', 'と': 'ど', 'て': 'で', 'つ': 'づ', 'チ': 'ヂ', 'ス': 'ズ', 'サ': 'ザ', 'フ': 'ブ', 'ち': 'ぢ'}
handakuten = {'は': 'ぱ', 'フ': 'プ', 'ヘ': 'ペ', 'ほ': 'ぽ', 'へ':
              'ぺ', 'ハ': 'パ', 'ヒ': 'ピ', 'ふ': 'ぷ', 'ひ': 'ぴ', 'ホ': 'ポ'}
reverseHandakuten = {'ぽ': 'ほ', 'ポ': 'ホ', 'ぴ': 'ひ', 'パ': 'ハ',
                     'ぺ': 'へ', 'ピ': 'ヒ', 'プ': 'フ', 'ペ': 'ヘ', 'ぱ': 'は', 'ぷ': 'ふ'}
reverseDakuten = {
    'ガ': 'カ', 'ギ': 'キ', 'ど': 'と', 'づ': 'つ', 'で': 'て', 'だ': 'た', 'ぽ': 'ほ', 'ポ': 'ホ', 'ぢ': 'ち', 'ゼ': 'セ', 'ゾ': 'ソ', 'べ': 'へ', 'ジ': 'シ', 'ズ': 'ス', 'ぶ': 'ふ', 'げ': 'け', 'ば': 'は', 'び': 'ひ',
    'ゲ': 'ケ', 'が': 'か', 'ぎ': 'き', 'ド': 'ト', 'ヂ': 'チ', 'ヅ': 'ツ', 'デ': 'テ', 'ダ': 'タ', 'グ': 'ク', 'ぜ': 'せ', 'バ': 'ハ', 'ぞ': 'そ', 'ベ': 'ヘ', 'じ': 'し', 'ざ': 'さ', 'ず': 'す', 'ブ': 'フ', 'ぐ': 'く', 'ビ': 'ヒ', 'ザ': 'サ'}



def count(theNumber, ichi=2, debug=False):
    ''' This returns a kanji version of the number, v3
            The setting for ichi means: 0: do not write any 一, 1 always write 一, 2 use the "common" case'''
    original_number = theNumber
    # Not sure how to handle 1000**6, since there is there are two possible
    # choices for the kanji, then for the larger number, the associated number
    # is ambigious.
    listOfSteps = ((10000 ** 5, '垓'), (10000 ** 4, '京'), (10000 ** 3, '兆'),
                   (10000 ** 2, '億'), (10000, '万'), (1000, '千'), (100, '百'), (10, '十'))
    reading = []
    for i in range(0, len(listOfSteps)):
        step = listOfSteps[i][0]
        counter = listOfSteps[i][1]
        forThisStep = int((theNumber - theNumber % step) / step)
        theNumber = theNumber % step
        if forThisStep > 0:
            reading += [(forThisStep, counter)]
    if theNumber > 0:
        reading.append(theNumber)
    return reading


def counting_kanji2(theNumber, ichi=2, debug=False):
    ''' This returns a kanji version of the number, v2
            The setting for ichi means: 0: do not write any 一, 1 always write 一, 2 use the "common" case'''
    '''
	- Add a return numberal, so that we get outputs such as: 10兆9121置く, which is more redeable
	- Add reading of the kanji
	'''
    original_number = theNumber
    # Not sure how to handle 1000**6, since there is there are two possible
    # choices for the kanji, then for the larger number, the associated number
    # is ambigious.
    listOfSteps = ((1000 ** 5, '垓'), (10000 ** 4, '京'), (10000 ** 3, '兆'),
                   (10000 ** 2, '億'), (10000, '万'), (1000, '千'), (100, '百'), (10, '十'))
    reading = ''
    for i in range(0, len(listOfSteps)):
        step = listOfSteps[i][0]
        counter = listOfSteps[i][1]

        forThisStep = int((theNumber - theNumber % step) / step)
        theNumber = theNumber % step

        if forThisStep > 0:
            if ichi == 1:
                reading += counting_kanji2(forThisStep) + counter
            elif ichi == 2 and forThisStep > 1:
                reading += counting_kanji2(forThisStep) + counter
            # Here, we then to avoid adding the number 一
            else:
                reading += counter

    if theNumber > 0:
        reading = reading + oneToTenReading[theNumber]

    # Need a suffix, if the number is greater than 9999 and is
    if original_number > 9999 and reading[0] in ('京', '兆', '億', '万', '千') and ichi == 2:
        reading = '一' + reading

    return reading


def countingReading(integer):
    reading = ''
    # the number of man
    man = (integer - integer % 10000) / 10000
    integer = integer % 10000
    if man > 0:
        reading += str(man) + u'まん'

    sen = (integer - integer % 1000) / 1000
    integer = integer % 1000
    if sen > 0:
        reading += str(sen) + u'せん'

    hyaku = (integer - integer % 100) / 100
    integer = integer % 100
    if hyaku > 0:
        reading += str(hyaku) + u'ひゃく'

    jyu = (integer - integer % 10) / 10
    integer = integer % 10
    if jyu > 0:
        reading += str(hyaku) + u'じゅう'
    if integer > 0:
        reading = reading + oneToTenReading[integer]

    return reading


def addDakuten(letter):
    # if the letter doesn't have a dakuten, just return the letter itself
    if not letter[0] in dakuten.keys():
        return letter
    else:
        return dakuten[letter[0]] + letter[1:]


def removeDakuten(letter):
    reverseDakuten = {
        'ガ': 'カ', 'ギ': 'キ', 'ど': 'と', 'づ': 'つ', 'で': 'て', 'だ': 'た', 'ぢ': 'ち', 'ゼ': 'セ', 'ゾ': 'ソ', 'べ': 'へ', 'ジ': 'シ', 'ズ': 'ス', 'ぶ': 'ふ', 'げ': 'け', 'ば': 'は', 'び': 'ひ', 'ゲ': 'ケ',
        'が': 'か', 'ぎ': 'き', 'ド': 'ト', 'ヂ': 'チ', 'ヅ': 'ツ', 'デ': 'テ', 'ダ': 'タ', 'グ': 'ク', 'ぜ': 'せ', 'バ': 'ハ', 'ぞ': 'そ', 'ベ': 'ヘ', 'じ': 'し', 'ざ': 'さ', 'ず': 'す', 'ブ': 'フ', 'ぐ': 'く', 'ビ': 'ヒ', 'ザ': 'サ'}

    if not letter in reverseDakuten.keys():
        return letter
    else:
        return reverseDakuten[letter]


def addHandakuten(letter):
    if not letter[0] in handakuten.keys():
        return letter
    else:
        return handakuten[letter[0]] + letter[1:]


def removeHandakuten(leter):
    reverseHandakuten = {'ぽ': 'ほ', 'ポ': 'ホ', 'ぴ': 'ひ', 'パ': 'ハ',
                         'ぺ': 'へ', 'ピ': 'ヒ', 'プ': 'フ', 'ペ': 'ヘ', 'ぱ': 'は', 'ぷ': 'ふ'}
    if not letter in reverseHandakuten.keys():
        return letter
    else:
        return handakuten[letter]


def removeTen(letter):
    if letter in reverseHandakuten.keys():
        return reverseHandakuten[letter]
    elif letter in reverseDakuten.keys():
        return reverseDakuten[letter]
    else:
        return letter


def startsWith(word, listOfCandidates):
    for candidate in listOfCandidates:
        if word.startswith(candidate):
            return True
    return False


def dictionaryOfExceptions():
    '''Returns a dictionary of exceptions, the keys are tuples (integer,counter) except of ('何',counter) and the values are a list of '''
    exceptionsData = open("Exceptions.txt")
    exceptions = {}
    # The format of the file is:
    # Integer or 何；；All possible readings of the Kanji, in order of popularity
    for line in exceptionsData.readlines():
        # ignore blank lines and comment lines
        if not line.startswith('#') and not line.startswith('＃') and line != '\n' and line:
            counterData, readingData = line.split('；；')
            readingData = readingData.rstrip()
            # if there is multiple reading, it will be n a list and if there is
            # not, it still needs to be in a list
            readings = readingData.split('、')
            if counterData.startswith('何'):
                quantity = '何'
                counter = counterData[len(quantity):]
            else:
                quantity = re.findall(r'^\d+', counterData)[0]
                counter = counterData[len(quantity):]
                quantity = int(quantity)
            exceptions[(quantity, counter)] = readings
    exceptionsData.close()
    return exceptions


def dictionaryOfCounterReading():
    '''Returns a dictionary of counter readings, the keys are counter and the values are a tuple made up of the reading and meaning in english'''
    counterData = open("CounterReadingAndMeaning.txt")
    counters = {}
    # The format of the file is:
    # Kanji of counter ;;Reading;;Meaning
    for line in counterData.readlines():
        # ignore blank lines and comment lines
        line = line.rstrip('\n')
        if not line.startswith('#') and not line.startswith('＃') and line != '\n':
            try:
                counter, reading, meaningData, extraNotes = line.split('；；')
            except ValueError:
                counter, reading, meaningData = line.split('；；')
                meaning = meaningData.rstrip()
                counters[counter] = (reading, meaning)
    counterData.close()
    return counters


def reading(integer, counterKanji, counterReading=''):
    ''' Returns the correct reading for the reading, integer should be given as a integereger, the reading as a hiragana'''

    counterReadings = dictionaryOfCounterReading()
    exceptions = dictionaryOfExceptions()

    # If we are simply counting numbers, this returns the count
    if counterKanji == '':
        return countingReading(integer)

    try:
        if counterReading == '':
            # We grab the first entry of the entry, as it is the actual reading
            counterReading = counterReadings[counterKanji][0]
    except:
        print("not part of the Database")
        return -1

    if (integer, counterKanji) in exceptions.keys():
        return exceptions[(integer, counterKanji)]

    # If integer is greater than 10, and it is not an exception, then the
    # reading is done simply as the number plus the counter
    if integer > 10:
        pass
    # The regular changes to pronunciations
    if startsWith(counterReading, ('か', 'き', 'く', 'け', 'こ', 'カ', 'キ', 'ク', 'ケ', 'コ')):
        if integer == 1:
            return ['いっ' + counterReading]
        elif integer == 6:
            return ['ろっ' + counterReading]
        elif integer == 8:
            return ['はっ' + counterReading, 'はち' + counterReading]
        elif integer == 10:
            return ['じっ' + counterReading, 'じゅっ' + counterReading]
        elif integer == 20:
            return ['ひゃっ' + counterReading]
    elif startsWith(counterReading, ('さ', 'し', 'す', 'せ', 'そ', 'サ', 'シ', 'ス', 'セ', 'ソ')):
        if integer == 1:
            return ['いっ' + counterReading]
        elif integer == 8:
            return ['はっ' + counterReading]
        elif integer == 10:
            return ['じっ' + counterReading, 'じゅっ' + counterReading]
    elif startsWith(counterReading, ('た', 'ち', 'つ', 'て', 'と', 'タ', 'チ', 'ツ', 'テ', 'ト')):
        if integer == 1:
            return ['いっ' + counterReading]
        if integer == 7:
            return ['なな' + counterReading, 'しち' + counterReading]
        elif integer == 8:
            return ['はっ' + counterReading, 'はち' + counterReading]
        elif integer == 10:
            return ['じっ' + counterReading, 'じゅっ' + counterReading]
    elif startsWith(counterReading, ('は', 'ひ', 'へ', 'ほ', 'ハ', 'ヒ', 'ヘ', 'ホ')):
        if integer == 1:
            return ['いっ' + addHandakuten(counterReading)]
        elif integer == 3:
            return ['さん' + addDakuten(counterReading)]
        elif integer == 4:
            return ['よん' + counterReading, 'よん' + addHandakuten(counterReading)]
        elif integer == 6:
            return ['ろっ' + addHandakuten(counterReading)]
        elif integer == 7:
            return ['なな' + counterReading, 'しち' + counterReading]
        elif integer == 8:
            return ['はっ' + addHandakuten(counterReading), 'はち' + counterReading]
        elif integer == 10:
            return ['じっ' + addHandakuten(counterReading), 'じゅっ' + addHandakuten(counterReading)]
        elif integer == 100:
            return ['ひゃっ' + addHandakuten(counterReading)]
        elif integer == 1000:
            return ['せん' + addDakuten(counterReading)]
        elif integer == 10000:
            return ['まん' + addDakuten(counterReading)]
        elif integer == '何':
            return ['なん' + addDakuten(counterReading)]
    elif startsWith(counterReading, ('ふ', 'フ')):
        if integer == 1:
            return ['いっ' + addHandakuten(counterReading)]
        elif integer == 3:
            return ['さん' + addHandakuten(counterReading)]
        elif integer == 4:
            return ['よん' + counterReading, 'よん' + addHandakuten(counterReading)]
        elif integer == 6:
            return ['ろっ' + addHandakuten(counterReading)]
        elif integer == 8:
            return ['はっ' + addHandakuten(counterReading)]
        elif integer == 10:
            return ['じっ' + addHandakuten(counterReading), 'じゅっ' + addHandakuten(counterReading)]
        elif integer == 100:
            return ['ひゃっ' + addHandakuten(counterReading)]
        elif integer == 1000:
            return ['せん' + addHandakuten(counterReading)]
        elif integer == 10000:
            return ['まん' + addHandakuten(counterReading)]
        elif integer == '何':
            return ['なん' + addHandakuten(counterReading)]
    elif startsWith(counterReading, ('ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ', 'パ', 'ピ', 'プ', 'ペ', 'ポ')):
        if integer == 1:
            return ['いっ' + counterReading]
        elif integer == 6:
            return ['ろっ' + counterReading]
        elif integer == 8:
            return ['はっ' + counterReading]
        elif integer == 10:
            return ['じっ' + counterReading, 'じゅっ' + counterReading]
        elif integer == 100:
            return ['ひゃっ' + counterReading]
    elif startsWith(counterReading, ('わ', 'ワ')):
        if integer == 3:
            return ['さん' + 'ば' + counterReading[1:]]
        elif integer == 4:
            return ['よ' + counterReading, 'よん' + counterReading, 'よんば' + counterReading[1:]]
        elif integer == 6:
            return ['ろく' + counterReading, 'ろっぱ' + counterReading[1:]]
        elif integer == 8:
            return ['はっぱ' + counterReading[1:], 'はち' + counterReading]
        elif integer == 10:
            return ['じっぱ' + counterReading[1:], 'じゅっぱ' + counterReading[1:]]

    # If there are no exception, just return the expected answer
    return [oneToTenKanji[integer] + counterReading]


class MyTest(unittest.TestCase):

    def testFromFile(self):
        fileData = open("TestReading.txt")
        for line in fileData.readlines():
            # ignore blank lines and comment lines
            if not line.startswith('#') and line != '\n':
                counter_data, expected_reading = line.split('；；')
                expected_reading = expected_reading.rstrip()
                if '、' in expected_reading:
                    expected_reading = expected_reading.split('、')
                counter_integer = re.findall(r'^\d+', counter_data)[0]
                counterKanji = counter_data[len(counter_integer):]
                #print("expected: " + expected_reading + "got: " + str(reading(int(counter_integer),counterKanji)))
                self.assertTrue(expected_reading in reading(
                    int(counter_integer), counterKanji), "Failed here!!")
        fileData.close()

    def tfadestCountingKanji(self):
        self.assertEqual(counting_kanji2(1), '一')
        self.assertEqual(counting_kanji2(2), '二')
        self.assertEqual(counting_kanji2(3), '三')
        self.assertEqual(counting_kanji2(10), '十')
        self.assertEqual(counting_kanji2(10, 1), '一十')
        self.assertEqual(counting_kanji2(20), '二十')
        self.assertEqual(counting_kanji2(30), '三十')
        self.assertEqual(counting_kanji2(100, 2), '百')
        self.assertEqual(counting_kanji2(100, 1), '一百')
        self.assertEqual(counting_kanji2(110), '百十')
        self.assertEqual(counting_kanji2(120), '百二十')
        self.assertEqual(counting_kanji2(220), '二百二十')
        self.assertEqual(counting_kanji2(1000), '千')
        self.assertEqual(counting_kanji2(1000, ichi=1), '一千')
        self.assertEqual(counting_kanji2(10000), '一万')
        self.assertEqual(counting_kanji2(100000000), '一億')
        self.assertEqual(counting_kanji2(111111111), '一億千百十一万千百十一')
        self.assertEqual(counting_kanji2(2036521801), '二十億三千六百五十二万千八百一')


def main():
    unittest.main()


def mainTwo():
    import sys
    counter = sys.argv[1]
    counterReadings = dictionaryOfCounterReading()
    print(counterReadings[counter][1])
    range_values = sys.argv[2]
    start, end = range_values.split('-')
    print_range(counter, int(start), int(end) + 1)


def print_range(counter, start, end):
    for i in range(start, end):
        print(str(i) + counter + '=' + str(reading(i, counter)))

if __name__ == '__main__':
    mainTwo()
