import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ 다크모드 스타일 적용
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: black !important;
            color: white !important;
        }
        .stButton > button {
            color: black !important;
        }
        .center-header {
            display: flex;
            align-items: center;
            gap: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 🔊 팟캐스트 오디오 삽입
st.audio("/mnt/data/Figma's Financials and IPO Prospectus Deep Dive.wav")

# 🎬 유튜브 영상 삽입
st.video("https://youtu.be/7y0301fjGQw?si=wOAotd844ozRz6wE")

# 🔰 헤더 영역: 로고 + 제목 정렬
col1, col2 = st.columns([1, 6])
with col1:
    st.image("new_logo.png", width=80)
with col2:
    st.markdown("<div class='center-header'><h2>🎯 QuantOchestra</h2></div>", unsafe_allow_html=True)
    st.markdown("### CCRT 올인원 통합 솔루션")

# 📊 급등 종목
with st.expander("📊 Top 5 급등 종목"):
    st.write(["국일제지", "두산로보틱스", "NHN KCP", "삼천당제약", "하이스틸"])

# 📈 유망 섹터 투표
with st.expander("📊 투자 유망 섹터 투표"):
    sector_choice = st.radio("어떤 섹터가 투자 유망하다고 생각하시나요?",
                             ("AI/로봇", "전력인프라", "SMR원전", "바이오"))
    st.write(f"투표하신 섹터: {sector_choice}")

    df = pd.DataFrame({
        '섹터': ["AI/로봇", "전력인프라", "SMR원전", "바이오"],
        '투표수': [60, 100, 40, 80]
    })

    fig, ax = plt.subplots()
    ax.bar(df['섹터'], df['투표수'], color=['#ff6347', '#4682b4', '#32cd32', '#ff8c00'])
    ax.set_title("투자 유망 섹터 투표 결과")
    st.pyplot(fig)

# 📌 투자 인사이트 요약
with st.expander("📌 투자 인사이트 레포트 요약"):
    st.markdown("""
    - **🔥 집중 종목**: 이더리움, 도지코인, 리플  
    - **🚫 국내 주식 보류**: 하이닉스 등 매수 자제  
    - **📉 금리 시나리오**:
        - 0.25%p 인하 → 안정  
        - 0.5%p 인하 → 자산시장 충격  
    - **📈 달러 전망**:
        - 강달러 유지 가능성  
    - **🧨 리스크**: 트럼프 관세 재개, 파월 경질  
    - **📆 출구 전략**: 2025년 8~9월 고점 예상
    """)

# 📌 Figma IPO 요약
with st.expander("📌 Figma IPO 전략 요약"):
    st.markdown("""
    - **상장일**: 2025년 7월 30일 (NYSE / FIG)  
    - **공모가**: $25 ~ $28 / 시총: $14.6B ~ $16.4B  
    - **매출**: $749M (2024년 기준)  
    - **특징**: AI + SaaS + Web3 토큰 전략  
    - **전략 제안**:
        - 🕵 정찰병 진입 → 소량 모니터링  
        - 🐢 DCA 매수  
        - 📉 락업 해제 이후 진입
    """)

# 📂 업로드 기반 PDF 다운로드
st.markdown("📂 **사용자 PDF 리포트 업로드 및 다운로드**")
uploaded_file = st.file_uploader("PDF 파일을 업로드하세요.", type=["pdf"])
if uploaded_file:
    st.download_button(
        label="📄 업로드한 PDF 다운로드",
        data=uploaded_file,
        file_name=uploaded_file.name,
        mime="application/pdf"
    )
else:
    st.write("🔽 위에 파일을 업로드해주세요.")

# 📥 고정된 PDF 다운로드 (Figma IPO 보고서)
with st.expander("📂 Figma IPO 리서치 보고서 다운로드"):
    with open("/mnt/data/Figma (FIG) IPO 투자 리서치 보고서.pdf", "rb") as file:
        pdf_data = file.read()

    st.download_button(
        label="📄 공식 리서치 보고서 다운로드",
        data=pdf_data,
        file_name="Figma_IPO_리서치_보고서.pdf",
        mime="application/pdf"
    )

# 🧠 섹터 마인드맵 이미지 (기존)
st.markdown("---")
st.subheader("🧠 QuantOchestra Sector Mindmap")
st.image("sector_mindmap.png", caption="QuantOchestra Sector Map", use_column_width=True)

# 🧠 Figma 투자 리포트 마인드맵 이미지 (신규)
st.markdown("---")
st.subheader("🧠 Figma IPO 분석 마인드맵 (NotebookLM)")
st.image("Figma_NotebookLM Mind Map.png", caption="Figma IPO Report Mindmap", use_column_width=True)

# 📌 저작권
st.markdown("""
<br><div style="text-align: center;">
    <p>저작권자: 류진(Ryu Jin) © GeminiPartners. All Rights Reserved.</p>
    <p>SaaS 운영자: 제미나이파트너스 | 📧 geminivintage40@gmail.com</p>
</div>
""", unsafe_allow_html=True)

# 디버깅용
st.write(f"📁 Current working directory: {os.getcwd()}")
