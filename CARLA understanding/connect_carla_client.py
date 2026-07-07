# find the localhost address and use it to make connection to carla simulator if running the script through terminal

import carla

if __name__ == "__main__":
    try:
        client = carla.Client('localhost', 2000)
        world = client.get_world()
        print('connected to the carla simulator through API in this script')
    except:
            print(f"could not connect to the carla server. Please check if the carla is running")

