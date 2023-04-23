import cv2
import os

def upscale_images(filenames, upscale_ratio):
    upscaled_images = []
    for filename in filenames:
        input_path = os.path.join('uploads', filename)
        output_path = os.path.join('images', f'upscaled_{filename}')

        image = cv2.imread(input_path)
        upscaled_image = cv2.resize(image, None, fx=upscale_ratio, fy=upscale_ratio, interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(output_path, upscaled_image)

        upscaled_images.append(f'upscaled_{filename}')

    return upscaled_images