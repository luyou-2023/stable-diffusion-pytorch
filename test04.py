from stable_diffusion_pytorch import pipeline

uncond_prompts = ["low quality"]
prompts = ["a photograph of an astronaut riding a horse"]
images = pipeline.generate(prompts, uncond_prompts, seed=42)
images[0].save('output4.jpg')

prompts = ["a photograph of an astronaut riding a horse"]
images = pipeline.generate(prompts, uncond_prompts, seed=42)
images[0].save('output5.jpg')
