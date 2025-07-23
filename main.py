import streamlit as st

# 💡 유튜브 영상 상단 삽입
st.video("https://www.youtube.com/watch?v=iHSjxEzH8BE")

# 🔰 로고 및 헤더
st.image("quant_logo.png", width=100)
st.title("🎯 QuantOchestra 실시간 리포트")
st.markdown("✅ **오늘의 데이터 분석을 시작합니다.**")

# 📊 급등 종목 리스트
with st.expander("📊 Top 5 급등 종목"):
    st.write(["국일제지", "두산로보틱스", "NHN KCP", "삼천당제약", "하이스틸"])

# 📌 투자 인사이트 레포트 요약 추가 ✅
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

# 🌐 섹터맵 시각화
with st.expander("🌐 섹터별 강도 시각화"):
    st.image("sector_map.png")

# ✅ 상태 메시지
st.success("데이터 최신 업데이트 완료 (2025-07-23)")




