import ply.yacc as yacc
from lexer import tokens
from ast_nodes import EQField, Fraction, Radical, Superscript, Subscript, SpaceCommand, ExpressionSequence

# 语法规则
def p_eq_field(p):
    '''eq_field : LBRACE EQ expression RBRACE'''
    p[0] = EQField(p[3])

def p_expression_sequence(p):
    '''expression : expression expression'''
    # 处理表达式序列，如 "3 \s\up(y)"
    if isinstance(p[1], ExpressionSequence):
        p[1].add_element(p[2])
        p[0] = p[1]
    else:
        p[0] = ExpressionSequence([p[1], p[2]])

def p_expression_fraction(p):
    '''expression : CMD_FRACTION LPAREN expression COMMA expression RPAREN
                  | CMD_FRACTION LPAREN expression SEMICOLON expression RPAREN'''
    p[0] = Fraction(p[3], p[5])

def p_expression_identifier(p):
    '''expression : IDENTIFIER'''
    p[0] = p[1]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[1]

def p_expression_radical(p):
    '''expression : CMD_RADICAL LPAREN expression COMMA expression RPAREN
                  | CMD_RADICAL LPAREN expression RPAREN'''
    if len(p) == 7:  # 有两个参数的根式 \r(degree,radicand)
        p[0] = Radical(p[3], p[5])
    else:  # 只有一个参数的根式 \r(radicand) - 默认为平方根
        p[0] = Radical(None, p[3])

def p_expression_superscript(p):
    '''expression : CMD_SUP LPAREN expression RPAREN'''
    p[0] = Superscript(p[3])

def p_expression_subscript(p):
    '''expression : CMD_SUB LPAREN expression RPAREN'''
    p[0] = Subscript(p[3])

def p_expression_space_ai(p):
    '''expression : CMD_ALIGN_INC LPAREN expression RPAREN'''
    p[0] = SpaceCommand('ai', p[3])

def p_expression_space_di(p):
    '''expression : CMD_ALIGN_DEC LPAREN expression RPAREN'''
    p[0] = SpaceCommand('di', p[3])

def p_expression_text(p):
    '''expression : TEXT'''
    p[0] = p[1]

def p_expression_operator(p):
    '''expression : OPERATOR'''
    p[0] = p[1]

def p_error(p):
    if p:
        print(f"语法错误在标记 {p.type}")
    else:
        print("语法错误在文件末尾")

# 构建语法分析器
parser = yacc.yacc()