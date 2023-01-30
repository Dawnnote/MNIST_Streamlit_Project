import cv2
from keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import random
import pyautogui
import os

os.environ['DISPLAY'] = ':0'

@st.cache(allow_output_mutation=True)
def load():
    return load_model('./model.h5')
model = load()

st.image('./images/title.png')

st.write('# 계산기 :computer:')
st.write('숫자 두개를 그려주세요')
CANVAS_SIZE = 340
STROKE_SIZE =16 

# 숫자 확인
def model_predict(canvas1, canvas2) :
        img1 = canvas1.image_data.astype(np.uint8)
        img1 = cv2.resize(img1, dsize=(28, 28))
        preview_img = cv2.resize(img1, dsize=(CANVAS_SIZE, CANVAS_SIZE), interpolation=cv2.INTER_NEAREST)
        x1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        x1 = x1.reshape((-1, 28, 28, 1))
        y1 = model.predict(x1).squeeze()

        
        img2 = canvas2.image_data.astype(np.uint8)
        img2 = cv2.resize(img2, dsize=(28, 28))
        x2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        x2 = x2.reshape((-1, 28, 28, 1))
        y2 = model.predict(x2).squeeze()

        return np.argmax(y1), np.argmax(y2) 

# 계산
def calculation() :
    operator = st.radio('operator', ["+", "-", "%", "*"]) 

    st.write("## 계산 결과는...")
    if operator == "+" : 
        st.write('## %d + %d = %d' % (z1,z2,z1+z2))

    elif operator == "-" : 
        st.write('## %d - %d = %d' % (z1,z2,z1-z2))

    elif operator == "%" : 
        st.write('## %d / %d = %d' % (z1,z2,z1/ z2))

    else : 
        st.write('## %d * %d = %d' % (z1,z2,z1*z2))

# canvas 설정
col1, col2 = st.columns(2)

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
   

# 숫자 에측 
if canvas1.image_data is not None and canvas2.image_data is not None:
    z1, z2 = model_predict(canvas1, canvas2)


# 그린 숫자가 맞는지 확인
st.write("## 입력하신 숫자가 맞나요?? %d, %d" % (z1 ,z2) )
[col1, col2] =st.columns(2) 


if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

def callback():
    st.session_state.button_clicked = True

# 맞을 경우  
with col1 :
    if (st.button("Yes", on_click=callback) or st.session_state.button_clicked): 
        st.write("## 연산자를 골라주세요!")
        calculation()


with col2 : 
    if st.button("NO")  :
        pyautogui.hotkey('f5') 
