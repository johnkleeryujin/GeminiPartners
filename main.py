print("Hello! Cursor에서 Python 잘 실행됐습니다.")

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

# 🌐 섹터맵 시각화
with st.expander("🌐 섹터별 강도 시각화"):
    st.image("sector_map.png")

# ✅ 상태 메시지
st.success("데이터 최신 업데이트 완료 (2025-07-23)")



