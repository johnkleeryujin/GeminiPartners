import os
import streamlit as st
import pandas as pd

# 💡 배경색 변경
st.markdown(""" 
    <style>
        body {
            background-color: black;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 💡 유튜브 영상 상단 삽입
st.video("https://www.youtube.com/watch?v=iHSjxEzH8BE")

# 🔰 로고 교체 및 헤더
st.image("new_logo.png", width=100)  # 새로운 로고 이미지로 교체
st.title("🎯 QuantOchestra 올인원 통합 솔루션")
st.markdown("✅ **오늘의 데이터 분석을 시작합니다.**")

# 📊 급등 종목 리스트
with st.expander("📊 Top 5 급등 종목"):
    st.write(["국일제지", "두산로보틱스", "NHN KCP", "삼천당제약", "하이스틸"])

# 📌 투자 유망 섹터 투표 추가
with st.expander("📊 투자 유망 섹터 투표"):
    sector_choice = st.radio(
        "어떤 섹터가 투자 유망하다고 생각하시나요?",
        ("AI/로봇", "전력인프라", "SMR원전", "바이오")
    )
    st.write(f"투표하신 섹터: {sector_choice}")
    
    # 투표 결과를 위한 데이터 예시
    data = {'섹터': ["AI/로봇", "전력인프라", "SMR원전", "바이오"],
            '투표수': [60, 100, 40, 80]}
    df = pd.DataFrame(data)

    # 바차트로 표시
    st.bar_chart(df.set_index('섹터'))

# 📌 투자 인사이트 레포트 요약
with st.expander("📌 투자 인사이트 레포트 요약"):
    st.markdown("""
    - **🔥 집중 종목**: 이더리움 (8~9월 정리 예정), 도지코인, 리플
    - **🚫 국내 주식 보류**: 하이닉스 등 매수 자제, 코인·미국 주식 중심
    - **📉 금리 시나리오**:
        - 0.25%p 인하 → 안정
        - 0.5%p 인하 → 자산시장 충격
    - **📈 달러 전망**:
        - 금리 인하 시 단기 강달러 가능성
        - 관세 재발 시 강달러 유지 전략
    - **🧨 시장 리스크**: 트럼프 관세 재개, 파월 경질, 15일 이내 급락 가능성
    - **📆 출구 전략**: 2025년 8~9월 고점 예상 → 자산 전환 준비
    - **💡 철학**: "천천히, 꾸준히" / 단타보단 장기 포트폴리오 전략
    """)

# 📂 PDF 다운로드 링크 (Upload 방식)
st.markdown("📂 **투자 인사이트 레포트 다운로드**")

# 파일 업로드 기능 추가
uploaded_file = st.file_uploader("투자 인사이트 레포트 파일을 업로드 해주세요.", type=["pdf"])

if uploaded_file is not None:
    st.download_button(
        label="투자 인사이트 레포트 다운로드",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )
else:
    st.write("파일을 업로드해 주세요.")

# 📌 저작권 및 SaaS 정보 추가
st.markdown("""
    <br>
    <div style="text-align: center;">
        <p>저작권자: 류진(Ryu Jin) Copyright ©GeminiPartners All Rights Reserved.</p>
        <p>SaaS: 제미나이파트너스 | 📧 geminivintage40@gmail.com</p>
    </div>
""", unsafe_allow_html=True)

# 디버깅 정보: 현재 작업 디렉토리 출력
st.write(f"Current working directory: {os.getcwd()}")
