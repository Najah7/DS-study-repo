import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import japanize_matplotlib

def display_two_histograms(data1, data2, bins=10):
    """2つのヒストグラムを表示する関数"""
    plt.figure(figsize=(10, 4))
    # NOTE: 描画するグラム全体の行、描画するグラフ全体の列、〇個目のグラフ
    plt.subplot(1, 2, 1)
    sns.distplot(data1, bins=bins)
    plt.subplot(1, 2, 2)
    sns.distplot(data2, bins=bins)
    plt.tight_layout()