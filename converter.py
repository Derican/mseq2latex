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
                res = result.to_latex()
                if result.is_block:
                    return f"\\[ {res} \\]"
                else:
                    return f"$ {res} $"
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
        "{ EQ a + b + v \\s\\do(c) }",
        # 括号功能测试用例
        "{ EQ \\b(a) }",  # 基本括号
        "{ EQ \\b \\lc\\{ (a) }",  # 左大括号，右圆括号  
        "{ EQ \\b \\lc\\{ \\rc\\) (a) }",  # 左大括号，右圆括号
        "{ EQ \\b \\bc\\{ (a) }",  # 两边都是大括号
        "{ EQ \\b \\bc\\{ \\lc\\( \\rc\\| (b) }",  # 复杂选项，右侧会覆盖
        # 置换功能测试用例
        "{ EQ \\d() }",  # 空置换
        "{ EQ \\d(hello) }",  # 简单置换
        "{ EQ \\d \\fo10 \\li() }",  # 带选项的空置换
        "{ EQ \\d \\fo10 \\ba5 (world) }",  # 带选项的置换
        "{ EQ \\d \\li(underline) }",  # 下划线选项
        # 积分功能测试用例
        "{ EQ \\i(0,1,x) }",  # 基本积分
        "{ EQ \\i \\su(1,5,3) }",  # 求和
        "{ EQ \\i \\pr(1,n,i) }",  # 乘积
        "{ EQ \\i \\su \\in(i,j,k) }",  # 内联求和
        "{ EQ \\i \\fc\\S(x,\\f(\\r(2,x),3),x + 3) }",  # 自定义符号（存储选项）
        # 列表功能测试用例
        "{ EQ \\l(A,B,C,D,E) }",  # 基本列表
        "{ EQ \\l(1,2,3) }",  # 数字列表
        "{ EQ \\l(x,y,z) }",  # 变量列表
        "{ EQ \\l(A;B;C) }",  # 分号分隔的列表
        "{ EQ \\l(\\f(1,2),\\r(3,x),\\i(0,1,x) ) }",  # 复杂元素列表
        # 重叠功能测试用例
        "{ EQ \\o(A,B,C) }",  # 基本重叠
        "{ EQ \\o \\al(x,y,z) }",  # 左对齐重叠
        "{ EQ \\o \\ac(1,2,3) }",  # 居中对齐重叠（默认）
        "{ EQ \\o \\ar(a,b,c) }",  # 右对齐重叠
        "{ EQ \\o \\al \\ar(X,Y) }",  # 多选项重叠（右侧覆盖）
        "{ EQ \\o \\ar (\\f(1,2),\\r(3,x),\\i(0,1,x) ) }",  # 复杂重叠
        # Box功能测试用例
        "{ EQ \\x(a) }",  # 基本Box
        "{ EQ \\x \\to \\bo(element) }",       # 上下边框
        "{ EQ \\x \\le(left) }",               # 左边框
        "{ EQ \\x \\ri(right) }",              # 右边框
        "{ EQ \\x \\to \\bo \\le \\ri(full) }", # 完整边框
        "{ EQ \\x \\to(\\f(1,2)) }",           # 边框包含分式
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
