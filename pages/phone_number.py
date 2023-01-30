import cv2
from keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import pandas as pd
from io import BytesIO
import pyautogui
import os

os.environ['DISPLAY'] = ':0'

@st.cache(allow_output_mutation=True)
def load():
    return load_model('./model.h5')
model = load()

st.image('./images/title.png')

name_input = st.text_input('이름을 입력하세요')

st.subheader(" '010'을 제외한 휴대폰 번호 8자리를 입력해주세요.")

CANVAS_SIZE = 160
STROKE_SIZE = 12
st.text('중간 번호 4자리')

col1, col2, col3, col4 = st.columns(4)

with col1:
    canvas1 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas1'
    )

with col2:
    canvas2 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas2'
    )

with col3:
    canvas3 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas3'
    )

with col4:
    canvas4 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas4'
    )

st.text('마지막 번호 4자리')
col5, col6, col7, col8 = st.columns(4)
with col5:
    canvas5 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas5'
    )

with col6:
    canvas6 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas6'
    )

with col7:
    canvas7 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas7'
    )

with col8:
    canvas8 = st_canvas(
        fill_color='#000000',
        stroke_width=STROKE_SIZE,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas8'
    )


if canvas1.image_data is not None:
    img1 = canvas1.image_data.astype(np.uint8)
    img1 = cv2.resize(img1, dsize=(28, 28))

    img2 = canvas2.image_data.astype(np.uint8)
    img2 = cv2.resize(img2, dsize=(28, 28))

    img3 = canvas3.image_data.astype(np.uint8)
    img3 = cv2.resize(img3, dsize=(28, 28))

    img4 = canvas4.image_data.astype(np.uint8)
    img4 = cv2.resize(img4, dsize=(28, 28))

    img5 = canvas5.image_data.astype(np.uint8)
    img5 = cv2.resize(img5, dsize=(28, 28))

    img6 = canvas6.image_data.astype(np.uint8)
    img6 = cv2.resize(img6, dsize=(28, 28))

    img7 = canvas7.image_data.astype(np.uint8)
    img7 = cv2.resize(img7, dsize=(28, 28))

    img8 = canvas8.image_data.astype(np.uint8)
    img8 = cv2.resize(img8, dsize=(28, 28))

    x1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    x1 = x1.reshape((-1, 28, 28, 1))
    y1 = model.predict(x1).squeeze()

    x2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    x2 = x2.reshape((-1, 28, 28, 1))
    y2 = model.predict(x2).squeeze()

    x3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    x3 = x3.reshape((-1, 28, 28, 1))
    y3 = model.predict(x3).squeeze()

    x4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    x4 = x4.reshape((-1, 28, 28, 1))
    y4 = model.predict(x4).squeeze()

    x5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)
    x5 = x5.reshape((-1, 28, 28, 1))
    y5 = model.predict(x5).squeeze()

    x6 = cv2.cvtColor(img6, cv2.COLOR_BGR2GRAY)
    x6 = x6.reshape((-1, 28, 28, 1))
    y6 = model.predict(x6).squeeze()

    x7 = cv2.cvtColor(img7, cv2.COLOR_BGR2GRAY)
    x7 = x7.reshape((-1, 28, 28, 1))
    y7 = model.predict(x7).squeeze()

    x8 = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)
    x8 = x8.reshape((-1, 28, 28, 1))
    y8 = model.predict(x8).squeeze()

    st.write('#### Number: 010-%d%d%d%d-%d%d%d%d' %(np.argmax(y1),np.argmax(y2),np.argmax(y3),np.argmax(y4),
                            np.argmax(y5),np.argmax(y6),np.argmax(y7),np.argmax(y8)),' 이 번호가 맞습니까?')
    
if 'number' not in st.session_state:
    st.session_state.number = '010-'

if 'Phone_Number' not in st.session_state:
    st.session_state.Phone_Number = []

if 'Name' not in st.session_state:
    st.session_state.Name = []

def phone_number_covert():
    num = str(np.argmax(y1))+str(np.argmax(y2))+str(np.argmax(y3))+str(np.argmax(y4))+'-'+str(np.argmax(y5))+str(np.argmax(y6))+str(np.argmax(y7))+str(np.argmax(y8))
    st.session_state.number += num
    return st.session_state.number
    
col_1, col_2 = st.columns(2)
with col_1:
    if st.button('Yes'):
        st.session_state.number = phone_number_covert()

        st.session_state.Phone_Number += [st.session_state.number]
        st.session_state.Name += [name_input]

        df = pd.DataFrame(
            {
                "Name" : st.session_state.Name,
                "Phone_Number": st.session_state.Phone_Number
            }
        )
        st.session_state.number = '010-'
        st.dataframe(df)

        st.button('추가 입력')

        csv = df.to_csv().encode('ANSI')
        st.download_button(
            label="CSV 파일 다운로드",
            data=csv,
            file_name='휴대폰 번호 정보.csv'
        )

        excel_data = BytesIO()  
        df.to_excel(excel_data)
        st.download_button(
            label="엑셀 파일 다운로드",
            data=excel_data,
            file_name='휴대폰 번호 정보.xlsx'
        )

with col_2:
    if st.button('No'):
        st.error('번호를 다시 입력하세요', icon="🚨")
