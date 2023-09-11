

import cv2
import os

def images_to_video(image_folder, video_name, fps, crop_size):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    images.sort(key=lambda x: int(x.split('.')[0]))
    print("len(images): ", len(images))
    
    # Read the first image to get height and width
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    frame = cv2.resize(frame,(crop_size[0],crop_size[1]))
    print("fa",frame.shape)
    height, width, _ = frame.shape
    print("hei",height)

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 설정 (XVID, MP4V 등)
    out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Add each frame to video
    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        frame = cv2.resize(frame,(crop_size[0],crop_size[1]))
        out.write(frame)

    out.release()
    print(f"{image_folder} : Video saved successfully!")


def main():
    """
    This is the main function where the program execution starts. 
    It specifies the path to the folder containing the images to be converted to video ('image_folder').
    It also sets the name of the output video ('video_name') and the frame rate ('fps').
    Finally, it calls the 'images_to_video' function to perform the conversion.
    args
        image_folder: path to the folder containing the images to be converted to video
        video_name: name of the output video
        crop_size: size of the images to be converted to video
    """
    #image_folder = 'D:/OneDrive - Sogang/Sogang/23/papers/segment-anything-main (1)/segment-anything-main/notebooks/result/429_2120/'
    #image_folder='D:/OneDrive - Sogang/Sogang/23/papers/segment-anything-main (1)/segment-anything-main/notebooks/result_new/Shelf5_051_1926/'
    #'D:/C_data/Downloads/test6_video_pred_mask/content/Segment-and-Track-Anything/tracking_results/test6_video/test6_video_masks/'
    ###image_folder='D:/Dataset/prior/floor_new_val2/'
    #image_folder='D:/Dataset/nachi/images_real_connector/left/'
    #image_folder='D:/OneDrive - Sogang/Sogang/23/papers/Track-Anything-master/result/mask/cross_red/'
    
    
    image_folder='D:/Dataset/nachi_test/origin/'
    if not image_folder.endswith('/'):
        image_folder = image_folder + '/'
    crop_size=[1280,512]
    video_name= image_folder+'../test.avi'
    fps = 30
    
    images_to_video(image_folder, video_name, fps, crop_size)

if __name__ == "__main__":
    main()
