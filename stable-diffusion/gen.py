#!/bin/env python3

from diffusers import AutoPipelineForText2Image
import torch

pipeline = AutoPipelineForText2Image.from_pretrained(
	"/home/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16"
).to("cuda")

image = pipeline(
	"stained glass of darth vader, backlight, centered composition, masterpiece, photorealistic, 8k"
).images[0]

image.save("/home/helloworld.png");

