import os
import argparse
from PIL import Image

def create_gif(folder_path, output_filename, frame_duration):
    # List of file paths
    file_paths = sorted([os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if file_name.endswith('.png')])

    # Create an image object array
    images = [Image.open(file_path) for file_path in file_paths]

    # Create the GIF
    output_path = os.path.join(folder_path, output_filename)
    images[0].save(output_path, save_all=True, append_images=images[1:], optimize=False, duration=frame_duration, loop=0)

    print(f'GIF saved at {output_path}')

def main():
    parser = argparse.ArgumentParser(description='Create a GIF from PNG images in a directory.')
    parser.add_argument('folder_path', type=str, help='Directory containing PNG images')
    parser.add_argument('--output', type=str, default='output.gif', help='Output GIF filename')
    parser.add_argument('--duration', type=int, default=200, help='Duration of each frame in milliseconds')

    args = parser.parse_args()

    create_gif(args.folder_path, args.output, args.duration)

if __name__ == "__main__":
    main()
