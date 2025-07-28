from dotenv import load_dotenv
import streamlit as st
from ai import get_personality_analysis

load_dotenv()

st.title("🔮 AI 관상 보기 프로그램")
st.write("---")

st.write("안녕하세요, AI 관상가입니다.")
st.write("당신의 얼굴 특징을 알려주시면 성격과 미래를 알려드릴게요.")

face_desc = st.text_area("얼굴 특징을 입력해주세요: ")
face_desc = face_desc.strip()

if st.button("관상 보기", type="primary"):
    if face_desc: 
        with st.spinner("관상을 분석 중입니다..."):
            result = get_personality_analysis(face_desc)
            st.write("----")
            st.write("관상 분석이 끝났습니다.")
            st.info(result)
        # 
    else:
        st.error("얼굴 특징을 입력하고, '관상 보기' 버튼을 클릭해주세요.")