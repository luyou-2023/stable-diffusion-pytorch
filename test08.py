from stable_diffusion_pytorch import model_loader, pipeline

from PIL import Image

prompts = ["a photograph of an astronaut riding a horse"]
input_images = [Image.open('space.jpg')]
images = pipeline.generate(prompts, input_images=input_images)

images[0].save('output7.jpg')
