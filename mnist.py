import cv2
from keras.models import load_model
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np

@st.cache(allow_output_mutation=True)
def load():
    return load_model('./cnn-mnist-model.h5')
model = load()

st.write('# MNIST Recognizer')

CANVAS_SIZE = 192

col1, col2 = st.beta_columns(2)

with col1:
    canvas = st_canvas(
        fill_color='#000000',
        stroke_width=20,
        stroke_color='#FFFFFF',
        background_color='#000000',
        width=CANVAS_SIZE,
        height=CANVAS_SIZE,
        drawing_mode='freedraw',
        key='canvas'
    )

if canvas.image_data is not None:d
    img = canvas.image_data.astype(np.uint8)
    img = cv2.resize(img, dsize=(28, 28))
    preview_img = cv2.resize(img, dsize=(CANVAS_SIZE, CANVAS_SIZE), interpolation=cv2.INTER_NEAREST)

    col2.image(preview_img)

    x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    x = x.reshape((-1, 28, 28, 1))
    y = model.predict(x).squeeze()

    st.write('## Result: %d' % np.argmax(y))
    st.bar_chart(y)


    # 아래 단계를 차례로 실행해 주세요
    # 1. python -m pip install --upgrade pip
    # 2. conda create -n tensorflow python=3.7
    # 3. activate tensorflow
    # 4. pip install tensorflow
    # 5. pip install keras
    # 6. pip install opencv-python
    # 7. pip install streamlit_drawable_canvas
    # 8. 모듈이 없다고 오류뜨면 그것도 pip install 하기
