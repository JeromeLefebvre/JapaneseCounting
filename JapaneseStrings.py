

class mojiretsu(str):

    ''' A class to do basic string manipulations in Japanese '''
    dakuten = {'た': 'だ', 'そ': 'ぞ', 'せ': 'ぜ', 'ヘ': 'ベ', 'す': 'ず', 'し': 'じ', 'さ': 'ざ', 'ヒ': 'ビ', 'け': 'げ', 'く': 'ぐ', 'ホ': 'ぼ', 'き': 'ぎ', 'か': 'が', 'ト': 'ド', 'テ': 'デ', 'ツ': 'ヅ', 'セ': 'ゼ', 'タ': 'ダ', 'ソ':
           'ゾ', 'ほ': 'ぼ', 'へ': 'べ', 'ク': 'グ', 'シ': 'ジ', 'ハ': 'バ', 'ふ': 'ぶ', 'ひ': 'び', 'ケ': 'ゲ', 'は': 'ば', 'キ': 'ギ', 'カ': 'ガ', 'と': 'ど', 'て': 'で', 'つ': 'づ', 'チ': 'ヂ', 'ス': 'ズ', 'サ': 'ザ', 'フ': 'ブ', 'ち': 'ぢ'}

    reverseDakuten = {
        'ガ': 'カ', 'ギ': 'キ', 'ど': 'と', 'づ': 'つ', 'で': 'て', 'だ': 'た', 'ぽ': 'ほ', 'ポ': 'ホ', 'ぢ': 'ち', 'ゼ': 'セ', 'ゾ': 'ソ', 'べ': 'へ', 'ジ': 'シ', 'ズ': 'ス', 'ぶ': 'ふ', 'げ': 'け', 'ば': 'は', 'び': 'ひ',
        'ゲ': 'ケ', 'が': 'か', 'ぎ': 'き', 'ド': 'ト', 'ヂ': 'チ', 'ヅ': 'ツ', 'デ': 'テ', 'ダ': 'タ', 'グ': 'ク', 'ぜ': 'せ', 'バ': 'ハ', 'ぞ': 'そ', 'ベ': 'ヘ', 'じ': 'し', 'ざ': 'さ', 'ず': 'す', 'ブ': 'フ', 'ぐ': 'く', 'ビ': 'ヒ', 'ザ': 'サ'}

    def stripDakuten(self):
        ''' Remove all dakuten from the string '''
        string = ''
        for char in self:
            try:
                string += self.reverseDakuten[char]
            except KeyError:
                string += char
        return string

    def dakutenize(letter):
        ''' Add dakuten to the first letter '''
        try:
            self.dakuten[letter[0]] + letter[1:]
        except:
            return letter

    def count(self, ichi=2):
        ''' Converts a string reprensenting an integer into kanjis
            The setting for ichi means: 0: do not write any 一, 1 always write 一, 2 use the "common" case'''
        assert(self.isnumeric())
        number = int(self)
        original_number = number
        # Not sure how to handle 1000**6, since there is there are two possible
        # choices for the kanji, then for the larger number, the associated number
        # is ambigious.
        listOfSteps = ((10000 ** 5, '垓'), (10000 ** 4, '京'), (10000 ** 3, '兆'),
                       (10000 ** 2, '億'), (10000, '万'), (1000, '千'), (100, '百'), (10, '十'))
        reading = []
        for step, counter in listOfSteps:
            forThisStep = int((number - number % step) / step)
            number = number % step
            if forThisStep > 0:
                reading += [(forThisStep, counter)]
        string = ''.join( str(a) + b for a,b in reading )
        if number > 0:
            reading.append(number)
            string += str(number)
        return string

    @staticmethod
    def katakana(gyo, dan):
        d = {('あ','あ'): 'ア', ('あ','い'): 'イ', ('あ','う'): 'ウ', ('あ','え'): 'エ', ('あ','お'): 'オ',
            ('か','あ'): 'カ', ('か','い'): 'キ', ('か','う'): 'ク', ('か','え'): 'ケ', ('か','お'): 'コ',
            ('さ','あ'): 'サ', ('さ','い'): 'シ', ('さ','う'): 'ス', ('さ','え'): 'セ', ('さ','お'): 'ソ',
            ('た','あ'): 'タ', ('た','い'): 'チ', ('た','う'): 'ツ', ('た','え'): 'テ', ('た','お'): 'ト',
            ('な','あ'): 'ナ', ('な','い'): 'ニ', ('な','う'): 'ヌ', ('な','え'): 'ネ', ('な','お'): 'ノ',
            ('は','あ'): 'ハ', ('は','い'): 'ヒ', ('は','う'): 'フ', ('は','え'): 'ヘ', ('は','お'): 'ホ',
            ('ま','あ'): 'マ', ('ま','い'): 'ミ', ('ま','う'): 'ム', ('ま','え'): 'メ', ('ま','お'): 'モ',
            ('や','あ'): 'ヤ',                   ('や','う'): 'ユ',                   ('や','お'): 'ヨ',
            ('ら','あ'): 'ラ', ('ら','い'): 'リ', ('ら','う'): 'ル', ('ら','え'): 'レ', ('ら','お'): 'ロ',
            ('わ','あ'): 'ワ', ('わ','い'): 'ヰ',                   ('わ','え'): 'ヱ', ('わ','お'): 'ヲ',
            ('ん',): 'ン',

            ('a','a'): 'ア', ('a','i'): 'イ', ('a','u'): 'ウ', ('a','e'): 'エ', ('a','o'): 'オ',
            ('k','a'): 'カ', ('k','i'): 'キ', ('k','u'): 'ク', ('k','e'): 'ケ', ('k','o'): 'コ',
            ('s','a'): 'サ', ('s','i'): 'シ', ('s','u'): 'ス', ('s','e'): 'セ', ('s','o'): 'ソ',
            ('t','a'): 'タ', ('t','i'): 'チ', ('t','u'): 'ツ', ('t','e'): 'テ', ('t','o'): 'ト',
            ('n','a'): 'ナ', ('n','i'): 'ニ', ('n','u'): 'ヌ', ('n','e'): 'ネ', ('n','o'): 'ノ',
            ('h','a'): 'ハ', ('h','i'): 'ヒ', ('h','u'): 'フ', ('h','e'): 'ヘ', ('h','o'): 'ホ',
            ('m','a'): 'マ', ('m','i'): 'ミ', ('m','u'): 'ム', ('m','e'): 'メ', ('m','o'): 'モ',
            ('y','a'): 'ヤ',                  ('y','u'): 'ユ',                   ('y','o'): 'ヨ',
            ('r','a'): 'ラ', ('r','i'): 'リ', ('r','u'): 'ル', ('r','e'): 'レ', ('r','o'): 'ロ',
            ('w','a'): 'ワ', ('w','i'): 'ヰ',                   ('w','e'): 'ヱ', ('w','o'): 'ヲ',
            ('n',): 'ン'            
            }
        try:
            return d[gyo][dan]
        except KeyError as e:
            return KeyError("No katakana for the given pairs %s, %s", gyo, dan)


for i in range(1, 20):
    j = mojiretsu(i)
    print(i,j.count())
