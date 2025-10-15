class ASTNode:
    """AST节点基类"""
    pass

class EQField(ASTNode):
    """EQ域节点"""
    def __init__(self, expression):
        self.expression = expression
    
    def to_latex(self):
        return self.expression.to_latex()

class Fraction(ASTNode):
    """分式节点"""
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def to_latex(self):
        num = self._format_expression(self.numerator)
        den = self._format_expression(self.denominator)
        return f"\\frac{{{num}}}{{{den}}}"
    
    def _format_expression(self, expr):
        if isinstance(expr, ASTNode):
            return expr.to_latex()
        else:
            return str(expr)

class Radical(ASTNode):
    """根式节点"""
    def __init__(self, degree, radicand):
        self.degree = degree  # 根次数，None表示平方根
        self.radicand = radicand  # 被开方数
    
    def to_latex(self):
        radicand = self._format_expression(self.radicand)
        
        if self.degree is None:
            # 平方根
            return f"\\sqrt{{{radicand}}}"
        else:
            # n次根
            degree = self._format_expression(self.degree)
            return f"\\sqrt[{degree}]{{{radicand}}}"
    
    def _format_expression(self, expr):
        if isinstance(expr, ASTNode):
            return expr.to_latex()
        else:
            return str(expr)

class Superscript(ASTNode):
    """上标节点"""
    def __init__(self, content):
        self.content = content
    
    def to_latex(self):
        content = self._format_expression(self.content)
        return f"^{{{content}}}"
    
    def _format_expression(self, expr):
        if isinstance(expr, ASTNode):
            return expr.to_latex()
        else:
            return str(expr)

class Subscript(ASTNode):
    """下标节点"""
    def __init__(self, content):
        self.content = content
    
    def to_latex(self):
        content = self._format_expression(self.content)
        return f"_{{{content}}}"
    
    def _format_expression(self, expr):
        if isinstance(expr, ASTNode):
            return expr.to_latex()
        else:
            return str(expr)

class SpaceCommand(ASTNode):
    """空间命令节点（ai, di）"""
    def __init__(self, command_type, content):
        self.command_type = command_type  # 'ai' 或 'di'
        self.content = content
    
    def to_latex(self):
        # 原样输出括号里的内容
        content = self._format_expression(self.content)
        return content
    
    def _format_expression(self, expr):
        if isinstance(expr, ASTNode):
            return expr.to_latex()
        else:
            return str(expr)

class CombinedScript(ASTNode):
    """组合脚本节点（处理相邻的上下标）"""
    def __init__(self, elements):
        self.elements = elements
    
    def to_latex(self):
        result = ""
        for element in self.elements:
            if isinstance(element, ASTNode):
                result += element.to_latex()
            else:
                result += str(element)
        return result

class ExpressionSequence(ASTNode):
    """表达式序列节点"""
    def __init__(self, elements):
        self.elements = elements if isinstance(elements, list) else [elements]
    
    def add_element(self, element):
        """添加新元素到序列"""
        self.elements.append(element)
    
    def to_latex(self):
        result = ""
        for i, element in enumerate(self.elements):
            if i > 0:
                result += " "  # 元素之间添加空格
            
            if isinstance(element, ASTNode):
                result += element.to_latex()
            else:
                result += str(element)
        return result
