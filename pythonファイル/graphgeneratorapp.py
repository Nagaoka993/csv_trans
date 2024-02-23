import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import matplotlib.pyplot as plt
import pandas as pd
import japanize_matplotlib
from graphgenerator import GraphGenerator
from str_abc import Str_Abc
import os

class GraphGeneratorApp(Str_Abc):
    def __init__(self, root):
        self.root = root
        self.root.title("お手軽データ分析くん")
        self.root.geometry("600x400")

        # グラフ生成クラスのインスタンスを作成
        self.graph_generator = GraphGenerator()
        
        # 初期化
        self.filename = ""  # ファイル名を初期化


        # CSVファイルを選択するボタンを追加
        self.csv_file_label = ttk.Label(root, text="CSVファイルを選択:")
        self.csv_file_label.pack()

        self.csv_file_entry = ttk.Entry(root)
        self.csv_file_entry.pack()

        self.browse_button = ttk.Button(root, text="参照", command=self.browse_csv)
        self.browse_button.pack()

        # 列名を入力するエントリウィジェットを追加
        self.column_name_label = ttk.Label(root, text="Keyを入力:")
        self.column_name_label.pack()

        self.column_name_entry = ttk.Entry(root)  # 列名を入力するエントリウィジェット
        self.column_name_entry.pack()

        # グラフのタイトルを入力するエントリウィジェットを追加
        self.graph_title_label = ttk.Label(root, text="グラフのタイトルを入力:")
        self.graph_title_label.pack()

        self.graph_title_entry = ttk.Entry(root)  # グラフのタイトルを入力するエントリウィジェット
        self.graph_title_entry.pack()
        # 保存ボタンを追加
        self.save_button = ttk.Button(root, text="データを保存", command=self.save_data)
        self.save_button.pack()

        # グラフ生成ボタンを追加
        self.generate_button = ttk.Button(root, text="グラフ生成", command=self.generate_graph)
        self.generate_button.pack()

    def browse_csv(self):
        # ファイルダイアログを表示してCSVファイルを選択
        csv_file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.csv_file_entry.delete(0, tk.END)
        self.csv_file_entry.insert(0, csv_file)

        # 選択されたCSVファイルのパスをグラフ生成クラスに渡す
        self.graph_generator.csv_file1 = csv_file
    def __str__(self):
        return "GUIでcsvファイル、キー、タイトルを入力させ、Graphgeneratorのインスタンスを作成します"

    def generate_graph(self):
        # グラフ生成クラスからCSVファイルのパスを取得
        csv_file = self.graph_generator.csv_file1
        if csv_file:
            # 列名を入力
            column_name = self.column_name_entry.get()

            if not column_name:
                print("エラー: 列名を入力してください。")
                return

            if csv_file:
                data1 = self.graph_generator.extraction_single_csv(csv_file, column_name)  # csv_file と列名を引数として渡す

                if data1 is not None:
                    # グラフのタイトルを入力
                    graph_title = self.graph_title_entry.get()

                    if not graph_title:
                        graph_title = "グラフ"

                    # バーチャートを表示
                    plt.bar(data1.index, data1.values)
                    plt.xlabel('X軸')
                    plt.ylabel('Y軸')
                    plt.title(graph_title)
                    plt.show()
    def save_data(self):
        # ファイル名、キー、タイトルを取得
        self.filename = self.csv_file_entry.get()
        self.key = self.column_name_entry.get()
        self.title = self.graph_title_entry.get()

        if not self.filename or not self.key:
            print("エラー: ファイル名とキーは必須です。")
            return

        # ファイルに保存
        # ここでファイル名、キー、タイトルを保存する処理を実行
        # 例: ファイル名を 'log_csv.txt' に保存する場合
        with open('log.txt', 'w',encoding='utf-8') as file:
            file.write(f"ファイル名: {self.filename}\n")
            file.write(f"キー: {self.key}\n")
            file.write(f"タイトル: {self.title}\n")
            print("データを保存しました。")


        print(f"ファイル名: {self.filename}, キー: {self.key}, タイトル: {self.title} をファイルに保存しました。")


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGeneratorApp(root)
    root.mainloop()
