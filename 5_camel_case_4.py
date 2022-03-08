s = '''C;V;can of coke\r
C;C;mirror\r
S;M;sweatTea()\r
S;V;epsonPrinter\r
C;M;santa claus\r
C;C;mirror\r'''
# https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=three-month-preparation-kit&playlist_slugs%5B%5D=three-month-week-one
import sys
import re

def print_lines(l_lines):
    def get_function(comand, tipo):
        r_split   = comand == "S"
        r_combine = comand == "C"
        
        r_method   = tipo == "M"
        r_class    = tipo == "C"
        r_variable = tipo == "V"
        
        if r_combine:
            def subs_titui_letras(word, index):
                pl_saida = ""
                for i, letter in enumerate(word):
                    firs_letter =  word[index+1]
                    r_lugar_substituir = (index + 1) == i
                    if r_lugar_substituir:
                        pl_saida = pl_saida + firs_letter.upper()
                    else:
                        pl_saida = pl_saida + letter
                return pl_saida

            def combine_function(word):
                saida = list(re.finditer(r" ",word))
                if r_variable or r_method:
                    pl_saida = word
                    for s in saida:
                        index = s.start()
                        pl_saida = subs_titui_letras(pl_saida, s.start())
                        
                        
                        
                        # word = pl_saida

                   
                    pl_saida = pl_saida.replace(" ", "")
                    
                    if r_method:
                        pl_saida = pl_saida + "()"
                    
                    
                    print(pl_saida)

                if r_class:
                    pl_saida = ""
                    saida = list(re.finditer(r" ",word))
                    for s in saida:
                        index = s.start()
                        firs_letter =  word[index+1]
                        
                        for i, letter in enumerate(word):
                            r_lugar_substituir = (index + 1) == i
                            r_primeira_letra = i == 0
                            if r_primeira_letra:
                                pl_saida = pl_saida + word[0].upper()
                            elif r_lugar_substituir:
                                pl_saida = pl_saida + firs_letter.upper()
                            else:
                                pl_saida = pl_saida + letter
                    
                    r_palavra_unica = len(saida) == 0
                    if r_palavra_unica:
                        for i, letter in enumerate(word):
                            r_primeira_letra = i == 0
                            if r_primeira_letra:
                                pl_saida = pl_saida + word[0].upper()
                            else:
                                pl_saida = pl_saida + letter

                    pl_saida = pl_saida.replace(" ", "")


                    print(pl_saida)

            return combine_function


        if r_split:
            def split_function(word):
                # if r_method:
                #     saida = re.finditer(r"[A-Z]",word)
                #     for s in saida:
                #         print(s)
                #     print(" ".join(saida))

                if r_class or r_method or r_variable:
                    saida = list(re.finditer(r"[A-Z]",word))
                    word = word.lower()
                    add = 0
                    for s in saida:
                        index = s.start()
                        r_primeiro_index = index == 0
                        if r_primeiro_index:
                            pass
                        else:
                            word = word[:index+add] + " " + word[index+add:]
                            add += 1
                    if r_method:
                        word = word.replace("()", "")
                    print(word)

            


                    # saida[0] = saida[0].lower()

                
                # print(word)
                # if r_method:
                #     saida = re.split(r"",word)
                #     return lambda x: print(x)
            
            return split_function
        


        return lambda x: print(x)
    
    
    for line in l_lines:
        comand, method, word = line.split(";") 
        get_function(comand, method)(word)
    





def main():
    string_ing = s.split("\n")
    string_ing_clear = list(map(lambda x: x.replace("\r", ""), string_ing))
    print_lines(string_ing_clear)


main()