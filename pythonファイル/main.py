import tkinter as tk
from graphgeneratorapp import GraphGeneratorApp  # GraphGeneratorAppのクラスをインポート

class Main(GraphGeneratorApp):
    def __init__(self):
        self.create_and_run_app_init()

    def create_and_run_app_init(self):
        root = tk.Tk() # tkinterのウィンドウを作成
        app = GraphGeneratorApp(root)  # アプリケーションのインスタンスを生成
        root.mainloop() # アプリケーションを実行し、ウィンドウを表示

"""
外部ライブラリ
    tkinter:pip install tk
    matplotlib:pip install matplotlib
    pandas:pip install pandas
    japanize_matplotlib（日本語フォントのために使用されているものです）:pip install japanize-matplotlib
サンプルcsv,key,タイトル
    'severe_cases_daily.csv',ALL,'コロナの重症患者の推移'

過去に調べたデータをもう一度使用したい場合、log_csvを確認し手入力してください

"""