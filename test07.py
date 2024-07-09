from stable_diffusion_pytorch import model_loader, pipeline

models = model_loader.preload_models('cpu')

prompts = ["a photograph of an astronaut riding a horse"]
images = pipeline.generate(prompts, models=models, device='cuda', idle_device='cpu')
images[0].save('output7.jpg')
