import streamlit as st 
from io import BytesIO 
from PIL import Image
from rembg import remove 
from cartoonizer import cartoonize
import cv2 as cv 
st.set_page_config(layout="wide",page_title="Image Background Remover")
st.title("Image Background Remover")
st.write(":dog:**Try uploading an image to watch the background magically removed**")
st.sidebar.write("## Upload and Download :gear:")
my_upload = st.sidebar.file_uploader("Upload an image", type =['jpg','jpeg','png'])
alpha_matting = st.sidebar.checkbox("Use Alpha Matting ",value= True)
threshold = st.sidebar.slider("Background Threshold",min_value=0,max_value=255,value =50,step=5)
def converts_images (image):
    buf = BytesIO()
    image.save(buf,format='PNG')
    byte_im = buf.getvalue()
    return byte_im
def remove_bg(my_upload,threshold,alpha_matting):
    image = Image.open(my_upload)
    col1,col2 = st.columns(2)
    col1.write("**Original Image** :camera:")
    col1.image(image)
    col2.write("**Fixed Image**:wrench:")
    fixed = remove(image,alpha_matting=alpha_matting,alpha_matting_background_threshold=threshold)
    col2.image(fixed)
    st.write("## Cartoonize Image")
    cartoon = cartoonize(image)
    image = Image.fromarray(cartoon)
    st.image(image)
    st.sidebar.download_button("Download Fixed Image",converts_images(fixed),"fixed.png")
    st.sidebar.download_button("Download Cartoonized Image",converts_images(image),"cartoon.png")
if my_upload:remove_bg(my_upload,threshold,alpha_matting)
else :  remove_bg(r"D:\AI\AI Models\3. OpenCV\Deployment File\images\cat.jpg",threshold,alpha_matting)