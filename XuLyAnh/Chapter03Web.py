import streamlit as st 
import os
import cv2
import XuLyAnh.Chapter03 as chapter3

def getImagePathFromBrowser(image_file):
    path_file = os.path.join("./file_upload",image_file.name)
    with open(os.path.join("./file_upload",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    fullpath = ""+os.getcwd()+"/"+path_file
    imgin = cv2.imread(fullpath,cv2.IMREAD_GRAYSCALE)
    return imgin
def getImageColorPathFromBrowser(image_file):
    path_file = os.path.join("file_upload",image_file.name)
    with open(os.path.join("file_upload",image_file.name),"wb") as f:
        f.write(image_file.getbuffer())
    fullpath = ""+os.getcwd()+"/"+path_file
    imgin = cv2.imread(fullpath,cv2.IMREAD_COLOR)
    return imgin
def XuLyAnhChuong3(option,image_file):
    if option == 'Negative':
        st.title('Negative')
        st.write('Tác dụng của negative trong xử lý ảnh là tăng tính tương phản của ảnh và giúp những đối tượng trong ảnh nổi bật hơn. Khi sử dụng kỹ thuật negative, các màu sáng sẽ trở thành màu tối và ngược lại, giúp các đối tượng tối sẽ trở nên nổi bật hơn trong ảnh.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = chapter3.Negative(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
            
    elif option == 'Logarit':
        st.title('Logarit')
        st.write('Thuật toán logarit được sử dụng trong xử lý ảnh để tăng độ tương phản của ảnh, giúp các chi tiết và đối tượng trong ảnh nổi bật hơn. Thuật toán logarit được áp dụng trên giá trị độ sáng (luminance) của từng pixel trong ảnh.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = chapter3.Logarit(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option == 'Lũy thừa':
        st.title('Lũy Thừa')
        st.write('Thuật toán power trong xử lý ảnh được sử dụng để thay đổi độ sáng của ảnh bằng cách tăng hoặc giảm bậc lũy thừa của từng pixel trong ảnh. Kỹ thuật này được sử dụng để cân bằng độ sáng và tăng độ tương phản của ảnh.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            st.spinner()
            imgout = chapter3.Power(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option == 'Biến đổi tuyến tính':
        st.title('Biến đổi tuyến tính')
        st.write('Kỹ thuật này cho phép thay đổi hình dạng, kích thước, góc quay, phóng to, thu nhỏ và bố cục của ảnh.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = chapter3.PiecewiseLinear(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
                
    elif option == 'Histogram':
        st.title('Histogram')
        st.write(' Histogram trong xử lý ảnh được sử dụng để phân tích và biểu diễn phân bố độ sáng của một ảnh. Phân bố độ sáng của ảnh thường được biểu diễn bằng một biểu đồ đường gọi là histogram.')
        if image_file is not None:
            optionHistogram = st.radio('Loại histogram',('Cơ bản','Cân bằng sáng','Cân bằng ảnh màu','Local','Thống kê'),horizontal=True)
            
            if optionHistogram=='Cơ bản':
                imgout = chapter3.Histogram(getImagePathFromBrowser(image_file))
            elif optionHistogram=='Cân bằng sáng':
                st.write('Dựa trên thông tin phân bố độ sáng của ảnh, thuật toán cân bằng độ sáng sẽ tăng độ tương phản của ảnh bằng cách điều chỉnh phân bố độ sáng sao cho giá trị trung bình của ảnh tại mỗi giá trị độ sáng là như nhau.')
                imgout = chapter3.HistEqual(getImagePathFromBrowser(image_file))
            elif optionHistogram=='Cân bằng ảnh màu':
                st.write('Histogram cũng được sử dụng để phân tích phân bố độ sáng của từng kênh màu (R, G, B) trong ảnh màu để thực hiện các thao tác xử lý màu.')
                imgout = chapter3.HistEqualColor(getImageColorPathFromBrowser(image_file))
            elif optionHistogram=='Local':
                st.write('Thuật toán local histogram trong xử lý ảnh được sử dụng để phân tích và cân bằng độ sáng tại từng vùng nhỏ trên ảnh. Khác với thuật toán Histogram truyền thống, thuật toán local histogram sẽ tính histogram của từng vùng trên ảnh thay vì tính histogram của toàn bộ ảnh.')
                imgout = chapter3.LocalHist(getImagePathFromBrowser(image_file))
            else:
                st.write('thuật toán thống kê histogram sẽ tính toán các thông số thống kê như trung bình, độ lệch chuẩn và phân bố xác suất của giá trị độ sáng trong ảnh. Điều này giúp xác định các đặc trưng quan trọng của phân bố độ sáng trong ảnh, như trung bình, độ tương phản và sự phân tán.')
                imgout = chapter3.HistStat(getImagePathFromBrowser(image_file))
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
                
    elif option=='Lọc box':
        st.title('Lọc box')
        st.write('Lọc box (Box filter) là một kỹ thuật xử lý ảnh thường được sử dụng để làm mờ hoặc giảm nhiễu ảnh. Kỹ thuật này sử dụng một bộ lọc có hình dạng hình hộp (box) và áp dụng bộ lọc này cho từng vùng nhỏ của ảnh để tính toán giá trị trung bình.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = cv2.blur(getImagePathFromBrowser(image_file),(21,21))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option=='Lọc Gauss':
        st.title('Lọc Gauss')
        st.write('Lọc Gauss (Gaussian filter) là một kỹ thuật xử lý ảnh để làm mờ hoặc giảm nhiễu ảnh bằng cách sử dụng hàm Gauss để tính toán các trọng số cho từng pixel trong ảnh. Kỹ thuật này là một trong những kỹ thuật xử lý ảnh phổ biến nhất.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = cv2.GaussianBlur(getImagePathFromBrowser(image_file),(43,43),7.0)
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option=='Phân ngưỡng':
        st.title('Phân Ngưỡng')
        st.write('Thuật toán phân ngưỡng (thresholding) trong xử lý ảnh là một phương pháp đơn giản để phân loại các pixel trong ảnh thành hai nhóm khác nhau (thường là đen và trắng) dựa trên giá trị của chúng. Phân ngưỡng thường được sử dụng để trích xuất các đối tượng hay các khu vực quan tâm từ ảnh ban đầu.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = chapter3.Threshold(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option=='Lọc median':
        st.title('Lọc Median')
        st.write('Lọc median (median filter) là một phương pháp xử lý ảnh để giảm nhiễu và làm mờ ảnh bằng cách thay thế giá trị của một pixel bằng giá trị trung vị của các pixel xung quanh nó trong một khu vực xác định.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = cv2.medianBlur(getImagePathFromBrowser(image_file),7)
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    elif option=='Sharpen':
        st.title('Sharpen')
        st.write('Sharpen (còn được gọi là làm nét ảnh) là một kỹ thuật xử lý ảnh để làm tăng độ rõ nét của các đường viền và chi tiết trong ảnh bằng cách tăng độ tương phản của chúng.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = chapter3.Sharpen(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
    else: 
        st.title('Gradient')
        st.write('Gradient trong xử lý ảnh là một phương pháp để tính toán độ dốc của một ảnh bằng cách tính toán đạo hàm của ảnh theo hướng x và y. Gradient thường được sử dụng để phát hiện biên của các đối tượng trong ảnh.')
        if image_file is not None:
            col1 ,col2 = st.columns(2)
            with col1:
                st.subheader("Ảnh chưa xử lý")
                st.image(image_file,width=400)
            imgout = chapter3.Gradient(getImagePathFromBrowser(image_file))
            with col2:
                st.subheader("Ảnh đã qua xử lý")
                st.image(imgout,width=400)
