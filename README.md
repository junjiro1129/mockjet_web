# MOCKJET – Instantly Generate 100+ Print-on-Demand Mockups
<p align="center">
  <!-- ⭐ Stars -->
  <a href="https://github.com/junjiro1129/mockjet_web/stargazers">
    <img src="https://img.shields.io/github/stars/junjiro1129/mockjet_web?style=social" alt="GitHub Stars"/>
  </a>
  <!-- 📝 License -->
  <a href="https://github.com/junjiro1129/mockjet_web/LICENSE">
    <img src="https://img.shields.io/github/license/junjiro1129/mockjet_web" alt="License"/>
  </a>
  <!-- 🔖 Release -->
  <a href="https://github.com/junjiro1129/mockjet_web/releases/latest">
    <img src="https://img.shields.io/github/v/release/junjiro1129/mockjet_web" alt="Latest release"/>
  </a>
  <!-- 🚀 Live Demo -->
  <a href="https://mockjet-web.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/Live%20Demo-Streamlit-orange?logo=streamlit" alt="Live demo on Streamlit Cloud"/>
  </a>
  <!-- 🐍 Python -->
  <img src="https://img.shields.io/badge/python-3.9+-blue" alt="Python 3.9+"/>
</p>

---

## 1. Quick Start & Live Demo

**Experience the power of MOCKJET instantly with the built-in DemoKit!**

1. **Download and unzip this repository.**
2. **Open the `demokit/` folder:**  
   - Contains two sample base images (with pre‑mapped print areas)  
   - Two design images  
   - A ready‑to‑use `templates.json`
3. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the web app:**
   ```bash
   streamlit run app.py
   ```
5. **In the app:**  
   - Drag & drop the sample base images, design images, and `templates.json` from `demokit/`
   - Click **Generate Mockups**
6. **Your mockups will be generated in seconds and saved in the `mockups/` folder!**

[▶️ Watch the demo video (mockup_web_demo.mp4)](demokit/mockup_web_demo.mp4)

*After you’ve tried the DemoKit, swap in your own images and base files using `coordinatemaker.html` for production use!*

---

## 2. What is MOCKJET?

MOCKJET is a blazing‑fast, no‑code web app for generating hundreds of high‑quality mockup images for Print‑on‑Demand (POD) products.  
No Photoshop, no technical skills required.  
Simply set your print areas visually, upload your designs, and generate perfectly‑aligned mockups for Etsy, Shopify, Redbubble, and more — all within your browser.

---

## 3. Features

- **Ultra‑fast batch mockup generation** (hundreds in seconds)  
- **No code, no Photoshop required** – 100 % browser‑based  
- **Interactive print area mapping** with `coordinatemaker.html`  
- **Supports multiple base images** in one session  
- **Automatic perfect alignment** for all designs  
- **PNG, JPG, JPEG compatible** for both bases and designs  
- **Instant DemoKit** for out‑of‑the‑box experience  
- **Cross‑platform** – works on Windows, Mac, Linux (with Python)  
- **Ideal for POD sellers:** Etsy, Shopify, Redbubble, and more  

---

## 4. Usage & Customization

### 4.1 Preparing Your Own Images
- **Base Images:** Product photos as mockup bases (T‑shirts, tote bags, mugs, etc.). Formats: PNG, JPG, JPEG.  
- **Design Images:** Artwork/designs in PNG, JPG, or JPEG. Transparent PNGs recommended.

### 4.2 Mapping Print Areas with `coordinatemaker.html`
1. Open `coordinatemaker.html` in your browser.  
2. Upload each base image and click the four corners of the printable area.  
3. Add/edit/delete bases as needed.  
4. Export all areas as a single `templates.json`.

### 4.3 Generating Mockups
```bash
streamlit run app.py
```
Drag & drop your base images, designs, and `templates.json`, then click **Generate Mockups**. Results are saved to `mockups/`.

---

## 5. Folder / File Structure
```
mockjet_web/
├── app.py
├── requirements.txt
├── coordinatemaker.html
├── demokit/
│   ├── templates.json
│   ├── bases/
│   │   ├── bag_sumple.jpg
│   │   └── mockup_base.png
│   ├── designs/
│   │   ├── sample_design1.jpg
│   │   └── sample_design2.png
│   └── mockup_web_demo.mp4
├
```
*Only `app.py`, `requirements.txt`, and `coordinatemaker.html` are required for your own projects. The DemoKit is for instant hands‑on experience.*

---

## 6. FAQ / Troubleshooting
**App error?** Ensure `pip install -r requirements.txt` was run and Python 3.8+ is used.  
**Misaligned images?** Re‑check print‑area clicks in `coordinatemaker.html`.  
**Files don’t appear?** Confirm PNG/JPG/JPEG format and use drag‑and‑drop upload.  
**Add more bases/designs?** Unlimited — just upload more and map new areas.

---

## 7. License & Support
**License:** MIT – free for personal & commercial use. Redistribution of the app itself is not allowed.  
**Contact:** junjiro1129@gmail.com (Discord coming soon!)

---

*Create, customize, and launch your own POD mockups with MOCKJET – the fastest way from design to shop!*
