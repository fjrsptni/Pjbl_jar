import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "✅"
)

with st.sidebar:
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image("14173.png")
    st.title("Bangun Datar")
    pilihan = st.selectbox("Pilihan Bangun Datar", ["Persegi", "Persegi Panjang" , "Lingkaran" ])
    st.caption ("Dibuat dengan :fire: oleh **Fajar Saptoni**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("menghitung `Luas` dan `keliling` persegi")
        sisi = st.number_input("Masukan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            #st.success(f"Luas persegi adalah {luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("Luas", value=luas, border=True)
            with col2:
                st.metric("Keliling", value=keliling, border=True)
            st.balloons()

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukan Panjang")
        lebar = st.number_input("Masukan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            #st.success(f"Luas persegi panjang adalah{luas:.2f} dan kelilingnya adalah {keliling:.2f}")
            col1, col2 = st.columns([2,2])
            with col1:
                st.metric("luas", value=luas, border=True)
            with col2:
                st.metric("keliling", value=keliling, border=True)
            st.snow()

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `Luas` dan `Keliling` Lingkaran")
        jarijari = st.number_input ("Masukan Jari-Jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2*3.14 * jarijari
            st.success(f"Luas Lingkaran adalah {luas:.2f} dan kelilingya adalah {keliling:.2f}")
            st.snow()
    case _ :
        st.error ("terjadi kesalahan")