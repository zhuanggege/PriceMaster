# main_window.py

import tkinter as tk
from tkinter import messagebox
from PriceMaster import calculate_price  # 导入计算函数

def calculate():
    try:
        # 获取输入值
        purchase_price = float(entry_purchase_price.get())
        shipping_fee = float(entry_shipping_fee.get())
        packaging_fee = float(entry_packaging_fee.get())
        commission_rate = float(entry_commission_rate.get())  # 百分比输入
        profit_ratio = float(entry_profit_ratio.get())  # 百分比输入
        exchange_rate = float(entry_exchange_rate.get())  # 获取汇率输入
        
        # 调用 calculate_price 函数计算结果
        result = calculate_price(purchase_price, shipping_fee, packaging_fee, commission_rate, profit_ratio, exchange_rate)  # 传递汇率
       
        # 显示计算结果，横排显示
        label_selling_price_value.config(text=f"{result['selling_price']:.2f}") # type: ignore
        label_purchase_price_value.config(text=f"{result['purchase_price']:.2f}")# type: ignore
        label_shipping_fee_value.config(text=f"{result['shipping_fee']:.2f}")# type: ignore
        label_packaging_fee_value.config(text=f"{result['packaging_fee']:.2f}")# type: ignore
        label_commission_value.config(text=f"{result['commission']:.2f}")# type: ignore
        label_commission_rate_value.config(text=f"{result['commission_rate']:.2f}%")# type: ignore
        label_profit_value.config(text=f"{result['profit']:.2f}")# type: ignore
        label_profit_ratio_value.config(text=f"{result['profit_ratio']:.2f}%")# type: ignore
        label_ruble_conversion_value.config(text=f"{result['ruble_conversion']:.2f}")# type: ignore
        label_total_cost_value.config(text=f"{result['total_cost']:.2f}")# type: ignore

    except ValueError:
        messagebox.showerror("输入错误", "请确保所有输入字段为有效数字！")

# 创建主窗口
root = tk.Tk()
root.title("售价计算器")

# 设置窗口大小并让窗口居中
root.geometry("800x400")  # 设置窗口宽度800px，高度500px
root.eval('tk::PlaceWindow . center')  # 让窗口居中显示

# 创建一个 Frame 容器来将所有内容包裹，并在其中居中显示
frame = tk.Frame(root)
frame.pack(expand=True, fill="both", padx=5, pady=20)

# 输入区域：所有控件放入 Frame 中
tk.Label(frame, text="进货价:", anchor="center").grid(row=0, column=0, padx=5, pady=5, sticky="ew")
entry_purchase_price = tk.Entry(frame)
entry_purchase_price.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame, text="运费:", anchor="center").grid(row=1, column=0, padx=5, pady=5, sticky="ew")
entry_shipping_fee = tk.Entry(frame)
entry_shipping_fee.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame, text="打包费:", anchor="center").grid(row=2, column=0, padx=5, pady=5, sticky="ew")
entry_packaging_fee = tk.Entry(frame)
entry_packaging_fee.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame, text="佣金率 (%)-直接输入数字:", anchor="center").grid(row=3, column=0, padx=5, pady=5, sticky="ew")
entry_commission_rate = tk.Entry(frame)
entry_commission_rate.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame, text="利润比例 (%)-直接输入数字:", anchor="center").grid(row=4, column=0, padx=5, pady=5, sticky="ew")
entry_profit_ratio = tk.Entry(frame)
entry_profit_ratio.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame, text="汇率:", anchor="center").grid(row=5, column=0, padx=5, pady=5, sticky="ew")
entry_exchange_rate = tk.Entry(frame)  # 新增汇率输入框
entry_exchange_rate.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# 计算按钮
tk.Button(frame, text="计算", command=calculate).grid(row=6, column=0, columnspan=2, pady=10, sticky="ew")

# 输出区域：横向排列计算结果
output_labels = [
    ("售价", "selling_price"),
    ("进货价", "purchase_price"),
    ("运费", "shipping_fee"),
    ("打包费", "packaging_fee"),
    ("佣金", "commission"),
    ("佣金率", "commission_rate"),
    ("利润", "profit"),
    ("利润比例", "profit_ratio"),
    ("换算卢布", "ruble_conversion"),
    ("总成本", "total_cost"),
]

for i, (text, key) in enumerate(output_labels):
    tk.Label(frame, text=text, anchor="center").grid(row=10, column=i*2, padx=5, pady=1, sticky="ew")
    result_label = tk.Label(frame, text="0.00", anchor="center")  # 确保结果文本居中
    result_label.grid(row=11, column=i*2, padx=(2, 2), pady=1, sticky="ew")  # 减小右边的间距
    globals()[f"label_{key}_value"] = result_label


# 主循环
root.mainloop()
