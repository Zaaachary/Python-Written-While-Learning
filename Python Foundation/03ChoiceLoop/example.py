def licai(base, rate, monthadd, years):
    """计算本金在年利率rate的情况下 经过days天后投资的收益"""
    result = float(base)
    for y in range(years):
        for i in range(12):
            result += monthadd
            result += result * rate / 365 * 30
    addin = base + monthadd * 12 * years
    print("经过%d年的定投，本金和定投共%f元，总收益为%f，收益率为%f" \
          % (years, addin, result, result / addin))


if __name__ == '__main__':
    # 30000, 0.25, 500, 5
    b, r, m, y = eval(input())
    licai(b, r, m, y)
