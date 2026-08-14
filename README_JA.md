# 🎨 Pseudo-3D Image Augmentation App (日本語版)

[English Version (README_EN.md)](./README_EN.md) | **日本語版 (README_JA.md)**  
🚀 **Webアプリ公開ページ**: [🌐 日本語版を起動 (index_ja.html)](https://keinagaokaeng.github.io/Pseudo-3D-Image-Augmentation-App/index_ja.html) | [🌐 English Version (index_en.html)](https://keinagaokaeng.github.io/Pseudo-3D-Image-Augmentation-App/index_en.html)

> **汎用擬似 3D 体積モデリング・回転変調データ拡張 & YOLO data.yaml 自動生成アノテーションツール**  
> *A Universal Pseudo-3D Volumetric Pseudo-Geometry Modeling & Automated Rotation-Augmented Annotation App with Auto-Generated YOLO data.yaml*

[![HTML5 / WebGL](https://img.shields.io/badge/Tech-WebGL%2FThree.js-blue.svg)](https://threejs.org/)
[![OpenCV](https://img.shields.io/badge/Backend-OpenCV%20Python-green.svg)](https://opencv.org/)
[![YOLO Support](https://img.shields.io/badge/Dataset-YOLO%20Format%20%2B%20data.yaml-orange.svg)](https://docs.ultralytics.com/)
[![License](https://img.shields.io/badge/License-MIT-purple.svg)](#license)

<p align="center">
  <img src="./Screenshot.png" alt="Pseudo-3D Image Augmentation App UI" width="100%">
</p>

---

## 📌 概要 (Overview)

**Pseudo-3D Image Augmentation App** は、あらゆる対象物（生物、工業製品、自動車、電子部品、動物、人物、各種オブジェクト等）の単一 2D 写真から、**3D 立体空間における被写体の擬似幾何変形（Pseudo-3D Deformation）・3 軸全方向回転（Yaw / Pitch / Roll）を再現し、多アングルの教師データセットを効率的に生成するための汎用アノテーション＆データ拡張アプリ**です。

---

## 🔬 背景 & データ不均衡の解消 (Background & Augmentation Benefits)

物体検出（YOLOv8/v9/v10/v11/26 等）の学習において、**特定のアングル写真（正面等）に偏ったデータセットでは、撮影角度が変わった際の認識率が著しく低下する課題**が発生します。

本アプリは、追加の物理撮影を行うことなく、1枚の単一アングル写真から高精度なマルチアングル教師データを増幅・拡張し、AI モデルの汎化性能（Generalization Performance）と検出精度を劇的に向上させます。

---

## 🌟 主な機能 (Key Features)

### 1. 🏷️ YOLO クラス設定 UI (Class ID & Class Name)
* アプリのサイドバーから **`YOLO Class ID` (数値: `0`, `1`, `2`, ...)** および **`Class Name` (名前: `car`, `jellyfish`, `component`, etc.)** を自由に手動指定・変更可能。
* ユーザーが独自の画像や異なるカテゴリの物体を読み込ませた際にも、即座に指定したラベル情報がアノテーションデータに反映されます。

### 2. 📄 YOLO 標準 `data.yaml` の生成 & ZIP 一括出力
* 教師データセット ZIP を出力する際、画像 (`/images/`) やラベル (`/labels/`) だけでなく、**YOLO 学習に必要な標準定義ファイル `data.yaml` を構築・同封出力**します。

```yaml
# Pseudo-3D Image Augmentation App Generated YOLO Dataset Config
path: ./
train: images
val: images

names:
  0: "jellyfish"
```
* 解凍するだけで、Ultralytics YOLO (v8 / v9 / v10 / v11 / 26 等) の学習パイプラインへそのまま投入可能です！

### 3. 🖼️ RGBA 透明被写体 ＋ CV2 Inpaint 補元背景の 2 レイヤー合成
* OpenCV の `cv2.inpaint` (Telea) で修復した背景と、4 チャンネル RGBA 透明被写体を分離し、Three.js 上で 2 レイヤー合成。

### 4. 🌸 5点多重ノード立体モデリング膨らみエンジン (Volumetric Deformation)
* 被写体の中央主頂点（Dome Depth）と外側 4 点の周辺膨らみ（Shoulders Depth / Radius / Apex Shift）を独立制御し、リアルな奥行きとガウシアン立体膨らみを付与。

### 5. 🤖 3D自動連続キャプチャー & 角度変調データ拡張 (Auto Batch Capture)
* **`🚀 20枚自動 Yaw連写 (ΔYaw=+1.0°)` [ショートカット: `Y`]**
* **`🚀 20枚自動 Pitch連写 (ΔPitch=+1.0°)` [ショートカット: `P`]**
* **`🚀 20枚自動 Roll連写 (ΔRoll=+1.0°)` [ショートカット: `R`]**
* **`🌀 複合カスタム自動連写` [ショートカット: `Shift + A`]**

### 6. 📐 3D回転追従 BBox パース自動伸縮エンジン
* 3D 回転に伴い、カメラ手前方向に接近する BBox 枠を自動拡大し、奥に遠ざかる枠を自動縮小。

### 7. 🔴 赤色 BBox 枠線投影 & CVAT 風ドラッグ直感補正
* アノテーション赤色 BBox 枠線 (`#ef4444`) を投影し、クラス情報 (Class ID: Class Name) と共にリアルタイム表示。

### 8. 📦 キャプチャーログ管理 Modal & ボツ画像 `✕` 削除
* 取得ログを一覧表示し、ホバーで大画面プレビュー。ボツ画像は **`✕` ボタン** または **キーボード `[X]` / `[Delete]`** で削除。

---

## ⌨️ キーボードショートカット一覧 (Keyboard Shortcuts)

| ショートカットキー | 実行アクション |
| :--- | :--- |
| **`[C]`** | 📸 単一アノテーション画像の保存 (1.1x クロップ + YOLO `.txt`) |
| **`[Y]`** | 🚀 20枚自動 Yaw 連続キャプチャー実行 (ΔYaw = +1.0°) |
| **`[P]`** | 🚀 20枚自動 Pitch 連続キャプチャー実行 (ΔPitch = +1.0°) |
| **`[R]`** | 🚀 20枚自動 Roll 連続キャプチャー実行 (ΔRoll = +1.0°) |
| **`[Shift + A]`** | 🌀 複合カスタム自動連続キャプチャー実行 |
| **`[X]` / `[Delete]`** | 🗑️ ホバー中または最新のボツキャプチャーログを削除 |

---

## 🛠️ スタンドアローン構成 & ディレクトリ構成 (Directory Structure)

本アプリは外部サーバーやインターネット接続を必要とせず、主要ブラウザ（Chrome / Safari / Edge / Firefox）でそのまま動作する完全スタンドアローン設計です。

### ディレクトリ構成
```text
Github/
├── index.html                             # トップアクセス用 (GitHub Pages ルート)
├── index_ja.html                          # 🇯🇵 日本語版 Web アプリ (公開ページ)
├── index_en.html                          # 🇺🇸 英語版 Web アプリ (公開ページ)
├── pseudo_3d_image_augmentation_app_ja.html # 🇯🇵 日本語版 スタンドアローン HTML
├── pseudo_3d_image_augmentation_app_en.html # 🇺🇸 英語版 スタンドアローン HTML
├── build_3d_tool.py                       # Python 自動データセット ビルドスクリプト
├── README.md                              # GitHub トップ用 ドキュメント
├── README_JA.md                           # 🇯🇵 日本語 ドキュメント
├── README_EN.md                           # 🇺🇸 英語 ドキュメント
└── Screenshot.png                         # アプリ画面スクリーンショット
```

---

## 🚀 使い方 (Quick Start Guide)

1. **アプリの起動**:
   [`index_ja.html`](https://keinagaokaeng.github.io/Pseudo-3D-Image-Augmentation-App/index_ja.html) （または英語版 [`index_en.html`](https://keinagaokaeng.github.io/Pseudo-3D-Image-Augmentation-App/index_en.html)）をブラウザで開きます。
2. **クラス情報および画像の読み込み**:
   「🏷️ YOLO アノテーション設定」で Class ID と Class Name を入力し、「📥 好きな画像をドラッグ＆ドロップ」エリアに自分の画像を読み込ませます。
3. **立体化とデータ生成**:
   「🌸 5点多重ノード」で立体感を出し、「🚀 20枚自動 Yaw連写」等でデータ拡張を行います。
4. **ZIP データセットのダウンロード**:
   「📦 ログ一括を教師データセット(ZIP)として出力」を押して保存すると、`images/`, `labels/`, および `data.yaml` がパックされた ZIP がダウンロードされます。

---

## 📝 引用 (Citation)

```bibtex
@misc{pseudo_3d_image_augmentation_app_2026,
  author = {Kei Nagaoka},
  title = {Pseudo-3D Image Augmentation App: A Universal Pseudo-3D Volumetric Pseudo-Geometry Modeling & Automated Rotation-Augmented Annotation App with Auto-Generated YOLO data.yaml},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/your-username/Pseudo-3D-Image-Augmentation-App}}
}
```

---

## 📜 ライセンス (License)

Distributed under the MIT License.
