import streamlit as st 
from streamlit_option_menu import option_menu
import base64
import shutil
import os
import XuLyAnh.Chapter03Web as webChapter3
import XuLyAnh.Chapter04Web as webChapter4
import XuLyAnh.Chapter05Web as webChapter5
import XuLyAnh.Chapter09Web as webChapter9
import PhatHienKhuonMat.ModelFaceBook.face_detect as fbFace
import NhanDangKhuonMat.predict as predict
import NhanDangKhuonMat.get_face as getFace
import NhanDangKhuonMat.Training as tranningFace
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("./image/background.jpg")
img2 = get_img_as_base64("./image/background2.jpeg")
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");

height: 100%;

background-position: center;
background-repeat: no-repeat;
background-size: cover;
}}
[class = "css-18ni7ap e8zbici2"]{{
    background: transparent;
}}
[class = "block-container css-1y4p8pa egzxvld4"]{{
    padding: 10px 0 0 0;
    max-width: 60rem;
}}
[class = "css-1544g2n e1fqkh3o4"]{{
    padding: 3rem 1rem 1.5rem
}}
h1 [class = "css-zt5igj e16nr0p33"]{{
    color: white;
    text-align: center;
}}
h3 [class = "css-zt5igj e16nr0p33"]{{
    color: white;
    font-weight: bold;
}}
[class = "css-5rimss e16nr0p34"] p{{
    background-color: #f0f2f6;
    font-family: ui-monospace;
    padding: 7px;
}}
[class = "css-16idsys e16nr0p34"] p{{
    font-size: 16px;
    font-family: ui-monospace;
}}

[class= "css-81oif8 effi0qh3"]{{
    color: white;
}}
[class = "row-widget stRadio"]{{
    background: transparent;
    
}}
[class ="css-1629p8f e16nr0p31"] h2{{
    font-size: 24px;
    font-weight: bold;
    color: #F0B071;
    font-style: oblique;
    font-family: 'bootstrap-icons';
}}
[class="row-widget stRadio"]
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}


[class = "css-1kyxreq etr89bj2"]{{
    margin-right:10%;
}}

[class = "css-1kyxreq etr89bj1"]{{
    width:80%;
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}


[data-testid="stSidebar"]{{
    background-image: url("data:image/png;base64,{img2}");

height: 100%;

background-position: center;
background-repeat: no-repeat;
background-size: cover;
}}


</style>
"""
# Chương trình
st.markdown(page_bg_img, unsafe_allow_html=True)

selected = option_menu(
    menu_title= None,
    options = ["Xử lý ảnh","Nhận dạng khuôn mặt","Phát hiện khuôn mặt"],
    icons=['card-image','person-bounding-box','app-indicator'],
    orientation= "horizontal"
)
if selected == "Phát hiện khuôn mặt":
    fbFace.run()
if selected == "Nhận dạng khuôn mặt":
    optionFace = st.selectbox('Chọn Kiểu',('Nhận dạng','Thêm khuôn mặt nhận dạng'))
    if optionFace == 'Nhận dạng':
        tranningFace.run()
        predict.run()
    else: getFace.run()
if selected == "Xử lý ảnh":
    st.sidebar.header("Nguyễn Hữu Đạt - 20110630")
    file_upload = '/file_upload'
    shutil.rmtree(file_upload)
    os.mkdir(file_upload)
    image_file = st.sidebar.file_uploader("Choose a image file",type=['png','jpg','tif','jpeg'])
    
    option = st.sidebar.selectbox('Chọn chương xử lý ảnh',('Chương 3','Chương 4', 'Chương 5','Chương 9'))
    if(option=='Chương 3'):
        optionRadio = st.sidebar.radio('Thuật toán xử lý',('Negative','Logarit','Lũy thừa','Biến đổi tuyến tính','Histogram','Lọc box','Lọc Gauss','Phân ngưỡng','Lọc median','Sharpen', 'Gradient'))
        webChapter3.XuLyAnhChuong3(optionRadio,image_file)
    if(option=='Chương 4'):
        optionRadio = st.sidebar.radio('Thuật toán xử lý',('Spectrum','Highpass filter','Notch Reject','Xóa nhiễu moire'))
        webChapter4.XuLyAnhChapter4(optionRadio,image_file)
    if(option=='Chương 5'):
        optionRadio = st.sidebar.radio('Thuật toán xử lý',('Tạo nhiễu chuyển động','Gỡ nhiễu'))
        webChapter5.XuLyAnhChapter5(optionRadio,image_file)
    if(option=='Chương 9'):
       optionRadio = st.sidebar.radio('Thuật toán xử lý',('Connected component','Count rice'))
       webChapter9.XuLyAnhChapter9(optionRadio,image_file)


       
