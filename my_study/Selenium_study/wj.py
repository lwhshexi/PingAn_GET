import tkinter as tk
from tkinter import filedialog, messagebox
import shutil
import os
import uuid

# 创建主窗口
root = tk.Tk()
root.title("文件选择和上传示例")
root.geometry("400x300")  # 设置窗口大小

# 用户名输入框
username_label = tk.Label(root, text="请输入用户名:")
username_label.pack(pady=5)

username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# 显示选中文件路径的标签
file_path_label = tk.Label(root, text="请点击按钮选择文件")
file_path_label.pack(pady=20)


def open_file_dialog():
    """打开文件选择对话框"""
    file_path = filedialog.askopenfilename()
    if file_path:  # 检查用户是否选择了文件
        file_path_label.config(text=file_path)  # 更新标签显示文件路径
        upload_file(file_path)  # 调用上传文件函数
    else:
        messagebox.showwarning("警告", "未选择任何文件")  # 如果没有选择文件，显示警告


def upload_file(file_path):
    """将文件复制到项目根目录，并重命名为包含用户名和编号的格式"""
    project_root = os.getcwd()  # 获取当前工作目录，即项目根目录
    username = username_entry.get().strip()  # 获取用户名并去除空格
    if not username:
        messagebox.showwarning("警告", "请先输入用户名")
        return

    # 生成唯一编号
    unique_id = str(uuid.uuid4())[:8]  # 取UUID的前8位作为编号
    file_name = os.path.basename(file_path)  # 获取文件名
    file_extension = os.path.splitext(file_name)[1]  # 获取文件扩展名
    new_file_name = f"{username}_{unique_id}{file_extension}"  # 新文件名

    destination_path = os.path.join(project_root, new_file_name)  # 构建目标文件路径

    try:
        shutil.copy(file_path, destination_path)  # 复制文件
        messagebox.showinfo("成功", f"文件已成功上传到：{destination_path}")
    except Exception as e:
        messagebox.showerror("错误", f"文件上传失败：{e}")


# 创建选择文件的按钮
choose_file_button = tk.Button(root, text="选择文件", command=open_file_dialog)
choose_file_button.pack(pady=10)

# 运行主循环
root.mainloop()
