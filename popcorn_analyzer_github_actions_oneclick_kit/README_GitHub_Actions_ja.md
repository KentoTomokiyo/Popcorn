# Popcorn Analyzer: GitHub Actions で Windows ワンクリック版を作る

このキットを GitHub に置いて Actions を 1 回実行すると、Windows 用の配布フォルダが作られます。

## できること
- Mac に Windows や Python を入れなくてよい
- GitHub の Windows ランナー上で自動ビルド
- 完成物は `PopcornAnalyzer.exe` を含む配布フォルダ
- 使う人は Windows でダブルクリックするだけ

## 手順
1. GitHub で新しいリポジトリを作る
2. このキットの中身をそのままアップロードする
3. GitHub の **Actions** タブを開く
4. **Build Windows one-click app** を選ぶ
5. **Run workflow** を押す
6. 完了後、Artifacts から **PopcornAnalyzer-Windows** をダウンロードする
7. 展開後のフォルダをそのまま Windows ユーザーに渡す

## 含まれるもの
- `.github/workflows/build-windows.yml`
- `PopcornAnalyzer.spec`
- `popcorn_analyzer_windows_easy.py`
- `requirements.txt`

## メモ
- ワークフローは Windows 上で PyInstaller を実行します
- ワークフロー内で FFmpeg の Windows ビルドを取得して同梱します
- 配布時は **フォルダごと** 渡してください
