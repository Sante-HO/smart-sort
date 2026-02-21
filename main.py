import yaml
import shutil
from pathlib import Path

# 1. 設定の読み込み
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

is_dry_run = config.get('dry_run', False) # 設定がなければFalseにする安全設計

print(f"--- {config['app_name']} 実行中 ---")
if is_dry_run:
    print("⚠️ 【重要】現在はDry Runモードです。実際の移動は行われません。")

rules = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".zip": "Archives"
}

target_dir = Path(config['target_dir'])

if not target_dir.exists():
    print("対象フォルダが見つかりません。")
else:
    for file_path in target_dir.iterdir():
        if file_path.is_file() and file_path.suffix in rules:
            folder_name = rules[file_path.suffix]
            dest_dir = target_dir / folder_name
            
            # ログメッセージの作成
            log_msg = f"[{folder_name}] {file_path.name}"
            
            if is_dry_run:
                # Dry Run時は表示だけ
                print(f" (シミュレーション) 移動予定: {log_msg}")
            else:
                # 本番時は実際にフォルダを作って移動
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(file_path), str(dest_dir / file_path.name))
                print(f" 実行済: {log_msg}")

print("--- 処理終了 ---")