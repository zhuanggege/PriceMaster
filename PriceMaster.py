# price_calculation.py

def calculate_price(purchase_price, shipping_fee, packaging_fee, commission_rate, profit_ratio, exchange_rate):
    """
    计算售价、总成本、利润等

    :param purchase_price: 进货价
    :param shipping_fee: 运费
    :param packaging_fee: 打包费
    :param commission_rate: 佣金率（百分比）
    :param profit_ratio: 利润比例（百分比）
    :return: 返回一个字典包含计算结果
    """
   
    commission_rate_decimal = commission_rate / 100  # 将佣金率转换为小数
    profit_ratio_decimal = profit_ratio / 100  # 将利润率转换为小数

    # 先计算售价
    selling_price = (purchase_price + shipping_fee + packaging_fee) / (1 - commission_rate_decimal - profit_ratio_decimal)  # 使用小数形式
    commission = selling_price * commission_rate_decimal  # 使用小数形式
    profit = selling_price * profit_ratio_decimal  # 使用小数形式

    # 现在可以计算总成本
    total_cost = purchase_price + shipping_fee + packaging_fee + commission

    ruble_conversion = selling_price * exchange_rate  # 使用自定义汇率

    # 返回所有计算的结果
    return {
        "selling_price": selling_price,
        "purchase_price": purchase_price,
        "shipping_fee": shipping_fee,
        "packaging_fee": packaging_fee,
        "commission": commission,
        "commission_rate": commission_rate,
        "profit": profit,
        "profit_ratio": profit_ratio,
        "ruble_conversion": ruble_conversion,
        "total_cost": total_cost
    }