import streamlit as st
import zipfile
import tempfile
import shutil
import os
import json
from PIL import Image
import numpy as np
import cv2
from io import BytesIO

st.set_page_config(page_title="MOCKJET – 100+ Mockups in Seconds", layout="wide")
st.title("🚀 MOCKJET - 100+ Mockups in Seconds")
st.write("Upload your base mockups and design images to generate product mockups in seconds!")

# --- ファイル保存用ディレクトリ
TMP_ROOT = tempfile.mkdtemp()
BASES_DIR = os.path.join(TMP_ROOT, "bases")
DESIGNS_DIR = os.path.join(TMP_ROOT, "designs")
OUT_DIR = os.path.join(TMP_ROOT, "out")
os.makedirs(BASES_DIR, exist_ok=True)
os.makedirs(DESIGNS_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)

# --- Helper: 画像ファイル保存
def save_uploaded_files(files, save_dir):
    valid_ext = [".png", ".jpg", ".jpeg"]
    saved_paths = []
    for uploaded_file in files:
        fname = uploaded_file.name
        ext = os.path.splitext(fname)[1].lower()
        if ext in valid_ext:
            out_path = os.path.join(save_dir, fname)
            with open(out_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            saved_paths.append(out_path)
        elif ext == ".zip":
            # ZIP解凍
            with zipfile.ZipFile(uploaded_file, "r") as zip_ref:
                for zipinfo in zip_ref.infolist():
                    ext2 = os.path.splitext(zipinfo.filename)[1].lower()
                    if ext2 in valid_ext:
                        zip_ref.extract(zipinfo, save_dir)
                        saved_paths.append(os.path.join(save_dir, zipinfo.filename))
    return saved_paths

# --- ファイルアップロードUI
st.header("Upload Mockup Bases (ZIP or PNG/JPG/JPEG files)")
bases_files = st.file_uploader("Upload base files", type=["png", "jpg", "jpeg", "zip"], accept_multiple_files=True)

st.header("Upload Design Images (.png, .jpg, .jpeg)")
design_files = st.file_uploader("Upload design files", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

st.header("Upload templates.json (coordinates of print area)")
templates_file = st.file_uploader("Upload templates.json", type=["json"])

# --- ファイル保存
bases_paths, designs_paths = [], []
if bases_files:
    bases_paths = save_uploaded_files(bases_files, BASES_DIR)
if design_files:
    designs_paths = save_uploaded_files(design_files, DESIGNS_DIR)

# --- templates.jsonロード
templates = None
if templates_file is not None:
    templates = json.load(templates_file)

# --- 画像表示
if bases_paths:
    st.subheader("Mockup Bases")
    num_cols = 6
    cols = st.columns(num_cols)
    for idx, img_path in enumerate(bases_paths):
        with cols[idx % num_cols]:
            st.image(img_path, caption=os.path.basename(img_path), width=180)

if designs_paths:
    st.subheader("Design Images")
    num_cols2 = 6
    cols2 = st.columns(num_cols2)
    for idx, img_path in enumerate(designs_paths):
        with cols2[idx % num_cols2]:
            st.image(img_path, caption=os.path.basename(img_path), width=180)

# --- 縦横比維持でワープ貼付
def warp_design_onto_mockup_fit(base_img, design_img, coords):
    base_cv = np.array(base_img.convert("RGBA"))
    design_cv = np.array(design_img.convert("RGBA"))
    h_des, w_des = design_cv.shape[:2]

    pts_dst = np.array(coords, dtype=np.float32)

    # 外接長方形
    widthA = np.linalg.norm(pts_dst[0] - pts_dst[1])
    widthB = np.linalg.norm(pts_dst[3] - pts_dst[2])
    maxWidth = int(max(widthA, widthB))

    heightA = np.linalg.norm(pts_dst[0] - pts_dst[3])
    heightB = np.linalg.norm(pts_dst[1] - pts_dst[2])
    maxHeight = int(max(heightA, heightB))

    # デザイン画像をアスペクト比維持でフィット
    scale = min(maxWidth / w_des, maxHeight / h_des)
    new_w = int(w_des * scale)
    new_h = int(h_des * scale)
    design_resized = cv2.resize(design_cv, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # 背景透明画像を中央配置
    design_bg = np.zeros((maxHeight, maxWidth, 4), dtype=np.uint8)
    x_offset = (maxWidth - new_w) // 2
    y_offset = (maxHeight - new_h) // 2
    design_bg[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = design_resized

    pts_src = np.array([[0,0],[maxWidth-1,0],[maxWidth-1,maxHeight-1],[0,maxHeight-1]], dtype=np.float32)

    M = cv2.getPerspectiveTransform(pts_src, pts_dst)
    warped = cv2.warpPerspective(design_bg, M, (base_cv.shape[1], base_cv.shape[0]), borderMode=cv2.BORDER_TRANSPARENT)

    mask = warped[:,:,3] > 0
    base_cv[mask] = warped[mask]
    return Image.fromarray(base_cv)

# --- モックアップ生成
output_images = []
if st.button("Generate Mockups") and bases_paths and designs_paths and templates:
    st.info("Generating mockups... Please wait.")

    for base_path in bases_paths:
        base_name = os.path.basename(base_path)
        if base_name not in templates:
            st.warning(f"{base_name} is not found in templates.json, skipping.")
            continue
        coords = templates[base_name]['print_area']
        # [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
        if isinstance(coords[0], dict):
            # もしdict形式なら変換
            coords = [[p[0], p[1]] for p in coords.values()]
        elif isinstance(coords[0], list):
            coords = coords
        else:
            st.warning("Invalid coords format.")
            continue

        for design_path in designs_paths:
            base_img = Image.open(base_path).convert("RGBA")
            design_img = Image.open(design_path).convert("RGBA")
            result_img = warp_design_onto_mockup_fit(base_img, design_img, coords)
            result_name = f"{os.path.splitext(base_name)[0]}_{os.path.splitext(os.path.basename(design_path))[0]}.png"
            result_path = os.path.join(OUT_DIR, result_name)
            result_img.save(result_path)
            output_images.append(result_path)

    st.success(f"Generated {len(output_images)} mockup images!")

# --- 生成画像表示＆ZIPダウンロード
if output_images:
    st.subheader("Generated Mockups")
    cols3 = st.columns(min(len(output_images), 4))
    for idx, out_img in enumerate(output_images):
        with cols3[idx % 4]:
            st.image(out_img, caption=os.path.basename(out_img), width=180)

    zip_buf = BytesIO()
    with zipfile.ZipFile(zip_buf, "w") as zipf:
        for img_path in output_images:
            zipf.write(img_path, os.path.basename(img_path))
    st.download_button("Download All as ZIP", zip_buf.getvalue(), file_name="mockups.zip", mime="application/zip")

# --- 後始末
def cleanup_tmp():
    shutil.rmtree(TMP_ROOT, ignore_errors=True)
import atexit
atexit.register(cleanup_tmp)
