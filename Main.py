import streamlit as st
import matplotlib.pylab as plt
from PIL import Image
import io

from API import transfer_style 

def main():
    st.title("Neural Style Transfer Application")
    st.write("Upload your content and style images to generate a new artistic image!")

    model_path = "./model" 

    # --- Image Upload Section ---
    st.header("1. Upload Your Images")

    col1, col2 = st.columns(2) # Create two columns for a cleaner layout

    with col1:
        # Content Image Upload
        st.subheader("Content Image")
        content_file = st.file_uploader("Choose a Content Image...", type=["jpg", "png", "jpeg"], key="content_uploader")
        content_image = None
        if content_file is not None:
            content_image = Image.open(content_file)
            st.image(content_image, caption="Content Image Preview", use_column_width=True)

    with col2:
        # Style Image Upload
        st.subheader("Style Image")
        style_file = st.file_uploader("Choose a Style Image...", type=["jpg", "png", "jpeg"], key="style_uploader")
        style_image = None
        if style_file is not None:
            style_image = Image.open(style_file)
            st.image(style_image, caption="Style Image Preview", use_column_width=True)

    st.write("---") # Separator
    st.header("2. Generate Stylized Image")

    col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1]) 
    with col_btn2: 
        if st.button("Generate Stylized Image", use_container_width=True):
            if content_image is not None and style_image is not None:
                with st.spinner("Applying style transfer... This may take a moment."):
                    # Save uploaded images temporarily to pass paths to transfer_style
                    content_path = "temp_content.jpg"
                    style_path = "temp_style.jpg"
                    
                    content_image.save(content_path)
                    style_image.save(style_path)

                    try:
                        stylized_img_array = transfer_style(content_path, style_path, model_path)
                        
                        st.success("Style transfer complete!")
                        st.write("---")
                        st.header("3. Your Stylized Image")
                        
                        if stylized_img_array.dtype == 'float32' or stylized_img_array.dtype == 'float64':
                            stylized_img_array = (stylized_img_array * 255).astype('uint8')

                        st.image(stylized_img_array, caption="Stylized Image", use_column_width=True)

                        
                        buf = io.BytesIO()
                        plt.imsave(buf, stylized_img_array, format='jpeg') # Save to buffer
                        byte_im = buf.getvalue()
                        st.download_button(
                            label="Download Stylized Image",
                            data=byte_im,
                            file_name="stylized_image.jpeg",
                            mime="image/jpeg"
                        )

                    except Exception as e:
                        st.error(f"An error occurred during style transfer: {e}")
                        st.info("Please ensure your 'model' directory is correctly placed and the image formats are supported (.jpg, .png).")
            else:
                st.warning("Please upload both a content image and a style image to proceed.")

if __name__ == "__main__":
    main()