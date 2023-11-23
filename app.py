import streamlit as st
import jaconv
import random
from janome.tokenizer import Tokenizer

st.title("読みにくい文章ジェネレーター")
with st.form(key="generate form"):
    option = st.selectbox("出力方法",("スペース区切り","一続き"))
    kugiri = " " if option == "スペース区切り" else ""
    text = st.text_area("文を入力してね")
    output_button = st.form_submit_button("よくわからんくする")
    
    if output_button:
        t = Tokenizer()
        words = []
        for token in t.tokenize(text):
            if token.part_of_speech[0] == "記号" or token.reading == "*":
                words.append(token.surface)
            else:
                hira = jaconv.kata2hira(token.reading)
                hira_shuffle = hira[0] + "".join(random.sample(hira[1:], len(hira[1:])))
                words.append(hira_shuffle)
        sentence = kugiri.join(words)

        st.write(sentence)