import streamlit as st

# Ganti dengan direct image URL kamu
background_url = "https://i.ibb.co.com/xqwsXfq8/IMG-0774.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- SESSION STATE UNTUK NAVIGASI ----------
if 'page' not in st.session_state:
    st.session_state.page = 0

# ---------- HALAMAN-HALAMAN ----------
def halaman_1():
    st.markdown(
        """
        <h1 style="
            font-weight: 1000;
            color: #1A1A1A;
            text-shadow: 1px 1px 3px rgba(255,255,255,0.6);
            background-color: rgba(255, 255, 255, 0.6);
            padding: 10px;
            border-radius: 10px;
            display: inline-block;
        ">
            🥦Helloooww welcome at VeggieBites guys!!
        </h1>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("Cari tahu yukk tipe vegetarian kamu yang mana biar kita bisa bantu kasih menu sehat yang sesuai buat kamuu><.")

    pilihan = st.radio(
        "Kamu termasuk tipe vegetarian yang mana nih?",
        [
            "Lacto-ovo (telur & susu masih aku makan sieh)",
            "Lacto (only susu, telur big no no)",
            "Ovo (telur oke sieh, tapi susu ga dulu deh)",
            "Vegan total (no hewani et all)"
        ]
    )
    
    if st.button("Next"):
        st.session_state.page += 1


def halaman_2():
    st.title("Kebutuhan Nutrisi Kamu")
    st.markdown("Sebagai vegetarian, kamu perlu perhatian khusus pada beberapa nutrisi ini loh:")
    st.markdown("""
    - Protein: Tempe, tahu, kacang-kacangan, Telur, Biji Chia, Quinoa, Bayam
    - Zat Besi: Bayam, Brokoli, Kacang Merah, Buncis, Lentil
    - Vitamin B12: Susu Kedelai Fortifikasi, suplemen, Serealia, Nori
    - Kalsium: Tahu, Almond, Sayur Hijau, Susu Kedelai
    - Omega-3: Flaxseed, Spirulina, Chlorella
    """)
    if st.button("Next"):
        st.session_state.page += 1
    if st.button("Back"):
        st.session_state.page -= 1


def halaman_3():
    st.title("Rekomendasi Menu Vegetarian Buat Kamu")
    st.subheader("1. 💚Smoothie Green💚")
    st.markdown("Bahan: Bayam, pisang, susu almond, chia seed")
    st.subheader("2. 🫑Tofu Stir Fry🥕")
    st.markdown("Bahan: Tahu, paprika, wortel, kecap asin")
    st.subheader("3. 🍫Overnight Oat Choco-Berry🍓")
    st.markdown("Bahan: Oat, susu oat, kakao bubuk, stroberi")
    st.markdown("Cara buat: Campur bahan, simpan di kulkas semalam.")
    st.subheader("4. 🥜Salad Kacang🥜")
    st.markdown("Bahan: Kacang merah, jagung, tomat, alpukat")
    st.markdown("Cara buat: Campur semua bahan dengan dressing lemon & olive oil.")
    st.subheader("5. 🥬Veggie Wrap🥬")
    st.markdown("Bahan: Tortilla, selada, wortel, hummus, timun")
    st.markdown("Cara buat: Isi tortilla dengan semua bahan dan gulung.")
    if st.button("Next"):
        st.session_state.page += 1
    if st.button("Back"):
        st.session_state.page -= 1


def halaman_4():
    st.title("Butuh Pengganti Bahan?")
    st.markdown("Masukkan bahan yang ingin diganti, nanti kita bantu kasih alternatifnya!")
    st.markdown("Contoh: susu, telur, daging, keju, dll")

    # Simpan hasil di session_state
    if "hasil_pengganti" not in st.session_state:
        st.session_state.hasil_pengganti = ""
    if "bahan_input" not in st.session_state:
        st.session_state.bahan_input = ""

    # Input text biasa
    st.session_state.bahan_input = st.text_input("Masukkan nama bahan yang mau diganti:", value=st.session_state.bahan_input)

    # Tombol Search
    if st.button("Search"):
        bahan = st.session_state.bahan_input.lower()
        pengganti = {
            "susu": "susu almond / oat milk",
            "telur": "chia egg (chia + air)",
            "daging": "jamur, tempe, atau tofu",
            "keju": "keju vegan berbasis kacang",
            "daging sapi": "tempe, tahu, jamur tiram, jackfruit, seitan",
            "daging ayam": "tempe, tahu, jamur tiram, jackfruit, seitan",
            "daging giling": "kacang hitam, kacang merah, walnut cincang, tahu hancur",
            "susu sapi": "susu almond, susu kedelai, oat milk, coconut milk",
            "keju cheddar": "keju vegan, nutritional yeast",
            "parmesan": "nutritional yeast, kacang mete blend",
            "cream cheese": "tahu sutra + lemon + garam (di-blend)",
            "mentega": "minyak kelapa, margarin vegan, alpukat",
            "mayones": "mayones vegan, tofu + mustard + lemon",
        }
        hasil = pengganti.get(bahan, "Bahan yang kamu cari belum ada di daftar. Coba bahan lain yuk!")
        st.session_state.hasil_pengganti = f"Pengganti untuk {bahan}: {hasil}"

    # Tampilkan hasil kalau ada
    if st.session_state.hasil_pengganti:
        st.success(st.session_state.hasil_pengganti)

    # Navigasi tombol
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back", key="back4"):
            st.session_state.page -= 1
            st.session_state.hasil_pengganti = ""
    with col2:
        if st.button("Next", key="next4"):
            st.session_state.page += 1
            st.session_state.hasil_pengganti = ""

def halaman_5():
    st.title("Terima Kasih Telah Berkunjung!")
    st.markdown("Semoga VeggieBites bermanfaat untuk kamu!")
    if st.button("Back"):
        st.session_state.page -= 1


# ini juga
halaman_fungsi = [halaman_1, halaman_2, halaman_3, halaman_4, halaman_5]

# tambahin nih
halaman_fungsi[st.session_state.page]()
