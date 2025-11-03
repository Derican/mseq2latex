from lexer import lexer
from parser import parser

def convert_mseq_to_latex(input_text):
    """
    将 Microsoft Equation 格式转换为 LaTeX 格式
    """
    try:
        result = parser.parse(input_text, lexer=lexer)
        if result and hasattr(result, 'to_latex'):
            return result.to_latex()
        else:
            return None
    except Exception as e:
        print(f"转换错误: {e}")
        return None

def main():
    print("Microsoft Equation to LaTeX 转换器")
    print("支持的命令:")
    print("  \\f(分子,分母) - 分式")
    print("  \\r(被开方数) - 平方根")
    print("  \\r(根次数,被开方数) - n次根")
    print("  \\s\\up(内容) - 上标")
    print("  \\s\\do(内容) - 下标")
    print("  \\s\\ai(内容) - 对齐增量")
    print("  \\s\\di(内容) - 对齐减量")
    print()
    
    # 测试示例
    test_cases = [
        "{EQ \\f(a,b)}",
        "{EQ \\r(x)}",
        "{EQ \\r(3,x)}",
        "{EQ x\\s\\up(2)}",
        "{EQ a\\s\\do(i)}",
        "{EQ \\f(x+1,y-2) + \\r(3,a+b)}",
    ]
    
    print("测试示例:")
    for i, test_case in enumerate(test_cases, 1):
        print(f"{i}. 输入: {test_case}")
        result = convert_mseq_to_latex(test_case)
        if result:
            print(f"   输出: {result}")
        else:
            print("   转换失败")
        print()

if __name__ == "__main__":
    main()
