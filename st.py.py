import streamlit as st
import random

st.set_page_config(page_title="1 Hari 1 Kebaikan", page_icon=":star:", layout="wide")

bismillah = [
    {"question": "Memuji Orang di Jalanan", "answer": "仁", "jawaban": "Mencintai"},
    {"question": "Membantu Orang Tua Menyebrang Jalan", "answer": "悌","jawaban": "Menghormati"},
    {"question": "Berdana Kepada Orang yang Membutuhkan", "answer": "仁","jawaban": "Bersyukur"},
]

# Generate a random index from the list
random_index = random.randint(0, len(bismillah) - 1)

# Display the random data
st.title("1 Hari 1 Kebaikan🎆!")
st.write("Lakukan kebaikan di bawah ini!")
st.write(bismillah[random_index])

# Display a button to generate another random data
if st.button("Kebaikan baru lagi!"):
    st.experimental_rerun()

user_answer = st.text_input("⋆⭒˚｡⋆ Apa nilai konfusius yang berhubungan dengan kebaikan tersebut?")

# Check if answer is correct
if user_answer.lower() == random_data['answer']:
    st.write("BENAR, KEREN SKALI!")
else:
    st.write(f"Belum tepat, ayo coba lagi!")