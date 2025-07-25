import os
import streamlit as st
import pandas as pd
import plotly.express as px

# ✅ 다크모드 적용
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

# 🔊 팟캐스트
st.subheader("🎧 Figma's Financials and IPO Prospectus Deep Dive")
st.audio("Figma's Financials and IPO Prospectus Deep Dive.wav")

# 🎬 유튜브
st.video("https://youtu.be/7y0301fjGQw?si=wOAotd844ozRz6wE")

# 헤더: 로고 + 타이틀
col1, col2 = st.columns([1, 6])
with col1:
    st.image("new_logo.png", width=80)
with col2:
    st.markdown("<div class='center-header'><h2>🎯 QuantOchestra</h2></div>", unsafe_allow_html=True)
    st.markdown("### CCRT 올인원 통합 솔루션")

# 🔥 급등 종목 리스트
with st.expander("📊 Top 5 ROI TrendTracking"):
    st.write(["두산에너빌리티", "한전기술", "NHN KCP", "솔트룩스", "두산로보틱스"])

# 📈 섹터 투표 (Plotly)
with st.expander("📊 투자 섹터 인기투표"):
    vote_df = pd.DataFrame({
        '섹터': ["AI/로봇", "전력인프라", "SMR 원자력", "AI 바이오"],
        '투표수': [60, 100, 40, 80]
    })
    fig = px.bar(vote_df, x='섹터', y='투표수', color='섹터', title="인기 섹터 투표 현황")
    st.plotly_chart(fig, use_container_width=True)

# 📌 투자 인사이트 요약
with st.expander("📌 투자 인사이트 레포트 요약 (2025 하이테크 산업 트렌드 기반)"):
    st.markdown("""
**1. 🧠 생성형 AI와 멀티모달 기술의 급속한 성장**  
- 텍스트·이미지·음성 융합된 AI가 산업 전반 확산  
- 실시간 번역/영상/게임 등에 AI 도입 본격화  
- 6G/엣지 컴퓨팅이 인프라 핵심

**2. 💰 투자 및 M&A 흐름**  
- 생성형 AI 투자 $33.9B, 고성장 스타트업 중심 M&A  
- 성장성 기반의 투자 쏠림 심화

**3. ⚠️ 주요 리스크**  
- AI 윤리·규제 불확실성  
- 기술 집중화로 인한 독점화 리스크 증가

**4. 🚀 반도체 + AI 재편**  
- 글로벌 반도체 시장 15% 성장  
- NVIDIA, HBM, CHIPS Act 중심 공급망 재편

**5. 🤖 로보틱스·자율기계**  
- 미국 로봇 시장 연 45.7% 성장 예상  
- Optimus, Boston Dynamics, Waymo 등 상용화 진입

**6. 🌍 미중 기술 패권 경쟁 격화**  
- 미국 수출 통제 vs 중국 독자 칩 개발

**결론**:  
- 2025년 8~9월 고점 예상  
- 전략: 정찰병 진입 → 락업 해제 이후 분할매수
    """)

# 📌 Figma IPO 요약
with st.expander("📌 Figma IPO 매매 대응전략"):
    st.markdown("""
- 상장일: 2025년 7월 30일 (NYSE: FIG)  
- 공모가: $25~$28 / 시총 $14.6B~$16.4B  
- 연평균 성장률 46%, SaaS + AI + Web3 토큰  
- 매매 전략:
    - 🕵 정찰병 진입  
    - 🐢 분할 DCA  
    - 📉 락업 해제 이후 본격 매수
    """)

# 📂 사용자 업로드 PDF 다운로드
st.markdown("📂 **사용자 PDF 리포트 업로드 및 다운로드**")
uploaded = st.file_uploader("PDF 파일을 업로드하세요", type="pdf")
if uploaded:
    st.download_button("📄 업로드한 PDF 다운로드", uploaded, file_name=uploaded.name)

# 📥 고정 PDF 다운로드
with st.expander("📂 Figma IPO 리서치 보고서 다운로드"):
    with open("Figma (FIG) IPO 투자 리서치 보고서.pdf", "rb") as f:
        st.download_button("📄 공식 리서치 다운로드", f.read(), file_name="Figma_IPO_Report.pdf")

# 🧠 마인드맵
st.markdown("---")
st.subheader("🧠 QuantOchestra Sector Mindmap")
st.image("sector_mindmap.png", caption="Sector Map", use_column_width=True)

st.markdown("---")
st.subheader("🧠 Figma IPO 분석 마인드맵 (NotebookLM 기반)")
st.image("Figma_NotebookLM Mind Map.png", caption="Figma Report Map", use_column_width=True)

# ⓒ 저작권
st.markdown("""
<br><div style="text-align: center;">
    <p>저작권자: 류진(Ryu Jin) © GeminiPartners. All Rights Reserved.</p>
    <p>운영사: 제미나이파트너스 | 📧 geminivintage40@gmail.com</p>
</div>
""", unsafe_allow_html=True)

