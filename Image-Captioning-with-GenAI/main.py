from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import gradio as gr

processr = BlipProcessor.from_pretrained("microsoft/blip-image-captioning-base")