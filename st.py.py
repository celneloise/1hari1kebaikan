import random
import streamlit as st

st.set_page_config(page_title="1 Hari 1 Kebaikan", page_icon=":star:", layout="wide")

dataset = [
    {"question": "Memuji Orang di Jalanan", "answer": "仁", "jawaban": "Mencintai"},
    {"question": "Membantu teman", "answer": "仁","jawaban": "Menghormati"},
    {"question": "Berdana Kepada Orang yang Membutuhkan", "answer": "仁","jawaban": "Bersyukur"},
]

# Display the heading and opening message
st.title("1 Hari 1 Kebaikan🎆!")
st.write("Lakukan kebaikan di bawah ini!")

# Display a random data from the dataset
random_data = random.choice(dataset)
st.write(f"-->{random_data['question']}")

# Ask user to input answer
user_answer = st.text_input("⋆⭒˚｡⋆ Apa nilai konfusius yang berhubungan dengan kebaikan tersebut?")

# Check if answer is correct
if user_answer.lower() == random_data['answer']:
    st.write("BENAR, KEREN SKALI!")
else:
    st.write(f"Belum tepat, ayo coba lagi!")

bismillah = [
    "父母呼 应勿缓 父母命 行勿懒 (fù mǔ hū, yìng wù huǎn, fù mǔ mìng, xíng wù lǎn)\nBila orang tua memanggil, cepat menyahut jangan lamban. Bila orang tua memberi tugas, cepat mengerjakan jangan malas.",
    "父母教 须敬听 父母责 须顺承 (fù mǔ jiào, xū jìng tīng, fù mǔ zé, xū shùn chéng)\nBila orang tua memberi nasihat, simaklah dengan saksama dan syukur. Bila orang tua menegur, turutilah dan terima dengan ikhlas.",
    "冬则温 夏则凊 晨则省 昏则定 (dōng zé wēn, xià zé jìng, chén zé xǐng, hūn zé ding)\nBeri orang tua kehangatan di musim dingin, berilah kesejukan di musim panas. Beri salam di pagi hari, beri ketenangan di malam hari (agar orang tua dapat tidur tenang).",
    # Add more data as needed
]

# Generate a random index from the list
random_index = random.randint(0, len(bismillah) - 1)

# Display the random data
st.write("˙⋆｡‧˚ʚ ",bismillah[random_index],"˚‧｡⋆")
         
# Display a button to generate another random data
if st.button("Refresh"):
    st.experimental_rerun()
