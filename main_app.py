# Library imports
import numpy as np
import streamlit as st
import cv2
from keras.models import load_model
import tensorflow as tf
from PIL import Image
import io

# Page configuration
st.set_page_config(
    page_title="Plant Disease Detection",
    page_icon="🌱",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #00ff00;
        text-align: center;
        margin-bottom: 2rem;
    }
    .upload-section {
        background-color: #f0f0f0;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .prediction-box {
        background-color: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #00ff00;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_plant_model():
    """Load the plant disease detection model"""
    try:
        model = load_model('plant_disease_model.h5')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Loading the Model
model = load_plant_model()

# Name of Classes
CLASS_NAMES = ('Tomato-Bacterial_spot', 'Potato-Barly blight', 'Corn-Common_rust')

# Setting Title of App
st.markdown('<h1 class="main-header">🌱 Plant Disease Detection 🔍</h1>', unsafe_allow_html=True)
st.markdown("### Upload an image of a plant leaf to detect diseases")

# Sidebar for additional information
with st.sidebar:
    st.header("ℹ️ About")
    st.markdown("""
    This application uses a Convolutional Neural Network (CNN) to detect plant diseases.
    
    **Supported Plants:**
    - 🍅 Tomato
    - 🥔 Potato  
    - 🌽 Corn
    
    **Detected Diseases:**
    - Bacterial Spot
    - Early Blight
    - Common Rust
    """)
    
    st.header("📋 Instructions")
    st.markdown("""
    1. Upload a clear image of a plant leaf
    2. Click 'Predict Disease' button
    3. View the prediction results
    """)

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader("📤 Upload Image")
    
    # Uploading the plant image
    plant_image = st.file_uploader(
        "Choose an image...", 
        type=["jpg", "jpeg", "png"],
        help="Upload a clear image of a plant leaf"
    )
    
    submit = st.button('🔍 Predict Disease', type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    if plant_image is not None:
        st.subheader("📷 Preview")
        # Display the uploaded image
        image = Image.open(plant_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

# On predict button click
if submit:
    if plant_image is not None and model is not None:
        try:
            with st.spinner("🔍 Analyzing image..."):
                # Convert the file to an opencv image
                file_bytes = np.asarray(bytearray(plant_image.read()), dtype=np.uint8)
                opencv_image = cv2.imdecode(file_bytes, 1)
                
                # Resizing the image
                opencv_image = cv2.resize(opencv_image, (256, 256))
                
                # Convert image to 4 Dimension
                opencv_image = opencv_image.reshape(1, 256, 256, 3)
                
                # Make Prediction
                Y_pred = model.predict(opencv_image)
                result = CLASS_NAMES[np.argmax(Y_pred)]
                
                # Extract plant and disease information
                plant_name = result.split('-')[0]
                disease_name = result.split('-')[1]
                confidence = float(np.max(Y_pred)) * 100
                
                # Display results
                st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
                st.success(f"✅ **Prediction Complete!**")
                st.markdown(f"""
                **Plant:** {plant_name} 🌱
                
                **Disease:** {disease_name} 🦠
                
                **Confidence:** {confidence:.2f}% 📊
                """)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Additional information based on disease
                if "Bacterial_spot" in disease_name:
                    st.info("💡 **Treatment:** Remove infected leaves and apply copper-based fungicides. Ensure proper plant spacing for air circulation.")
                elif "blight" in disease_name:
                    st.info("💡 **Treatment:** Apply fungicides containing chlorothalonil or mancozeb. Remove and destroy infected plant debris.")
                elif "rust" in disease_name:
                    st.info("💡 **Treatment:** Apply fungicides and ensure proper plant nutrition. Remove infected plant parts.")
                    
        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
            st.info("Please try uploading a different image or ensure the image is clear and properly formatted.")
    
    elif plant_image is None:
        st.warning("⚠️ Please upload an image first!")
    elif model is None:
        st.error("❌ Model could not be loaded. Please check the model file.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🌱 Plant Disease Detection System | Built with Streamlit and TensorFlow</p>
</div>
""", unsafe_allow_html=True)
