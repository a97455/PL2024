import ply.lex as lex

def createSqlLexer(data):
    tokens = (
        'SQL',
        'NUMBER',
        'WORD',
        'OP',
        'DELIMITERS'
    )

    t_SQL = r'Select|from|where'
    t_NUMBER = r'\d+'
    t_WORD = r'\b[a-zA-Z]+\b'
    t_OP = r'>='
    t_DELIMITERS = r',|;'
    t_ignore  = ' ' #ignore spaces

    def t_error(t):
        print("Illegal character '%s'" % t.value)
        t.lexer.skip(len(t.value))

    lexer = lex.lex()
    lexer.input(data)

    for tok in lexer:
        print(tok.type + ':', tok.value)
        

if __name__ == "__main__":
    data = 'Select id, nome, salario from empregados where salario >= 820;'
    createSqlLexer(data)