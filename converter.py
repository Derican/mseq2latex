from lexer import lexer
from parser import parser

class MSEQToLatexConverter:
    """Microsoft EQ到LaTeX转换器"""
    
    def __init__(self):
        self.lexer = lexer
        self.parser = parser
    
    def convert(self, eq_text):
        """将EQ域文本转换为LaTeX"""
        try:
            # 词法分析
            self.lexer.input(eq_text)
            
            # 语法分析
            result = self.parser.parse(eq_text, lexer=self.lexer)
            
            if result:
                return result.to_latex()
            else:
                return None
                
        except Exception as e:
            print(f"转换错误: {e}")
            return None

def main():
    converter = MSEQToLatexConverter()
    
    # 测试示例
    test_cases = [
        "{ EQ \\f(2,RateChange) }",
        "{ EQ \\f(x,y) }",
        "{ EQ \\f(1,2) }",
        "{ EQ \\f(1,\\f(1,2)) }",
        "{ EQ \\r(3,x) }",
        "{ EQ \\r(x) }",
        "{ EQ \\r(2,\\f(1,2)) }",
        "{ EQ \\r(\\f(1,2),2) }",
        "{ EQ \\s\\ai2(a) }",
        "{ EQ \\s\\di3(b) }",
        "{ EQ \\s\\up(a) }",
        "{ EQ \\s\\up4(a) }",
        "{ EQ \\s\\do(a) }",
        "{ EQ \\s\\do3(a) }",
        "{ EQ \\f(\\r(2,x), 3 \\s\\up(y)) }",
        "{ EQ v \\s\\do(0 + \\r(2,x) - \\f(1,2)) }",
    ]
    
    for test in test_cases:
        print(f"输入: {test}")
        result = converter.convert(test)
        if result:
            print(f"输出: {result}")
        else:
            print("转换失败")
        print("-" * 40)

if __name__ == "__main__":
    main()
