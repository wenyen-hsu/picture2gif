from PIL import Image
import os
import glob

def create_gif_from_images(image_folder, output_gif_name, duration=100):
    """
    將資料夾中的圖片轉換成GIF動畫
    
    參數:
        image_folder: 包含圖片的資料夾路徑
        output_gif_name: 輸出GIF檔案名稱
        duration: 每幀的持續時間(毫秒)
    """
    # 確保輸出檔名有.gif擴展名
    if not output_gif_name.lower().endswith('.gif'):
        output_gif_name += '.gif'
        
    # 取得資料夾中所有圖片
    image_files = sorted(glob.glob(f"{image_folder}/*.jpg") + 
                         glob.glob(f"{image_folder}/*.jpeg") + 
                         glob.glob(f"{image_folder}/*.png") + 
                         glob.glob(f"{image_folder}/*.bmp"))
    
    if not image_files:
        print(f"在 {image_folder} 中找不到圖片檔案")
        return
    
    # 開啟所有圖片
    images = []
    for image_file in image_files:
        img = Image.open(image_file)
        images.append(img)
    
    # 儲存為GIF
    images[0].save(
        output_gif_name,
        save_all=True,
        append_images=images[1:],
        optimize=False,
        duration=duration,
        loop=0  # 0表示無限循環
    )
    
    print(f"GIF已成功創建: {output_gif_name}")

# 使用範例
if __name__ == "__main__":
    folder_path = input("請輸入包含圖片的資料夾路徑: ")
    output_name = input("請輸入輸出GIF檔名: ")
    frame_duration = int(input("請輸入每幀的持續時間(毫秒)(預設100): ") or "100")
    
    create_gif_from_images(folder_path, output_name, frame_duration)