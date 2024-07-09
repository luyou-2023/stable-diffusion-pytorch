from stable_diffusion_pytorch import pipeline

prompts = ["a photograph of an astronaut riding a horse"]
uncond_prompts = ["low quality"]
images = pipeline.generate(prompts, uncond_prompts)
images[0].save('output3.jpg')
