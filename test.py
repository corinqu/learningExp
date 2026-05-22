import tkinter as tk

root = tk.Tk()
root.title("Grid 动态伸缩 vs Place 绝对死板")
root.geometry("500x250")

# =====================================================================
# 核心对比 A：GRID 区域 (支持完美的响应式动态拉伸)
# =====================================================================
frame_g = tk.LabelFrame(root, text=" 1. grid() - 配置了权重 (拖拽窗口看我自动变宽) ", fg="green")
frame_g.pack(side="top", fill="both", expand=True, padx=10, pady=10)

# 💡 核心魔法：告诉 grid，第 0 列和第 1 列的权重都是 1 (即 1:1 平分剩余空间)
frame_g.columnconfigure(0, weight=1)
frame_g.columnconfigure(1, weight=1)
# 同时也让行可以上下拉伸
frame_g.rowconfigure(0, weight=1)

# 摆放两个按钮，并用 sticky="nsew" 让它们上下左右吸附并撑满格子
btn_g1 = tk.Button(frame_g, text="Grid 按钮 1 (各占50%)", bg="lightgreen")
btn_g1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

btn_g2 = tk.Button(frame_g, text="Grid 按钮 2 (各占50%)", bg="lightgreen")
btn_g2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)


# =====================================================================
# 核心对比 B：PLACE 区域 (死板定位，无法对窗口变化做出响应)
# =====================================================================
frame_p = tk.LabelFrame(root, text=" 2. place() - 固定坐标 (拖拽窗口时我毫无反应) ", fg="red", height=90)
frame_p.pack(side="top", fill="x", padx=10, pady=10)

# 使用 place 只能写死它们的大小和位置
btn_p1 = tk.Button(frame_p, text="Place 按钮 1", bg="lightcoral")
btn_p1.place(x=10, y=15, width=180, height=40)

btn_p2 = tk.Button(frame_p, text="Place 按钮 2", bg="lightcoral")
btn_p2.place(x=210, y=15, width=180, height=40)

root.mainloop()