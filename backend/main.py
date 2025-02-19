import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from PIL import Image
import io
from processors.image_processor import ImageProcessor

app = FastAPI(
    title="ZainVision - Professional Image Processing API",
    description="Modern API for applying various styles and filters to images",
    version="1.0.0",
    contact={
        "name": "Zain Ul Abideen",
        "url": "https://zain-ul-abideen.vercel.app/",
        "email": "zain.dev00@gmail.com"
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# Configure CORS for Streamlit frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],  # Streamlit default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/styles")
async def get_styles():
    """Get available image processing styles with descriptions."""
    return {
        "styles": ImageProcessor.get_available_styles(),
        "descriptions": ImageProcessor.get_style_descriptions()
    }

@app.post("/process-image")
async def process_image(
    file: UploadFile = File(...),
    style: str = Query("original", description="Style to apply to the image"),
    intensity: float = Query(1.0, ge=0.0, le=1.0, description="Intensity of the effect (0.0 to 1.0)")
):
    """
    Process an uploaded image with the specified style and intensity.

    Args:
        file (UploadFile): The image file to process
        style (str): Style to apply to the image
        intensity (float): Intensity of the effect (0.0 to 1.0)

    Returns:
        Response: The processed image as a PNG file
    """
    try:
        # Read and validate the image
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Process the image
        processed_image = ImageProcessor.process_image(image, style, intensity)

        # Convert the processed image to bytes
        img_byte_arr = io.BytesIO()
        processed_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        return Response(
            content=img_byte_arr,
            media_type="image/png"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    """Get information about the API and its creator."""
    return {
        "app_name": "ZainVision Pro",
        "version": "1.0.0",
        "creator": {
            "name": "Zain Ul Abideen",
            "github": "https://github.com/Zain-Ul-Abideen00",
            "linkedin": "https://www.linkedin.com/in/zain-ul-abideen00/",
            "portfolio": "https://zain-ul-abideen.vercel.app/",
            "email": "zain.dev00@gmail.com"
        },
        "documentation": "/docs",
        "features": [
            "Multiple image processing styles",
            "Adjustable effect intensity",
            "Real-time processing",
            "Modern API design",
            "Comprehensive documentation"
        ]
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
