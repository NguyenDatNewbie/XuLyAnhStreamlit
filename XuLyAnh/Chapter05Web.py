import streamlit as st 
import os
import cv2
import XuLyAnh.Chapter05 as chapter05
def getImagePathFromBrowser(image_file):
    path_file = os.path.join("file_upload",image_file.name)
    with open(os.path.join("file_upload",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    fullpath = ""+os.getcwd()+"/"+path_file
    imgin = cv2.imread(fullpath,cv2.IMREAD_GRAYSCALE)
    return imgin

def XuLyAnhChapter5(option,file):
    if option == 'Tạo nhiễu chuyển động':
        st.title('Tạo nhiễu chuyển động')
        st.write('Trong xử lý ảnh, tạo nhiễu chuyển động được sử dụng như một kỹ thuật để mô phỏng các tình huống di chuyển nhanh trong thực tế và để kiểm tra hiệu quả của các thuật toán xử lý ảnh.')
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            imgout = chapter05.CreateMotionNoise(getImagePathFromBrowser(file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option == 'Gỡ nhiễu':
        st.title('Gỡ nhiễu')
        st.write('Gỡ nhiễu là một kỹ thuật quan trọng trong xử lý ảnh để cải thiện chất lượng ảnh và tăng độ chính xác của các phân tích ảnh, giảm thiểu độ nhiễu trong quá trình xử lý ảnh tiếp theo và cải thiện độ tin cậy của các ứng dụng xử lý ảnh.')
        donhieu = st.select_slider(
            'Chọn độ nhiễu cần gỡ',
            options=['Ít','Trung bình','Nhiều'])
        
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            temp = cv2.medianBlur(getImagePathFromBrowser(file),1)
            if(donhieu=='Trung bình'):
                temp = cv2.medianBlur(getImagePathFromBrowser(file),5)
            if(donhieu=='Nhiều'):
                temp = cv2.medianBlur(getImagePathFromBrowser(file),7)
            imgout = chapter05.DenoiseMotion(temp)
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)