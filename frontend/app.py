import streamlit as st
import httpx
from PIL import Image
import io
import time

# Configure the app
st.set_page_config(
    page_title="ZainVision - Professional Image Processing",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
        margin-bottom: 80px;
    }
    .stButton>button {
        width: 100%;
        font-size: 2rem;
        background-color: transparent;
        color: #ffff;
        border: 2px solid #ffff;
        padding: 0.5rem;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        border: 2px solid #0099CC;
        color: #0099CC;
        scale: 1.01;
        transition: scale 0.3s ease;
        font-weight: 700;
    }
    .footer-container {
        margin-top: 3rem;
    }
    .footer {
        background-color: #1E1E1E;
        border-radius: 10px;
        color: #FFFFFF;
        padding: 1.5rem;
        text-align: center;
        border-top: 1px solid #333;
    }
    .footer p {
        margin: 0;
        padding: 0;
        font-size: 0.9rem;
    }
    .social-links {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin-top: 0.8rem;
    }
    .social-links a {
        color: #00BFFF;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s ease;
    }
    .social-links a:hover {
        color: #87CEEB;
        text-decoration: none;
    }
    .stAlert {
        background-color: #1E1E1E;
        color: white;
        border: 1px solid #333;
    }
    .stats-box {
        background-color: #1E1E1E;
        padding: 1rem;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .feature-box {
        background-color: #1E1E1E;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border: 1px solid #333;
    }
    .feature-box h3 {
        color: #00BFFF;
        margin-bottom: 0.5rem;
    }
    .feature-box p {
        color: #FFFFFF;
        margin: 0;
    }
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Constants
API_URL = st.secrets.get("API_URL", "https://zain-vision-pro.vercel.app")  # Vercel deployment URL

# Add a debug message to verify the API URL
if st.secrets.get("DEBUG", False):
    st.sidebar.info(f"API URL: {API_URL}")

# Session state initialization
if 'processing_history' not in st.session_state:
    st.session_state.processing_history = []
if 'total_processed' not in st.session_state:
    st.session_state.total_processed = 0
if 'processing_times' not in st.session_state:
    st.session_state.processing_times = []

def get_api_info():
    """Fetch API information including available styles."""
    try:
        with httpx.Client() as client:
            styles_response = client.get(f"{API_URL}/styles")
            info_response = client.get(f"{API_URL}/")
            return styles_response.json(), info_response.json()
    except Exception as e:
        st.error(f"Failed to fetch API information: {str(e)}")
        return None, None

def process_image(image_file, style, intensity):
    """Send image to backend for processing and return processed image."""
    try:
        start_time = time.time()
        files = {"file": image_file}
        params = {"style": style, "intensity": intensity}

        with httpx.Client() as client:
            response = client.post(
                f"{API_URL}/process-image",
                files=files,
                params=params
            )

        processing_time = time.time() - start_time
        st.session_state.processing_times.append(processing_time)

        if response.status_code == 200:
            # Update statistics
            st.session_state.total_processed += 1
            st.session_state.processing_history.append({
                "style": style,
                "intensity": intensity,
                "time": processing_time
            })
            return Image.open(io.BytesIO(response.content))
        else:
            st.error(f"Error processing image: {response.text}")
            return None
    except Exception as e:
        st.error(f"Failed to process image: {str(e)}")
        return None

def display_statistics():
    """Display processing statistics."""
    if st.session_state.total_processed > 0:
        avg_time = sum(st.session_state.processing_times) / len(st.session_state.processing_times)

        st.sidebar.markdown("### Processing Statistics")
        col1, col2 = st.sidebar.columns(2)

        with col1:
            st.metric("Total Processed", st.session_state.total_processed)
        with col2:
            st.metric("Avg. Process Time", f"{avg_time:.2f}s")

def display_features():
    """Display app features in a modern layout."""
    st.markdown("## 🚀 Key Features")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="feature-box">
            <h3>🎨 Professional Filters</h3>
            <p>Access a wide range of professional-grade image filters and effects, from classic styles to artistic transformations.</p>
        </div>

        <div class="feature-box">
            <h3>🎯 Precise Control</h3>
            <p>Fine-tune your effects with intensity controls and real-time previews for perfect results.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
            <h3>⚡ Fast Processing</h3>
            <p>Experience lightning-fast image processing with our optimized backend and efficient algorithms.</p>
        </div>

        <div class="feature-box">
            <h3>📊 Processing History</h3>
            <p>Track your image processing history and statistics for better workflow management.</p>
        </div>
        """, unsafe_allow_html=True)

def display_usage_tips():
    """Display usage tips and guidelines."""
    st.markdown("## 💡 Pro Tips")

    st.info("""
    **Get the Best Results:**
    1. Start with high-quality images for optimal results
    2. Experiment with different intensity levels
    3. Combine multiple styles by processing images sequentially
    . Save your favorite processed images for future reference
    """)

def main():
    # Get API information
    styles_info, api_info = get_api_info()
    if not styles_info or not api_info:
        st.error("Failed to connect to the API. Please ensure the backend server is running.")
        return

    # App header with new title
    st.title("🎨 ZainVision Pro")
    st.markdown("""
    Transform your images with professional-grade filters and artistic effects. Experience advanced
    image processing with intuitive controls and real-time previews.
    """)

    # Display features section
    display_features()

    # Display statistics
    display_statistics()

    # Sidebar
    with st.sidebar:
        st.header("Controls")

        # Image upload
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=["jpg", "jpeg", "png"]
        )

        # Style selection with descriptions
        st.subheader("Style Options")
        selected_style = st.selectbox(
            "Select Style",
            ["original"] + styles_info["styles"],
            format_func=lambda x: x.replace("_", " ").title()
        )

        # Show style description
        if selected_style in styles_info["descriptions"]:
            st.info(styles_info["descriptions"][selected_style])

        # Intensity slider
        intensity = st.slider(
            "Effect Intensity",
            min_value=0.0,
            max_value=1.0,
            value=1.0,
            step=0.1,
            help="Adjust the strength of the selected effect"
        )

        # Process button
        process_button = st.button("Apply Style", use_container_width=True)

        # Recent processing history
        if st.session_state.processing_history:
            st.markdown("### Recent Processing History")
            for i, hist in enumerate(reversed(st.session_state.processing_history[-5:])):
                st.markdown(f"""
                    **{i+1}.** {hist['style'].title()}
                    Intensity: {hist['intensity']:.1f} | Time: {hist['time']:.2f}s
                """)

        # Add information about the creator
        st.markdown("---")
        st.markdown("### About the Creator")
        st.markdown(f"""
        **{api_info['creator']['name']}**

        Connect with me:
        - [GitHub]({api_info['creator']['github']})
        - [LinkedIn]({api_info['creator']['linkedin']})
        - [Portfolio]({api_info['creator']['portfolio']})
        - ✉️ {api_info['creator']['email']}
        """)

    # Main content area
    if uploaded_file is not None:
        # Create columns for before/after display
        col1, col2 = st.columns(2)

        # Display original image
        with col1:
            st.subheader("Original Image")
            original_image = Image.open(uploaded_file)
            st.image(original_image, use_column_width=True)

        # Process and display styled image
        with col2:
            st.subheader("Processed Image")
            if process_button:
                with st.spinner("Processing image..."):
                    # Reset file pointer
                    uploaded_file.seek(0)

                    # Process image
                    processed_image = process_image(uploaded_file, selected_style, intensity)

                    if processed_image:
                        st.image(processed_image, use_column_width=True)

                        # Add download button with custom filename
                        buf = io.BytesIO()
                        processed_image.save(buf, format="PNG")
                        timestamp = time.strftime("%Y%m%d_%H%M%S")
                        st.download_button(
                            label="💾 Download Processed Image",
                            data=buf.getvalue(),
                            file_name=f"zainvision_{selected_style}_{timestamp}.png",
                            mime="image/png",
                            use_container_width=True
                        )

                        # Display image information
                        st.markdown("#### Image Information")
                        st.markdown(f"""
                        - **Style Applied:** {selected_style.replace('_', ' ').title()}
                        - **Intensity:** {intensity:.1f}
                        - **Original Size:** {original_image.size}
                        - **Processing Time:** {st.session_state.processing_times[-1]:.2f} seconds
                        """)
    # Display usage tips
    display_usage_tips()
    # Footer
    st.markdown(
        """
        <div class="footer-container">
            <div class="footer">
                <p>© 2025 ZainVision Pro | Developed by Zain Ul Abideen</p>
                <div class="social-links">
                    <a href="https://github.com/Zain-Ul-Abideen00" target="_blank">
                        <span>👨‍💻 GitHub</span>
                    </a>
                    <a href="https://www.linkedin.com/in/zain-ul-abideen00/" target="_blank">
                        <span>🔗 LinkedIn</span>
                    </a>
                    <a href="https://zain-ul-abideen.vercel.app/" target="_blank">
                        <span>🌐 Portfolio</span>
                    </a>
                    <a href="mailto:zain.dev00@gmail.com">
                        <span>✉️ Email</span>
                    </a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
