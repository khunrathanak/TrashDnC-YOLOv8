import gradio as gr
from ultralytics import YOLO
from PIL import Image

# Load trained YOLOv8 model
model = YOLO("best.pt")

# Define the detection function
def detect_objects(image):
    results = model.predict(source=image, save=False)
    annotated = results[0].plot()
    return Image.fromarray(annotated)

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("## 🗑️ Waste Detection YOLOv8 Demo")
    gr.Markdown("Take a photo with your camera or upload one to classify and detect waste types.")

    with gr.Column():
        image_input = gr.Image(type="pil", label="Upload or Take Picture")
        submit_btn = gr.Button("Submit")

    output_image = gr.Image(label="Detection Result")

    submit_btn.click(fn=detect_objects, inputs=image_input, outputs=output_image)

if __name__ == "__main__":
    demo.launch()
