import streamlit as st
import MeCab
import jaconv
import random

st.title("読みにくい文章ジェネレーター")
with st.form(key="generate form"):
    option = st.selectbox("出力方法",("スペース区切り","一続き"))
    kugiri = " " if option == "スペース区切り" else ""
    text = st.text_input("文を入力してね")
    output_button = st.form_submit_button("よくわからんくする")
    
    if output_button:
        m = MeCab.Tagger()
        node = m.parseToNode(text)
        words = []
        while node:
            feature = node.feature.split(",")
            if len(feature) == 6 or feature[0] =="補助記号": #英単語と記号
                words.append(node.surface)
            elif len(feature) > 19: #日本語
                hira = jaconv.kata2hira(feature[20])
                if len(hira) > 2:
                    hira_naka = hira[1:]
                    hira = hira[0] + "".join(random.sample(hira_naka, len(hira_naka)))
                words.append(hira)
            node = node.next
        sentence = kugiri.join(words)

        st.write(sentence)