

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

a = mojiretsu("がやく")
print(a.stripDakuten())
