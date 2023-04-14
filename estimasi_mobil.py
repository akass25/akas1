import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

model = st.text_input('Input Model Mobil', 0)
year = st.number_input('Input Tahun Mobil', 0)
mileage = st.number_input('Input Km Mobil', 0)
tax = st.number_input('Input Pajak Mobil', 0)
mpg = st.number_input('Input Konsumsi BBM Mobil', 0)
engineSize = st.number_input('Input Engine Size', 0)

predict = ''

if st.button('Prediksi Harga'):
    predict = model.predict(
        [[model, year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Prediksi harga mobil bekas dalam Ponds : ', predict)
    st.write ('Prediksi harga mobil bekas dalam IDR (Juta) :', predict*19000)
