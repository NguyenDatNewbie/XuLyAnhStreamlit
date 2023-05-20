import XuLyAnh.Chapter09 as chapter9
import streamlit as st 
import os
import cv2

def getImagePathFromBrowser(image_file):
    path_file = os.path.join("file_upload",image_file.name)
    with open(os.path.join("file_upload",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    fullpath = ""+os.getcwd()+"/"+path_file
    imgin = cv2.imread(fullpath,cv2.IMREAD_GRAYSCALE)
    return imgin

def XuLyAnhChapter9(option,file):
    if option == 'Connected component':
        st.title('Connected component')
        st.write('Connected component là một khái niệm trong xử lý ảnh để xác định các vùng có liên thông với nhau trong một ảnh nhị phân hoặc ảnh xám. Còn được ứng dụng rộng rãi như xác định vật thể, phát hiện cạnh, phân tích văn bản')
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            imgout = chapter9.ConnectedComponent(getImagePathFromBrowser(file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    else:
        st.title('Count Rice')
        st.write('Việc đếm số lượng hạt gạo trong ảnh là một ứng dụng phổ biến của xử lý ảnh và có rất nhiều ứng dụng trong thực tế, ví dụ như: Kiểm tra chất lượng sản phẩm, nghiên cứu về năng suất và sản lượng, điều khiển tự động')
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            imgout = chapter9.CountRice(getImagePathFromBrowser(file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)