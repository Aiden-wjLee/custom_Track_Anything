

import cv2
import os

def images_to_video(image_folder, video_name, fps):
    images = [img for img in os.listdir(image_folder) if img.endswith(".png") or img.endswith(".jpg")]
    images.sort(key=lambda x: int(x.split('.')[0]))
    #print(images)
    print("len(images): ", len(images))
    # 첫 번째 이미지를 읽어, 비디오 해상도를 결정합니다.
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    frame = cv2.resize(frame,(255,255))
    print("fa",frame.shape)
    #cv2.imshow('frame',frame)
    #cv2.waitKey(0)
    height, width, _ = frame.shape
    print("hei",height)

    # VideoWriter 객체를 생성합니다.
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 설정 (XVID, MP4V 등)
    out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # 각 이미지를 프레임으로 추가합니다.
    for image in images:
        frame = cv2.imread(os.path.join(image_folder, image))
        frame = cv2.resize(frame,(255,255))
        out.write(frame)

    out.release()
    print(f"{image_folder} : Video saved successfully!")


def main():
    #image_folder = 'D:/OneDrive - Sogang/Sogang/23/papers/segment-anything-main (1)/segment-anything-main/notebooks/result/429_2120/'
    #image_folder='D:/OneDrive - Sogang/Sogang/23/papers/segment-anything-main (1)/segment-anything-main/notebooks/result_new/Shelf5_051_1926/'
    
    #'D:/C_data/Downloads/test6_video_pred_mask/content/Segment-and-Track-Anything/tracking_results/test6_video/test6_video_masks/'
    
    
    ###image_folder='D:/Dataset/prior/floor_new_val2/'
    #image_folder='D:/Dataset/nachi/images_real_connector/left/'
    image_folder='D:/OneDrive - Sogang/Sogang/23/papers/Track-Anything-master/result/mask/cross_red/'
    ###video_name = image_folder+'../floor_new_val2.avi'
    video_name= image_folder+'../left4.avi'
    fps = 30
    images_to_video(image_folder, video_name, fps)

if __name__ == "__main__":
    main()
