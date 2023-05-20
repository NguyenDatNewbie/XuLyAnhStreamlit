import streamlit as st 
import os
import cv2
import XuLyAnh.Chapter04 as chapter4
def getImagePathFromBrowser(image_file):
    path_file = os.path.join("file_upload",image_file.name)
    with open(os.path.join("file_upload",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    fullpath = ""+os.getcwd()+"/"+path_file
    imgin = cv2.imread(fullpath,cv2.IMREAD_GRAYSCALE)
    return imgin

def XuLyAnhChapter4(option,file):
    if option == 'Spectrum':
        st.title('Spectrum')
        st.write('spectrum là một công cụ quan trọng trong xử lý ảnh và có nhiều ứng dụng hữu ích để giúp cải thiện chất lượng ảnh và phân tích các thông tin tần số trong ảnh')
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            imgout = chapter4.Spectrum(getImagePathFromBrowser(file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option == 'Highpass filter':
        st.title('Highpass filter')
        st.write('Highpass filter (bộ lọc thông cao) là một kỹ thuật trong xử lý ảnh được sử dụng để loại bỏ các tần số thấp trong một ảnh và chỉ giữ lại các tần số cao hơn. Tác dụng chính của highpass filter trong xử lý ảnh bao gồm: Loại bỏ nhiễu, phát hiện cạnh, tăng cường độ tương phản')
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            imgout = chapter4.FrequencyFilter(getImagePathFromBrowser(file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option == 'Notch Reject':
        st.title('Notch Reject')
        st.write('Notch Reject Filter (bộ lọc từ chối đỉnh) là một trong những kỹ thuật xử lý ảnh được sử dụng để loại bỏ các tần số đỉnh (notch) trong một ảnh. Tác dụng chính của Notch Reject Filter trong xử lý ảnh bao gồm: Loại bỏ nhiễu, giảm nhiễu qua hệ thống, lọc tần số, phát hiện tín hiệu')
        if file is not None:
            imgout = chapter4.DrawNotchRejectFilter()
            st.subheader("Kết quả")
            st.image(imgout,width=400)
    else:
        st.title('Xóa nhiễu moire')
        st.write('Nhiễu moire là một hiện tượng phổ biến trong xử lý ảnh xảy ra khi một hình ảnh được quét hoặc sao chụp từ một bề mặt có cấu trúc tương tự như lưới. Việc xóa nhiễu moiré là một bước quan trọng trong xử lý ảnh để cải thiện chất lượng ảnh và làm rõ các chi tiết.')
        if file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(file,width=400)
            imgout = chapter4.RemoveMoire(getImagePathFromBrowser(file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    