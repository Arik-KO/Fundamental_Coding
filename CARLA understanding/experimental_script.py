
import carla

client = carla.Client('localhost',2000)
world = client.get_world()

client.load_world('Town01')
spectator = world.get_spectator()
transform = spectator.get_transform()

location = transform.location
rotation = transform.rotation

spectator.set_transform(carla.Transform())