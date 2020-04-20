
upper_dict = {'ァ':'ア', 'ィ': 'イ', 'ゥ': 'ウ', 'ェ': 'エ', 'ォ': 'オ',
              'ャ': 'ヤ', 'ュ': 'ユ', 'ョ': 'ヨ'}


class Pokemon():

    def __init__(self, num, name):
        self.num = int(num)
        self.name = name

    def __str__(self):
        return "No.{} {}".format(self.num, self.name)

    def first_letter(self):
        """名前のはじめの文字を返す"""
        return self.name[0]

    def last_letter(self):
        """引数の最後の文字を返す
        最後の文字が小文字だった場合は、その文字を大文字にして返す
        最後の文字が ー だった場合は、その前の文字を返す
        """
        c = self.name[-1]
        if c == 'ー':
            c = self.name[-2]

        if c in "ァィゥェォャュョ":
            c = upper_dict[c]
        return c

    def number(self):
        return self.num

    def name(self):
        return self.name


class PokemonNo():

    def __init__(self, num):
        if num == '***':
            self.num = num
        else:
            self.num = int(num)
