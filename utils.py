# utils.py
import pandas as pd
import os

def concat_data(folder_path, save_path):
    all_data = []
    
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder_path, file)
            df = pd.read_excel(file_path)
            all_data.append(df)
    
    merged_df = pd.concat(all_data, ignore_index=True, join='outer')
    output_path = os.path.join(save_path, "合并结果.xlsx")
    merged_df.to_excel(output_path, index=False)
    
    print(f"合并完成！共 {len(merged_df)} 行数据")
    print(f"保存位置: {output_path}")
