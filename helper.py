import os

def get_image_full_directory(directory):
    images_list = os.listdir(image_path)
    images_full_list =[]
    for image in images_list:
        im_f = os.path.join(directory,image)
        images_full_list.append(im_f)
    return images_full_list
