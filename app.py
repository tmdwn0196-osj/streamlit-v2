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

#git add . <- ignore 제외 모든 파일

@st.cache_data
def load_data():
    df = pd.read_csv("../data/smart_home_sensors.csv")
    return df

sensors = load_data()

st.write("## **🏠스마트 홈 대시보드(이쁘게 꾸밈)🏠**")
st.divider()
st.write("### 선택하기")


user_temp = st.slider(
    "온도 설정",
    min_value= 10.0,
    max_value= 40.0,
    value= (20.0,30.0),
    step = 0.5
)

min, max = user_temp

multi_selected_room = st.multiselect(
    "방 설정",
    options=sensors['room'].unique(),default=[])

result = sensors[sensors['room'].isin(multi_selected_room)&
    (sensors['temperature'].between(min,max))]
st.write("선택된 방:", multi_selected_room)
st.write(f"설정한 방, 온도 {multi_selected_room} , {min:.1f}에서 {max:.1f} ")
st.dataframe(result)

st.write("---")

if st.toggle("데이터 요약보기"):
    st.dataframe(sensors.describe())