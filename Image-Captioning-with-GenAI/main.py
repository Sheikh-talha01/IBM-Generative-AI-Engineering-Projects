from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


# made a   function
def generate_caption(image):
    img_input =  Image.fromarray(image)
    print(img_input)
    return ""


demo = gr.Interface(fn=generate_caption,
                    inputs=[gr.Image(label = 'Image')],
                    outputs=[gr.Text(label = 'Caption')])

demo.launch()