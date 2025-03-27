import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import os
import sys
import importlib.util

# 動態導入原有的pictures2gif模組
def import_pictures2gif_module():
    try:
        # 獲取當前腳本的路徑
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # 構建pictures2gif.py的完整路徑
        module_path = os.path.join(current_dir, 'pictures2gif.py')
        
        # 動態導入模組
        spec = importlib.util.spec_from_file_location("pictures2gif", module_path)
        pictures2gif = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pictures2gif)
        
        return pictures2gif
    except Exception as e:
        messagebox.showerror("錯誤", f"無法導入pictures2gif模組: {str(e)}")
        return None

class GifMakerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("圖片轉GIF工具")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # 導入pictures2gif模組
        self.pictures2gif = import_pictures2gif_module()
        if not self.pictures2gif:
            self.root.destroy()
            return
        
        self.setup_ui()
    
    def setup_ui(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 標題
        title_label = ttk.Label(main_frame, text="圖片轉GIF工具", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # 圖片文件夾選擇
        folder_frame = ttk.Frame(main_frame)
        folder_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(folder_frame, text="圖片文件夾:").pack(side=tk.LEFT)
        self.folder_path_var = tk.StringVar()
        folder_entry = ttk.Entry(folder_frame, textvariable=self.folder_path_var, width=30)
        folder_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        browse_button = ttk.Button(folder_frame, text="瀏覽...", command=self.browse_folder)
        browse_button.pack(side=tk.LEFT)
        
        # 輸出GIF文件名
        output_frame = ttk.Frame(main_frame)
        output_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(output_frame, text="輸出GIF名稱:").pack(side=tk.LEFT)
        self.output_name_var = tk.StringVar(value="animation.gif")
        output_entry = ttk.Entry(output_frame, textvariable=self.output_name_var, width=30)
        output_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        # 輸出GIF存放位置
        save_frame = ttk.Frame(main_frame)
        save_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(save_frame, text="保存位置:").pack(side=tk.LEFT)
        self.save_path_var = tk.StringVar()
        save_entry = ttk.Entry(save_frame, textvariable=self.save_path_var, width=30)
        save_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        save_button = ttk.Button(save_frame, text="瀏覽...", command=self.browse_save_location)
        save_button.pack(side=tk.LEFT)
        
        # 每幀持續時間
        duration_frame = ttk.Frame(main_frame)
        duration_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(duration_frame, text="每幀持續時間(毫秒):").pack(side=tk.LEFT)
        self.duration_var = tk.IntVar(value=100)
        duration_spinbox = ttk.Spinbox(duration_frame, from_=10, to=1000, increment=10, 
                                       textvariable=self.duration_var, width=10)
        duration_spinbox.pack(side=tk.LEFT, padx=5)
        
        # 進度條
        self.progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        progress_bar.pack(fill=tk.X, pady=10)
        
        # 創建GIF按鈕
        create_button = ttk.Button(main_frame, text="創建GIF", command=self.create_gif)
        create_button.pack(pady=10)
        
        # 狀態標籤
        self.status_var = tk.StringVar(value="就緒")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, font=("Arial", 10))
        status_label.pack(pady=5)
    
    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="選擇包含圖片的文件夾")
        if folder_path:
            self.folder_path_var.set(folder_path)
            # 預設將保存位置設為與圖片相同的文件夾
            if not self.save_path_var.get():
                self.save_path_var.set(folder_path)
    
    def browse_save_location(self):
        save_path = filedialog.askdirectory(title="選擇GIF保存位置")
        if save_path:
            self.save_path_var.set(save_path)
    
    def create_gif(self):
        # 獲取所有輸入
        folder_path = self.folder_path_var.get()
        output_name = self.output_name_var.get()
        save_path = self.save_path_var.get()
        duration = self.duration_var.get()
        
        # 檢查輸入
        if not folder_path:
            messagebox.showerror("錯誤", "請選擇包含圖片的文件夾")
            return
        
        if not os.path.isdir(folder_path):
            messagebox.showerror("錯誤", "所選圖片文件夾不存在")
            return
        
        if not save_path:
            messagebox.showerror("錯誤", "請選擇GIF保存位置")
            return
        
        if not os.path.isdir(save_path):
            messagebox.showerror("錯誤", "所選保存位置不存在")
            return
        
        if not output_name:
            messagebox.showerror("錯誤", "請輸入輸出GIF名稱")
            return
        
        # 確保輸出名稱有.gif擴展名
        if not output_name.lower().endswith('.gif'):
            output_name += '.gif'
        
        # 組合完整輸出路徑
        full_output_path = os.path.join(save_path, output_name)
        
        # 更新狀態
        self.status_var.set("正在創建GIF...")
        self.progress_var.set(50)  # 設置進度為50%
        self.root.update()
        
        try:
            # 調用原始程式的函數
            self.pictures2gif.create_gif_from_images(folder_path, full_output_path, duration)
            
            # 更新狀態和進度
            self.status_var.set(f"GIF已成功創建: {full_output_path}")
            self.progress_var.set(100)  # 設置進度為100%
            
            # 詢問用戶是否要打開GIF
            if messagebox.askyesno("完成", f"GIF已成功創建!\n\n要現在打開查看嗎?"):
                self.open_gif(full_output_path)
        
        except Exception as e:
            self.progress_var.set(0)
            self.status_var.set("創建失敗")
            messagebox.showerror("錯誤", f"創建GIF時發生錯誤: {str(e)}")
    
    def open_gif(self, gif_path):
        try:
            import platform
            import subprocess
            
            system = platform.system()
            
            if system == "Darwin":  # macOS
                subprocess.call(["open", gif_path])
            elif system == "Windows":
                os.startfile(gif_path)
            else:  # Linux
                subprocess.call(["xdg-open", gif_path])
        except Exception as e:
            messagebox.showerror("錯誤", f"無法打開GIF: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GifMakerApp(root)
    root.mainloop()