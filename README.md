Python File Organizer CLI

📌 概要
このツールは、指定されたディレクトリ内のファイルを拡張子に基づいて自動的に仕分け・整理するためのコマンドラインツールです。
「設定の外部化」と「安全な実行」をコンセプトに設計されています。

✨ 特徴
YAMLによる柔軟な設定: プログラムを書き換えることなく、設定ファイル（config.yaml）を編集するだけで整理ルールをカスタマイズできます。

Dry Run（テスト実行）機能: 実際にファイルを移動する前に、どのファイルがどこへ移動されるかのシミュレーション結果を確認できる安全設計です。

堅牢なパス操作: Pythonの pathlib ライブラリを使用し、OSに依存しない正確なファイル操作を実現しています。

🚀 使い方
1. インストール
リポジトリをクローンし、必要なライブラリをインストールします。

Bash
git clone https://github.com/Sante-HO/smart-sort.git
cd smart-sort
pip install PyYAML
2. 設定（config.yaml）
config.yaml を編集して、整理ルールを定義します。

YAML
target_dir: "."      # 整理したいフォルダのパス
dry_run: true        # trueならシミュレーションのみ、falseで実際に移動
3. 実行
Bash
python main.py
🛠 技術スタック
Language: Python 3.12+

Libraries:

PyYAML: 設定ファイルの解析

pathlib: オブジェクト指向なパス操作

shutil: 高レベルなファイル移動処理

🧠 設計思想
安全性: 破壊的なファイル操作（移動）を行う前に、ユーザーが必ず結果を予測できる「Dry Run」機能を標準搭載しました。

保守性: 整理ルールをコードから分離し、YAML形式で管理することで、非エンジニアでもメンテナンスしやすい構成にしています。
