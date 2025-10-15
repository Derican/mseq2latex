import ply.lex as lex

# 定义标记
tokens = (
    'LBRACE',      # {
    'RBRACE',      # }
    'EQ',          # EQ
    'BACKSLASH',   # \
    'F',           # f
    'R',           # r
    'S',           # s
    'UP',          # up
    'DO',          # do
    'AI',          # ai
    'DI',          # di
    'LPAREN',      # (
    'RPAREN',      # )
    'COMMA',       # ,
    'SEMICOLON',   # ;
    'IDENTIFIER',  # 标识符
    'NUMBER',      # 数字
)

# 标记规则
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_BACKSLASH = r'\\'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

# 忽略空白字符
t_ignore = ' \t'

def t_EQ(t):
    r'EQ'
    return t

def t_F(t):
    r'f'
    return t

def t_R(t):
    r'r'
    return t

def t_S(t):
    r's'
    return t

def t_UP(t):
    r'up\d*'
    return t

def t_DO(t):
    r'do\d*'
    return t

def t_AI(t):
    r'ai\d*'
    return t

def t_DI(t):
    r'di\d*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"非法字符 '{t.value[0]}'")
    t.lexer.skip(1)

# 构建词法分析器
lexer = lex.lex()
