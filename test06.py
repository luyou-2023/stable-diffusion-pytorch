from stable_diffusion_pytorch import model_loader, pipeline

models = model_loader.preload_models('cuda')

prompts = ["a photograph of an astronaut riding a horse"]
images = pipeline.generate(prompts, models=models)

images[0].save('output6.jpg')
