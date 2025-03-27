# picture2gif
transfer series of pictures to gif
# 圖片轉GIF工具

這是一個簡單的Python工具，可以將一系列圖片轉換成GIF動畫。

## 功能

- 支援多種圖片格式（JPG, JPEG, PNG, BMP）
- 自定義每幀的持續時間
- 按照檔名順序自動排序圖片
- 創建無限循環的GIF動畫

## 安裝需求

使用前，請確保已安裝Python和必要的依賴庫：

```bash
pip install Pillow
```

## 使用方式

1. 將所有要轉換的圖片放在同一個資料夾中
2. 執行程式：
   ```bash
   python image_to_gif.py
   ```
3. 依照提示輸入：
   - 包含圖片的資料夾路徑
   - 輸出GIF檔案的名稱
   - 每幀的持續時間（毫秒）

## 範例

```bash
請輸入包含圖片的資料夾路徑: ./my_images
請輸入輸出GIF檔名: animation.gif
請輸入每幀的持續時間(毫秒)(預設100): 150
GIF已成功創建: animation.gif
用open -a Safari animation.gif打開
也可使用python gif_maker_gui.py用gui操作
```

## 注意事項

- 圖片會按照檔名的字母順序排序
- 建議使用相同尺寸的圖片以獲得最佳效果
- 如果圖片數量過多或尺寸過大，可能需要較長的處理時間

## 授權

此程式不用授權隨便使用

## 貢獻

歡迎提交問題報告或改進建議！