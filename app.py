import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="스마트 홈 대시보드 - 오승주",
    page_icon="🐶",
    layout= "centered"

)

st.header("스트림릿 배포 테스트중")
st.write("스트림릿 배포해보기 - 오승주")



# 페이지 등록
# st.page("파일경로",title = '메뉴이름, icon = "아이콘")
# 1. 홈화면
home = st.Page("pages/home.py", title = "홈")
# 2. 센서화면
sensors = st.Page("pages/sensors.py", title = "센서현황")
# 3. 전력화면
power = st.Page("pages/power.py", title = "전력현황")
# 4. 분석페이지

test = st.Page("pages/test11.py",title = "분석테스트")

# 네비게이션 구성
pg = st.navigation({
    "메인" : [home],
    "분석" : [sensors, power,test]

})

st.sidebar.write("같은 사이드 바 형태입니다.")

# 선택된 페이지 실행
pg.run()


# ---------#
# 페이지 추가하기
# 온도 분석 페이지 만들어보기 -> 간단하게 제목과 안의 텍스트만
# ---------# 