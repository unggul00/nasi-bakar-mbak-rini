import streamlit as st
import urllib.parse
import os
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Nasi Bakar Pawon Mbak Rini",
    page_icon="🔥",
    layout="wide"
)

# ================= DARK THEME CSS =================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght=300;400;500;600;700;800&family=Playfair+Display:wght=600;700;800;900&display=swap');

/* ---------- Tokens ----------
bg base      : #0d0d0f
bg surface   : #17161a
bg surface-2 : #201e23
border       : #2b2930
text primary : #f5f1ea
text muted   : #9a938f
accent flame : #ff5a1f
accent amber : #ffb020
------------------------------ */

html, body, [class*="css"], .stMarkdown {
font-family: 'Plus Jakarta Sans', sans-serif;
}

.stApp {
background: #0d0d0f;
}

section[data-testid="stSidebar"] {
background: #131215;
}

/* ---------- Top bar ---------- */
.topbar {
display: flex;
align-items: center;
justify-content: space-between;
padding: 18px 8px 26px 8px;
border-bottom: 1px solid #221f24;
margin-bottom: 46px;
}

.topbar-brand {
font-family: 'Playfair Display', serif;
font-weight: 800;
font-size: 22px;
color: #f5f1ea;
letter-spacing: 0.2px;
}

.topbar-brand span {
color: #ff5a1f;
}

.topbar-actions {
display: flex;
gap: 12px;
}

.topbar-link {
color: #cfc9c2;
text-decoration: none;
font-size: 14px;
font-weight: 600;
padding: 10px 18px;
border-radius: 30px;
border: 1px solid #2b2930;
transition: all 0.25s ease;
}

.topbar-link:hover {
border-color: #ff5a1f;
color: #ff5a1f;
}

.topbar-cta {
background: linear-gradient(135deg, #ff5a1f 0%, #ffb020 100%);
color: #0d0d0f !important;
text-decoration: none;
font-size: 14px;
font-weight: 700;
padding: 10px 22px;
border-radius: 30px;
box-shadow: 0 4px 18px rgba(255, 90, 31, 0.25);
}

/* ---------- Hero ---------- */
.hero-container {
background: radial-gradient(circle at 80% 20%, #201c22 0%, #17161a 55%, #131215 100%);
border: 1px solid #221f24;
padding: 64px 56px;
border-radius: 28px;
margin-bottom: 70px;
}

.hero-flex {
display: flex;
align-items: center;
justify-content: space-between;
gap: 50px;
}

.hero-text {
flex: 1.1;
text-align: left;
}

.hero-eyebrow {
display: inline-block;
color: #ff5a1f;
font-size: 13px;
font-weight: 700;
letter-spacing: 2px;
text-transform: uppercase;
margin-bottom: 18px;
}

.hero-text h1 {
font-family: 'Playfair Display', serif;
font-size: 52px;
font-weight: 800;
color: #f5f1ea !important;
line-height: 1.15;
margin: 0 0 22px 0;
letter-spacing: -0.5px;
}

.hero-text p {
font-size: 17px;
color: #a39c96;
max-width: 480px;
margin: 0 0 34px 0;
line-height: 1.75;
}

.hero-btn-container {
display: flex;
gap: 14px;
flex-wrap: wrap;
}

.btn-primary {
background: linear-gradient(135deg, #ff5a1f 0%, #ffb020 100%);
color: #0d0d0f !important;
padding: 15px 34px;
border-radius: 50px;
text-decoration: none;
font-weight: 700;
font-size: 15px;
transition: all 0.3s ease;
box-shadow: 0 8px 22px rgba(255, 90, 31, 0.3);
display: inline-block;
}

.btn-primary:hover {
transform: translateY(-2px);
box-shadow: 0 10px 26px rgba(255, 90, 31, 0.4);
}

.btn-secondary {
background: transparent;
color: #f5f1ea !important;
padding: 15px 34px;
border-radius: 50px;
text-decoration: none;
font-weight: 600;
font-size: 15px;
transition: all 0.3s ease;
border: 1px solid #3a3640;
display: inline-block;
}

.btn-secondary:hover {
border-color: #ff5a1f;
color: #ff5a1f !important;
}

.ig-icon {
width: 16px;
height: 16px;
vertical-align: -3px;
margin-right: 2px;
color: currentColor;
}

.hero-image {
flex: 0.9;
display: flex;
justify-content: center;
align-items: center;
position: relative;
}

.hero-image::before {
content: "";
position: absolute;
width: 260px;
height: 260px;
background: radial-gradient(circle, rgba(255,90,31,0.35) 0%, rgba(255,90,31,0) 70%);
z-index: 0;
}

.hero-logo {
max-width: 240px;
height: auto;
position: relative;
z-index: 1;
filter: drop-shadow(0 10px 30px rgba(0,0,0,0.5));
}

/* ---------- Section styling ---------- */
.section-title {
text-align: left;
font-family: 'Playfair Display', serif;
font-size: 30px;
font-weight: 700;
color: #f5f1ea;
margin-top: 10px;
margin-bottom: 6px;
}

.section-sub {
text-align: left;
color: #8f8781;
font-size: 15px;
margin-bottom: 32px;
}

/* ---------- Feature / value cards ---------- */
.custom-card {
background: #17161a;
border: 1px solid #242127;
border-radius: 18px;
padding: 30px;
height: 100%;
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.custom-card:hover {
transform: translateY(-4px);
border-color: #ff5a1f;
box-shadow: 0 16px 32px rgba(0,0,0,0.35);
}

.card-icon {
width: 46px;
height: 46px;
border-radius: 50%;
border: 1.5px solid #ff5a1f;
color: #ff5a1f;
display: flex;
align-items: center;
justify-content: center;
font-size: 20px;
margin-bottom: 18px;
}

.custom-card h3 {
font-family: 'Playfair Display', serif;
color: #f5f1ea;
font-size: 19px;
margin-bottom: 10px;
font-weight: 700;
}

.custom-card p {
color: #9a938f;
font-size: 14.5px;
line-height: 1.65;
margin: 0;
}

.custom-price {
margin-top: 18px;
font-size: 21px;
font-weight: 700;
color: #ffb020;
}

.menu-thumb {
width: 54px;
height: 54px;
border-radius: 14px;
background: linear-gradient(135deg, #ff5a1f 0%, #ffb020 100%);
display: flex;
align-items: center;
justify-content: center;
font-size: 26px;
margin-bottom: 16px;
}

/* ---------- Info banner (Jam Operasional) ---------- */
.info-banner {
background: linear-gradient(120deg, #ff5a1f 0%, #ffb020 100%);
color: #17140f;
border-radius: 22px;
padding: 38px;
text-align: center;
margin: 60px 0;
box-shadow: 0 20px 45px rgba(255, 90, 31, 0.2);
}

.info-banner h3 {
color: #3a1c05 !important;
font-size: 14px;
font-weight: 700;
letter-spacing: 2px;
text-transform: uppercase;
margin-bottom: 10px;
opacity: 0.85;
}

.info-banner h2 {
color: #17140f !important;
font-family: 'Playfair Display', serif;
font-size: 26px;
font-weight: 800;
margin-bottom: 4px;
}

.info-banner h1 {
color: #17140f !important;
font-size: 42px;
font-weight: 800;
margin-bottom: 8px;
}

.info-banner .info-note {
color: #3a1c05;
margin-top: 8px;
font-size: 14px;
opacity: 0.85;
}

/* ---------- Form ---------- */
div[data-testid="stForm"] {
background: #17161a !important;
padding: 40px !important;
border-radius: 22px !important;
border: 1px solid #242127 !important;
}

label, .stMarkdown p {
color: #d8d3cd !important;
font-weight: 600 !important;
font-size: 14.5px !important;
}

input, textarea, div[data-baseweb="select"], div[data-baseweb="select"] > div {
border-radius: 12px !important;
border: 1px solid #2b2930 !important;
background-color: #0d0d0f !important;
color: #f5f1ea !important;
}

div[data-baseweb="popover"] li {
background-color: #17161a !important;
color: #f5f1ea !important;
}

input:focus, textarea:focus {
border-color: #ff5a1f !important;
box-shadow: 0 0 0 1px #ff5a1f !important;
}

.stNumberInput button {
background-color: #17161a !important;
color: #f5f1ea !important;
}

/* ---------- Buttons (native streamlit) ---------- */
.stButton > button {
background: linear-gradient(135deg, #ff5a1f 0%, #ffb020 100%) !important;
color: #0d0d0f !important;
border: none !important;
padding: 14px 28px !important;
font-size: 16px !important;
font-weight: 700 !important;
border-radius: 50px !important;
width: 100% !important;
box-shadow: 0 8px 22px rgba(255, 90, 31, 0.25) !important;
transition: all 0.3s ease !important;
}

.stButton > button:hover {
transform: translateY(-2px) !important;
box-shadow: 0 10px 26px rgba(255, 90, 31, 0.35) !important;
}

.stAlert {
border-radius: 14px !important;
}

/* ---------- Footer ---------- */
.footer-container {
margin-top: 90px;
padding: 42px 8px 20px 8px;
border-top: 1px solid #221f24;
display: flex;
justify-content: space-between;
flex-wrap: wrap;
gap: 20px;
}

.footer-container .footer-block strong {
font-family: 'Playfair Display', serif;
color: #f5f1ea;
font-size: 17px;
}

.footer-container .footer-block p {
color: #8f8781;
font-size: 13.5px;
line-height: 1.8;
margin: 6px 0 0 0;
}

.footer-container a {
color: #ff5a1f;
text-decoration: none;
}

</style>
""", unsafe_allow_html=True)

# ================= AMBIL DATA LOGO LOKAL =================
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    return ""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(BASE_DIR, "logo.png")

logo_base64 = get_base64_image(LOGO_PATH)

if logo_base64:
    logo_html = f'<img src="{logo_base64}" class="hero-logo" alt="Logo">'
else:
    logo_html = ''
    st.sidebar.warning(
        f"⚠️ Logo tidak ditemukan di:\n`{LOGO_PATH}`\n\n"
        "Pastikan file bernama persis `logo.png` berada di folder yang sama dengan app.py."
    )

WA_LINK = "https://wa.me/6281327599900"
IG_LINK = "https://instagram.com/nasibakarmbakrini"

# ================= TOP BAR =================
st.markdown(f"""
<div class="topbar">
<div class="topbar-brand">Nasi <span>Bakar</span> Pawon Mbak Rini</div>
<div class="topbar-actions">
<a class="topbar-link" href="{IG_LINK}" target="_blank">Instagram</a>
<a class="topbar-cta" href="{WA_LINK}" target="_blank">Pesan Sekarang</a>
</div>
</div>
""", unsafe_allow_html=True)

# ================= HERO SECTION =================
st.markdown(f"""
<div class="hero-container">
<div class="hero-flex">
<div class="hero-text">
<span class="hero-eyebrow">Kuliner Rumahan Otentik</span>
<h1>Nasi Bakar Pawon Mbak Rini</h1>
<p>Menggugah selera dengan cita rasa rumahan otentik. Dibuat dengan rempah pilihan dan aroma daun pisang segar yang khas, sangat pas untuk santap pagi maupun berbagai acara spesial Anda.</p>
<div class="hero-btn-container">
<a class="btn-primary" href="{WA_LINK}" target="_blank">🛒 Pesan Sekarang</a>
<a class="btn-secondary" href="{IG_LINK}" target="_blank"><svg class="ig-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="2" width="20" height="20" rx="6" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg> Lihat Instagram</a>
</div>
</div>
<div class="hero-image">
{logo_html}
</div>
</div>
</div>
""", unsafe_allow_html=True)

# ================= VALUE PROPOSITION =================
st.markdown('<div class="section-title">Kenapa Memilih Kami?</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Komitmen kami untuk menyajikan kualitas rasa terbaik setiap harinya.</div>', unsafe_allow_html=True)

feat1, feat2, feat3 = st.columns(3)

with feat1:
    st.markdown("""
<div class="custom-card">
<div class="card-icon">🔥</div>
<h3>Fresh Dibakar</h3>
<p>Proses pembakaran dilakukan sesaat sebelum dikirim untuk menjaga hidangan tetap hangat dengan aroma daun pisang yang optimal.</p>
</div>
""", unsafe_allow_html=True)

with feat2:
    st.markdown("""
<div class="custom-card">
<div class="card-icon">💰</div>
<h3>Harga Bersahabat</h3>
<p>Porsi yang pas dan mengenyangkan, diracik dengan bahan berkualitas premium namun tetap ramah di kantong.</p>
</div>
""", unsafe_allow_html=True)

with feat3:
    st.markdown("""
<div class="custom-card">
<div class="card-icon">💼</div>
<h3>Menerima Pesanan</h3>
<p>Pilihan andalan dan praktis untuk melengkapi menu acara kantor, rapat, kumpul keluarga, arisan, maupun syukuran.</p>
</div>
""", unsafe_allow_html=True)

# ================= MENU FAVORIT =================
st.markdown('<div class="section-title">Menu Favorit</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Varian menu nasi bakar khas resep pawon tradisional.</div>', unsafe_allow_html=True)

menu1, menu2, menu3 = st.columns(3)

with menu1:
    st.markdown("""
<div class="custom-card">
<div class="menu-thumb">🍗</div>
<h3>Nasi Bakar Ayam</h3>
<p>Suwiran ayam berlimpah dengan paduan bumbu rahasia yang gurih, meresap, dan pedasnya pas.</p>
<div class="custom-price">Rp 10.000</div>
</div>
""", unsafe_allow_html=True)

with menu2:
    st.markdown("""
<div class="custom-card">
<div class="menu-thumb">🐟</div>
<h3>Nasi Bakar Ikan</h3>
<p>Olahan ikan gurih manis dipadukan kemangi segar yang harum melengkapi setiap suapan.</p>
<div class="custom-price">Rp 10.000</div>
</div>
""", unsafe_allow_html=True)

with menu3:
    st.markdown("""
<div class="custom-card">
<div class="menu-thumb">🍖</div>
<h3>Nasi Bakar Ampela</h3>
<p>Potongan ampela bumbu basah bertekstur empuk yang kaya rasa dan menggugah selera.</p>
<div class="custom-price">Rp 10.000</div>
</div>
""", unsafe_allow_html=True)

# ================= JAM OPERASIONAL =================
st.markdown("""
<div class="info-banner">
<h3>Jam Operasional</h3>
<h2>Senin - Sabtu</h2>
<h1>06.00 - 09.00 WIB</h1>
<p class="info-note">* Hari Minggu dan tanggal merah libur</p>
</div>
""", unsafe_allow_html=True)

# ================= ORDER FORM =================
st.markdown('<div class="section-title">Formulir Pemesanan Online</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Lengkapi data di bawah ini untuk meneruskan pesanan otomatis ke WhatsApp.</div>', unsafe_allow_html=True)

with st.form(key="order_form", clear_on_submit=False):
    col_form1, col_form2 = st.columns(2)

    with col_form1:
        nama = st.text_input("Nama Pemesan", placeholder="Contoh: Rini")
        menu = st.selectbox("Pilih Varian Menu", ["Nasi Bakar Ayam", "Nasi Bakar Ikan", "Nasi Bakar Ampela"])
        jumlah = st.number_input("Jumlah Pesanan (Porsi)", min_value=1, value=1)

    with col_form2:
        alamat = st.text_area("Alamat Lengkap Pengiriman", placeholder="Contoh: Jl. Bengawan Solo No.46, RT.04/RW.05, Semanggi, Kec. Ps. Kliwon, Surakarta")
        catatan = st.text_area("Catatan Tambahan (Opsional)", placeholder="Contoh: Pedas sedang saja, minta tolong dikirim jam 07.00 pagi")

    submit_button = st.form_submit_button(label="🚀 Buat & Kirim Pesanan Sekarang")

if submit_button:
    if not nama or not alamat:
        st.error("Silakan lengkapi Nama dan Alamat pengiriman terlebih dahulu.")
    else:
        nomor_wa = "6281327599900"
        pesan_wa = (
            f"Halo Mbak Rini, saya ingin memesan Nasi Bakar:\n\n"
            f"👤 *Nama Pemesan*: {nama}\n"
            f"📦 *Menu*: {menu}\n"
            f"🔢 *Jumlah*: {jumlah} Porsi\n"
            f"📍 *Alamat*: {alamat}\n"
            f"📝 *Catatan*: {catatan if catatan else '-'}\n\n"
            f"Terima kasih!"
        )

        pesan_encoded = urllib.parse.quote(pesan_wa)
        link_wa = f"https://wa.me/{nomor_wa}?text={pesan_encoded}"

        st.success("🎉 Formulir pesanan berhasil dibuat!")

        st.markdown(f"""
<div style="text-align: center; margin-top: 15px;">
<a class="btn-primary" href="{link_wa}" target="_blank" style="background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color: #ffffff !important; padding: 16px 40px; display: inline-block; box-shadow: 0 8px 22px rgba(37, 211, 102, 0.3);">
💬 Teruskan Ke WhatsApp (Klik Di Sini)
</a>
</div>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown(f"""
<div class="footer-container">
<div class="footer-block">
<strong>Nasi Bakar Pawon Mbak Rini</strong>
<p>📍 Jl. Bengawan Solo No.46, RT.04/RW.05, Semanggi, Kec. Ps. Kliwon,<br>Kota Surakarta, Jawa Tengah 57117</p>
<p>Sajian kuliner lokal berkualitas, higienis, dan penuh rasa.</p>
</div>
<div class="footer-block">
<strong>Hubungi Kami</strong>
<p><svg class="ig-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="2" y="2" width="20" height="20" rx="6" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg> <a href="{IG_LINK}" target="_blank">@nasibakarmbakrini</a></p>
<p>💬 <a href="{WA_LINK}" target="_blank">0813-2759-9900</a></p>
</div>
</div>
""", unsafe_allow_html=True)