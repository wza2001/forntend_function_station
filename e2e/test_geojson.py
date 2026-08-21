import json
import pandas as pd
import numpy as np

geojson_path = "public/abudhabi_city_buildings.geojson"

try:
    with open(geojson_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    features = data.get("features", [])
    total_features = len(features)
    print(f"=== 要素总数: {total_features} ===")

    if total_features == 0:
        print("错误: GeoJSON 中无有效要素。")
        exit()

    # 提取 properties
    props_list = [f.get("properties", {}) for f in features]
    df = pd.DataFrame(props_list)

    print("\n--- 现有字段列表 ---")
    print(list(df.columns))

    # 检查常见高度字段
    candidate_cols = ["height", "elevation", "building:levels", "levels", "render_height"]
    found_cols = [c for c in candidate_cols if c in df.columns]
    print(f"\n匹配到的高度相关字段: {found_cols}")

    for col in found_cols:
        print(f"\n================ 字段: [{col}] 分析 ================")
        raw_series = df[col]

        # 1. 数据类型与空值
        types_count = raw_series.map(lambda x: type(x).__name__).value_counts().to_dict()
        null_count = raw_series.isna().sum() + (raw_series == "").sum()
        null_ratio = (null_count / total_features) * 100

        print(f"数据类型分布: {types_count}")
        print(f"空值/缺失数量: {null_count} / {total_features} ({null_ratio:.2f}%)")

        # 2. 转换为数值后统计分布
        numeric_series = pd.to_numeric(raw_series, errors="coerce").dropna()

        if len(numeric_series) > 0:
            print(f"有效数值样本数: {len(numeric_series)}")
            print("数值统计摘要 (五数概括):")
            print(numeric_series.describe().to_string())

            # 打印高度分段分布
            bins = [0, 15, 30, 50, 100, 200, np.inf]
            labels = ["0-15m", "15-30m", "30-50m", "50-100m", "100-200m", ">200m"]
            cuts = pd.cut(numeric_series, bins=bins, labels=labels, right=False)
            print("\n分段区间分布:")
            print(cuts.value_counts().sort_index().to_string())
        else:
            print("警告: 该字段未解析出任何有效数值！")

    # 打印前 3 个要素的原始属性样本
    print("\n--- 前 3 个要素属性样本 ---")
    for i, p in enumerate(props_list[:3]):
        print(f"Sample {i + 1}: {p}")

except FileNotFoundError:
    print(f"错误: 找不到文件 {geojson_path}，请确认路径是否正确。")
except Exception as e:
    print(f"分析出错: {e}")