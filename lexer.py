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
    'TEXT',        # 其他文本字符（包括中文）
    'OPERATOR',    # 操作符（+, -, 等）
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
    # 检查是否是保留字
    if t.value == 'EQ':
        t.type = 'EQ'
    elif t.value == 'f':
        t.type = 'F'
    elif t.value == 'r':
        t.type = 'R'
    elif t.value == 's':
        t.type = 'S'
    return t

def t_OPERATOR(t):
    r'[+\-*/=<>]'
    return t

def t_TEXT(t):
    r'[^\{\}\\(),;+\-*/=<>\s\d]+'
    # 匹配除了特殊符号、空白、数字之外的所有字符（包括中文）
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"非法字符 '{t.value[0]}'")
    t.lexer.skip(1)

# 构建词法分析器
lexer = lex.lex()
