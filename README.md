# 🎨 ZainVision Pro - Advanced Image Processing App

A modern, professional-grade image processing application that combines a Streamlit frontend with a FastAPI backend for powerful and intuitive image transformations.

## ✨ Features

### Image Processing
- **14+ Professional Filters:**
  - Grayscale
  - Sepia
  - Blur
  - Edge Detection
  - Sharpen
  - Vintage
  - Cool Tone
  - Warm Tone
  - Pencil Sketch
  - HDR Effect
  - Cartoon
  - Invert
  - Emboss
  - Watercolor

### User Interface
- Clean, modern dark-themed interface
- Real-time image preview
- Adjustable effect intensity
- Processing history tracking
- Image information display
- Drag-and-drop file upload
- One-click image download

### Technical Features
- FastAPI backend with OpenAPI documentation
- Asynchronous image processing
- Session state management
- Processing statistics
- Comprehensive error handling
- CORS configuration
- Responsive design

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Zain-Ul-Abideen00/zainvision-pro.git
   cd zainvision-pro
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Backend**
   ```bash
   python backend/main.py
   ```
   The API will be available at http://localhost:8000

5. **Start the Frontend**
   ```bash
   streamlit run frontend/app.py
   ```
   The web interface will open automatically in your browser

## 🛠️ Project Structure

```
zainvision-pro/
├── backend/
│   ├── main.py                 # FastAPI application
│   └── processors/
│       └── image_processor.py  # Image processing logic
├── frontend/
│   ├── app.py                 # Streamlit interface
│   └── .streamlit/
│       └── config.toml        # Streamlit configuration
├── requirements.txt           # Project dependencies
├── vercel.json               # Vercel deployment config
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
```

## 🌟 Usage

1. **Upload Image:**
   - Drag and drop your image or click to upload
   - Supports JPG, JPEG, and PNG formats

2. **Select Style:**
   - Choose from 14+ available styles
   - Read style descriptions for guidance

3. **Adjust Intensity:**
   - Use the slider to control effect strength (0.0 to 1.0)
   - See real-time preview of changes

4. **Process and Download:**
   - Click "Apply Style" to process
   - Download processed image with one click
   - View processing statistics and history

## 🚀 Deployment

### Vercel Deployment
1. Push to GitHub
2. Connect to Vercel
3. Configure build settings
4. Deploy

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

## 💻 Development

### Prerequisites
- Python 3.8+
- Node.js (for Vercel CLI)
- Git

### Setting Up Development Environment
1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Set up environment variables

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Creator

**Zain Ul Abideen**
- Portfolio: [https://zain-ul-abideen.vercel.app/](https://zain-ul-abideen.vercel.app/)
- GitHub: [@Zain-Ul-Abideen00](https://github.com/Zain-Ul-Abideen00)
- LinkedIn: [Zain Ul Abideen](https://www.linkedin.com/in/zain-ul-abideen00/)
- Email: zain.dev00@gmail.com

## 🙏 Acknowledgments

- OpenCV for image processing capabilities
- Streamlit for the amazing web framework
- FastAPI for the robust backend
- All contributors and users of this application
