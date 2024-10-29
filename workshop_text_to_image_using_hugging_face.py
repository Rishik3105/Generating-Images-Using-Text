# -*- coding: utf-8 -*-
"""workshop_text to image_using hugging face.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12GOBSgZmK64A2r4zJQPcJ730-NYs7-Bh
"""

#installing transformer package
! pip install diffusers transformers accelerate

#CONNECTING WITH HUGGING FACE
from huggingface_hub import login
login(token="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")

#CHECK WE ARE USING CPU OR GPU IF IT IS CPU CHANGE IT TO GPU # GIVES TRUE IF WE ARE USING GPU FALSE IF WE ARE CPU
import torch
print(torch.cuda.is_available())

from diffusers import StableDiffusionPipeline
import torch   #torch library is used to create depp neural network
import matplotlib.pyplot as plt
#load the pre-trained stable diffusion model
model_id="stabilityai/stable-diffusion-2-1"
pipe=StableDiffusionPipeline.from_pretrained(model_id)
#ensure it is using GPU for faster generation
if torch.cuda.is_available():
  pipe.to("cuda")
else:
  print("GPU is not available using CPU")
#define the promt and generate an image
prompt="hello world in future city"
image=pipe(prompt).images[0]
#display the image using matplotlib
plt.imshow(image)
plt.axis("off")
plt.show()