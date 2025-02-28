from collections import defaultdict


def main():
    def buildDict():
        return {
            '(' :'leftParen',
            ')' :'rightParen',
            '[' :'leftBracket',
            ']' :'rightBracket',
            '{' :'leftBrace',
            '}' :'rightBrace',
            '.' :'dot',
            '+' :'plus',
            '-' :'minus',
            '*' :'multiply',
            '/' :'divide',
            '%' :'modulus',
            '<' :'lessThan',
            '>' :'greaterThan',
            '=' :'assignment',
            ';' :'semicolon',
            ',' :'comma',
            '++' :'increment',
            '--' :'decrement',
            '<=' :'lessThanEq',
            '>=' :'greaterThanEq',
            '==' :'logicEqual',
            '&&' :'logicAnd',
            '||' :'logicOr',
            '!' :'logicNot',
            '&' :'bitAnd',
            '|' :'bitOr',
            'int': 'int',
            'float': 'float',
            'char': 'char',
            'main': 'main',
            'return': 'return',
            'while':'while',
            'for': 'for',
            'break': 'break',
            'if': 'if',
            'else': 'else',
            'goto': 'goto',
            'continue': 'continue',
            'switch': 'switch',
            'case': 'case',
            'unsigned': 'unsigned',
            'void': 'void'
        }
    tokenDict = buildDict()
    symbols = ['+','-','*','/','<','>','&','|','=']

    with open('case.txt', 'r') as textFile:
        while True:
            #reads one character
            char = textFile.read(1)

            #if whitespace, do nothing and skip everything
            if char == ' ' or char == '\t':
                continue

            #EOF, done reading the file
            if not char:
                break

            #char is one of the special characters like &, %...
            if char in tokenDict:

                #char is one of these (+,-,<,>,=,&,|), so we need to check the next character to test whether it's + or ++ for example
                if char in symbols:

                    #we will read next character and save the current file index to come back to it if its a single character operator 
                    currentIndex = textFile.tell()
                    nextChar = textFile.read(1)

                    #it is a double character operator, so just print entry from tokendict
                    if (char+nextChar) in tokenDict:
                        print(tokenDict.get(char+nextChar), end=' ')
                    elif char == '/' and nextChar == '/':
                        while char != '\n':
                            currentIndex = textFile.tell()
                            char = textFile.read(1)
                        print("comment", end=' ')
                        textFile.seek(currentIndex)
                    #it is a single character operator, so revert the file pointer and print entry of the single character operator
                    else:
                        textFile.seek(currentIndex)
                        print(tokenDict.get(char), end=' ')

                #not one of these(+,-,<,>,=,&,|), so just print out entry from tokendict
                else:
                    print(tokenDict.get(char), end=' ')

            #char is actually a digit
            elif char.isdigit():
                digitBuilder = []
                while char.isdigit():
                    currentIndex = textFile.tell()
                    digitBuilder.append(char)
                    char = textFile.read(1)
                entireNumber = "".join(digitBuilder)
                print("number", end=' ')
                textFile.seek(currentIndex)

            #char is a letter, so we should build a string as long as we keep reading letters or digits
            elif char.isalpha():
                stringBuilder = []
                while char.isalnum():

                    #save current index before we advance file pointer, so we don't skip over a character
                    currentIndex = textFile.tell()
                    stringBuilder.append(char)
                    char = textFile.read(1)

                #we read a non alphanumeric character, so we broke out, and now we want to create the full string
                fullString = "".join(stringBuilder)
                # print(f" **{fullString}** ", end='')
                
                #if the string is a keyword, just print out the keyword
                if fullString in tokenDict:
                    print(tokenDict.get(fullString), end=' ')

                #else it is an identifier
                else:
                    print("identifier", end=' ')

                #bring the file pointer back 1 so we don't skip a character
                textFile.seek(currentIndex)
                
            #most likely new line
            else:
                print(char, end=' ')
                if char == '\n':
                    while char == '\n':
                        currentIndex = textFile.tell()
                        char = textFile.read(1)
                    textFile.seek(currentIndex)

    # while True:
    #     lexeme = input("Lexeme: ")
    #     if lexeme == 'exit':
    #         break
    #     print(tokenDict.get(lexeme))

    return

if __name__ == "__main__":
    main()
