import cv2
import numpy as np
from PIL import Image
import io

class ImageProcessor:
    @staticmethod
    def _pil_to_cv2(pil_image):
        """Convert PIL Image to CV2 format."""
        numpy_image = np.array(pil_image)
        return cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    @staticmethod
    def _cv2_to_pil(cv2_image):
        """Convert CV2 image to PIL format."""
        color_converted = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
        return Image.fromarray(color_converted)

    @staticmethod
    def process_image(image: Image.Image, style: str, intensity: float = 1.0) -> Image.Image:
        """
        Apply the selected style to the input image.

        Args:
            image (PIL.Image): Input image
            style (str): Style to apply
            intensity (float): Intensity of the effect (0.0 to 1.0)

        Returns:
            PIL.Image: Processed image
        """
        # Convert PIL image to CV2 format
        cv2_image = ImageProcessor._pil_to_cv2(image)

        if style == "grayscale":
            gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
            processed = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "sepia":
            kernel = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
            processed = cv2.transform(cv2_image, kernel)
            processed = np.clip(processed, 0, 255).astype(np.uint8)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "blur":
            kernel_size = int(15 * intensity) | 1  # Ensure odd number
            processed = cv2.GaussianBlur(cv2_image, (kernel_size, kernel_size), 0)

        elif style == "edge_detection":
            edges = cv2.Canny(cv2_image, 100, 200)
            edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, edges, intensity, 0)

        elif style == "sharpen":
            kernel = np.array([[-1,-1,-1],
                             [-1, 9,-1],
                             [-1,-1,-1]]) * intensity
            processed = cv2.filter2D(cv2_image, -1, kernel)

        elif style == "vintage":
            processed = cv2.convertScaleAbs(cv2_image, alpha=1.1, beta=10)
            rows, cols = processed.shape[:2]
            kernel_x = cv2.getGaussianKernel(cols, 200)
            kernel_y = cv2.getGaussianKernel(rows, 200)
            kernel = kernel_y * kernel_x.T
            mask = 255 * kernel / np.linalg.norm(kernel)
            for i in range(3):
                processed[:,:,i] = processed[:,:,i] * mask
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "cool_tone":
            b, g, r = cv2.split(cv2_image)
            b = cv2.convertScaleAbs(b, alpha=1.2, beta=10)
            processed = cv2.merge([b, g, r])
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "warm_tone":
            b, g, r = cv2.split(cv2_image)
            r = cv2.convertScaleAbs(r, alpha=1.2, beta=10)
            processed = cv2.merge([b, g, r])
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "pencil_sketch":
            gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
            inv = 255 - gray
            blur = cv2.GaussianBlur(inv, (21, 21), 0)
            sketch = cv2.divide(gray, 255 - blur, scale=256.0)
            processed = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "hdr_effect":
            hdr = cv2.detailEnhance(cv2_image, sigma_s=12, sigma_r=0.15)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, hdr, intensity, 0)

        elif style == "cartoon":
            # Cartoon effect
            gray = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(cv2_image, 9, 300, 300)
            cartoon = cv2.bitwise_and(color, color, mask=edges)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, cartoon, intensity, 0)

        elif style == "invert":
            processed = cv2.bitwise_not(cv2_image)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, processed, intensity, 0)

        elif style == "emboss":
            kernel = np.array([[-2,-1,0],
                             [-1, 1,1],
                             [ 0, 1,2]]) * intensity
            processed = cv2.filter2D(cv2_image, -1, kernel) + 128

        elif style == "watercolor":
            # Simulate watercolor effect
            bilateral = cv2.bilateralFilter(cv2_image, 9, 75, 75)
            median = cv2.medianBlur(bilateral, 5)
            processed = cv2.addWeighted(cv2_image, 1 - intensity, median, intensity, 0)

        else:
            processed = cv2_image

        # Ensure output is in valid range
        processed = np.clip(processed, 0, 255).astype(np.uint8)

        # Convert back to PIL format
        return ImageProcessor._cv2_to_pil(processed)

    @staticmethod
    def get_available_styles():
        """Return a list of available image processing styles."""
        return [
            "grayscale",
            "sepia",
            "blur",
            "edge_detection",
            "sharpen",
            "vintage",
            "cool_tone",
            "warm_tone",
            "pencil_sketch",
            "hdr_effect",
            "cartoon",
            "invert",
            "emboss",
            "watercolor"
        ]

    @staticmethod
    def get_style_descriptions():
        """Return descriptions for each available style."""
        return {
            "grayscale": "Convert image to black and white",
            "sepia": "Add a warm, vintage brown tone",
            "blur": "Apply Gaussian blur effect",
            "edge_detection": "Highlight edges in the image",
            "sharpen": "Enhance image details and edges",
            "vintage": "Apply a retro filter with warm tones",
            "cool_tone": "Enhance blue tones for a cool effect",
            "warm_tone": "Enhance red tones for a warm effect",
            "pencil_sketch": "Convert image to pencil sketch style",
            "hdr_effect": "Enhance local contrast for HDR-like effect",
            "cartoon": "Transform image into cartoon style",
            "invert": "Invert image colors",
            "emboss": "Create an embossed effect",
            "watercolor": "Create a watercolor painting effect"
        }
