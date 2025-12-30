from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    # Process the image
    inputs = processor(image, return_tensors="pt")
    
    # Generate the caption
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    
    print(f"Generated caption: {caption}")
    return caption

# Create Gradio interface
demo = gr.Interface(
    fn=generate_caption,
    inputs=[gr.Image(label='Upload Image')],
    outputs=[gr.Text(label='Generated Caption')],
    title="Image Captioning with BLIP",
    description="Upload an image and the BLIP model will generate a descriptive caption for it."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
