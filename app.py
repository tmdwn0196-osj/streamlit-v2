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

st.sidebar.header("필터 설정")

user_temp = st.sidebar.slider(
    "123",
    min_value=10.0,
    max_value=40.0,
    value=(20.0, 30.0),
    step=0.5
)


