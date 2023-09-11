import os
import numpy as np
import cv2
from result_mask_main import result_mask
from image_to_video import images_to_video

def custom_save(video_state):
    """
    save_folder : folder to save the masks in png format
    npy_folder : folder to save the masks in npy format 
    mask_folder : folder to save the masks in jpg format
    """
    #===================================================================
    save_folder = './result/mask'
    npy_folder='./result/mask_npy'
    mask_folder='D:/OneDrive - Sogang/Sogang/23/papers/Track-Anything-master/result/mask/'
    #===================================================================
    
    print('aaaaaaaaaaaa{}/{}'.format(save_folder,video_state["video_name"].split('.')[0]))
    if not os.path.exists('{}/{}'.format(save_folder,video_state["video_name"].split('.')[0])):
        os.makedirs('{}/{}'.format(save_folder,video_state["video_name"].split('.')[0]))
    if not os.path.exists('{}/{}'.format(npy_folder,video_state["video_name"].split('.')[0])):
        os.makedirs('{}/{}'.format(npy_folder,video_state["video_name"].split('.')[0]))
    i = 0
    print("save mask")
    for mask in video_state["masks"]:
        np.save(os.path.join('{}/{}'.format(npy_folder, video_state["video_name"].split('.')[0]), '{:05d}.npy'.format(i)), mask)
        i+=1
        
    ##custom
    video_folder_name=video_state["video_name"].split('.')[0]+'/'#f'floor_new_val{i}/'
    npy_folder=npy_folder+'/'+video_folder_name
    save_folder = save_folder +'/'+video_folder_name
    result_mask(npy_folder, save_folder)
    
    
    video_name1=video_state["video_name"].split('.')[0]
    video_name= mask_folder+f'{video_name1}.avi'
    fps = 30
    crop_size=[255,255]
    images_to_video(mask_folder+video_name1+'/', video_name, fps, crop_size)