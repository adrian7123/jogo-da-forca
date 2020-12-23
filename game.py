import os

class Game(object):
    _erros: int = 0
    _limite_de_erros: int = 6
    _letras = []
    _venceu = False

    def init_game(self):
        os.system('clear')
        print('=' * 21)
        print('   Jogo da Forca!!   ')
        print('=' * 21)
        print('Digite a palavra secreta: ')
        palavra = input('> ')

        # inicio do jogo
        while self._erros <= self._limite_de_erros and not self._venceu:
            self.create_canvas(palavra)

        self.end_game(self._venceu, palavra)

    def create_canvas(self, palavra, erro: bool = False, message: str = ''):
        b = self.boneco()
        palavra_secreta = self.palavra_secreta(palavra, self._letras)

        if ' - ' not in palavra_secreta:
            self._venceu = True
            return

        os.system('clear')

        if erro:
            print(message + '\n')

        print(" ____")
        print("|    |")
        print(f"|    {b[0]}")
        print(f"|   {b[2]}{b[1]}{b[3]}")
        print(f"|   {b[4]} {b[5]}")
        print(" ------  " + palavra_secreta)

        print(f'''Letras Usadas: {self._letras}''')

        print('Digite uma letra')
        letra = input('> ')

        if letra == '':
            self.create_canvas(palavra, True, 'Informe uma Letra')

        if letra not in self._letras and letra != '':
            self._letras.append(letra[0])

            if letra not in palavra:
                self._erros += 1


    def boneco(self) -> list:

        _full_boneco = [
            'O',   # 0
            '|',   # 1
            '/',   # 2
            '\\',  # 3
            '/',   # 4
            '\\'  # 5
        ]

        _new_boneco = [
            '',
            '',
            '',
            '',
            '',
            ''
        ]

        if self._erros > 0:
            for i in range(self._erros):
                # fix bug - body err
                if i == 1:
                    _new_boneco.insert(i, ' |')
                else:
                    if i == 2:
                        _new_boneco.pop(1)
                        _new_boneco.insert(1, '|')
                    _new_boneco.insert(i, _full_boneco[i])
        return _new_boneco

    def palavra_secreta(self, palavra: str, letras: list) -> str:
        _palavra_secreta = ''

        for letra in palavra:
            if letra in letras:
                _palavra_secreta += letra
            else:
                _palavra_secreta += ' - '

        return _palavra_secreta

    def end_game(self, venceu: bool, palavra):
        _erros = self._erros

        os.system('clear')
        if venceu:
            print('Venceu!!')
            print(f'Palavra: {palavra}')
            print(f'Erros: {_erros}')
            print('='*20)
            self.jogar_novamente()
        else :
            print('Perdeu!')
            print(f'Palavra: {palavra}')
            self.jogar_novamente()

    def jogar_novamente(self):
        self._erros = 0
        self._letras = []
        self._venceu = False


        jogar = input('Jogar novamente? [S/N] ')
        if jogar != 'n' and jogar != 'N' :
            self.init_game()
        else:
            os.system('clear')
            print(':(')