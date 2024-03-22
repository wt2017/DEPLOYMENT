#!/bin/env python3

import os
import sys
from diffusers import AutoPipelineForText2Image
import torch

def generate(filename, text):

    pipeline = AutoPipelineForText2Image.from_pretrained(
	"/home/stable-diffusion-v1-5", torch_dtype=torch.float16, variant="fp16"
    ).to("cuda")

    image = pipeline(text).images[0]
    image.save(filename);

    print(f"Picture Is Successfully Generated !")


# Parse command-line arguments.
if len(sys.argv) != 3:
    raise ValueError("This script requires exactly two arguments - a filename and some text to write to it.")

# Call the function with the parsed arguments.
generate(sys.argv[1], sys.argv[2])
