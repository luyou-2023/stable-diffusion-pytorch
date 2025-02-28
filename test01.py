from PIL import Image

from stable_diffusion_pytorch import pipeline

prompts = ["Visualize a Valentine's Day promotion, infused with a charming palette of reds and pinks. Picture an affectionate setting teeming with heart-shaped decorations, premium gift boxes, and exquisite roses. Incorporate modern and elegant typography amidst a neat and festive layout. An enticing promotional offer is prominently displayed, perfect for catching the eye of those browsing website banners."]
images = pipeline.generate(prompts)
images[0].save('output.jpg')

image = Image.open('output.jpg')
image.show()
# tar -xf data.v20221029.tar
