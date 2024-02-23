import matplotlib.pyplot as plt
import matplotlib.style
import pandas as pd
import japanize_matplotlib
from str_abc import Str_Abc
matplotlib.style.use("ggplot")

class GraphGenerator(Str_Abc):
    def __init__(self, csv_file=None,key = None,grah_name = None):
        self.csv_file1 = csv_file
        self.key = key
        self.grah_name = ""
        self.key = ""  # キーを初期化
        self.title = ""  # タイトルを初期化
    
    def  __str__(self):
        return "与えられたcsvファイル、キー、タイトルでグラフを作成します。"
        
    def extraction_single_csv(self, csv_file=None,column_name = None):
        df = pd.read_csv(csv_file)
        if column_name is None:
            column_name = self.key  # ユーザーが列名を指定しない場合、self.key を使用
        try:
            # 入力された列名を使用してデータを抽出
            column_from_csv = df[column_name]
            
            # データを返却
            return column_from_csv
        except KeyError:
            print("エラー: 指定された列名が存在しません。")
            return None
        
    def plot_bar_chart(self, data):
        plt.bar(data.index, data.values)
        plt.xlabel('X軸')
        plt.ylabel('Y軸')
        if self.grah_name is None:
            plt.title(input("グラフのタイトルを入力してください: "))
        else:
            plt.title(self.grah_name)    
        plt.show()
