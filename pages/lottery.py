import cv2
from keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as ts
import random  
import pyautogui
import os

os.environ.get('DISPLAY') is None


disable_btn=False

@st.cache(allow_output_mutation=True)
def load():
    return load_model('./model.h5')
model = load()
st.image('./images/title.png')

st.title('행운의 숫자 뽑기')

col1, col2,col3,col4 = st.columns(4)
CANVAS_SIZE = 192
yes_btn=False
no_btn=False




with col1:
    st.write("숫자를 그려주세요")
    canvas1 = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas1'
    )
with col2:
    st.write("숫자를 그려주세요")
    canvas2 = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas2'
    )    
    


# 브라우저가 가진 session을 이용하여 화면이 새로 렌더링 되더라도 계속 내 데이터를 가지고 갑니다.
if 'key' not in st.session_state:
    st.session_state['key'] = set()
if 'sort' not in st.session_state:
    st.session_state['sort'] = []
if 'rn' not in st.session_state:
    st.session_state['rn'] = random.sample(range(1,100),4)   

def lottery_check (check,win):
    same=0
    for i in check :
        if i in win:
             same+=1
    return same
    
    
if len(st.session_state.key)>3 :
    disable_btn=True
    with col1:
        st.write('뽑은 숫자들')
        st.session_state.sort=list(st.session_state.key)
        sorted_number=sorted(st.session_state.sort)
        st.write(sorted_number)
    with col2:    
        st.write('당첨번호 확인하기')
        check_number=st.button('과연 몇개?')
        st.write('나온 숫자입니다')
        lottery_num=sorted(st.session_state.rn)
        st.write(lottery_num)
        txt=lottery_check(sorted_number,lottery_num)
        st.write('%d 개 맞았습니다 ' %(txt))

    

def get_2number (c1,c2):
    img = canvas1.image_data.astype(np.uint8)
    img = cv2.resize(img, dsize=(28, 28))
    x1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x1 = x1.reshape((-1, 28, 28, 1))
    y1 = model.predict(x1).squeeze()
    get_number1=np.argmax(y1)
    
    img = canvas2.image_data.astype(np.uint8)
    img = cv2.resize(img, dsize=(28, 28))
    x2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x2 = x2.reshape((-1, 28, 28, 1))
    y2 = model.predict(x2).squeeze()
    get_number2=np.argmax(y2)
    return int(get_number1)*10+int(get_number2)

if (canvas1.image_data is not None) & (canvas2.image_data is not None):
    with col3:

        get_number=get_2number(canvas1,canvas2)
        st.subheader('쓰신 숫자가: %d 맞나요?' % get_number)

        with st.container() :
            yes_btn= st.button('yes',disabled=(disable_btn))
            no_btn= st.button('no')

        # 바뀐 부분
        if yes_btn:
            st.session_state.key.add(int(get_number))
            

        if no_btn:
            with col2:
                st.write("숫자를 다시 입력해주세요")
        st.text('중복숫자는 불가능')
# 바뀐부분
with col4:
    st.text(" 총 4개의\n 숫자를 입력\n 하세요")
    if st.session_state:
        str_set=''
        for i in st.session_state.key :
           str_set+=str(i)+' '
        st.subheader(str_set)
    with col4:
        refresh_btn=st.button("regame?")
        if refresh_btn==True:
            pyautogui.hotkey('f5')        
        
        
