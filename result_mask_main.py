import numpy as np
import cv2
import os
from tqdm import tqdm
#load ./mask/00001.npy


#my_array = np.load('./result/mask/test10_video/00001.npy')*255
#print(my_array.shape)
#cv2.imshow('image', my_array)
#cv2.waitKey(0)
def result_mask(npy_folder, save_folder):
    # npy 파일이 저장된 폴더 내의 모든 파일에 대해 반복
    if not os.path.exists(save_folder):
        os.makedirs(save_folder, exist_ok=True)
    else:
        print("폴더가 이미 존재합니다.")
    for i, npy_file in enumerate(tqdm(os.listdir(npy_folder), desc='npy save')):
        #print(npy_file)
        if npy_file.endswith('.npy'):
            # 파일 이름에서 확장자 제거 후, 이미지를 저장할 폴더 경로 생성
            video_name = os.path.splitext(npy_file)[0]
            
        #save_path = os.path.join(save_folder, video_name)
        
            # npy 파일 읽어오기
            npy_path = os.path.join(npy_folder, npy_file)
            img_array = np.load(npy_path)
            
            save_path = os.path.join(save_folder, video_name)
            # 이미지 저장
            img_path = os.path.join(save_path+".png")
                #print(save_path)
            if i==0:
                max_value = img_array.max()
            cv2.imwrite(img_path, img_array*255.0/max_value)
    print(f"{save_folder} 이미지 저장 완료")

def main():
    #for i in range (1, 17):
    #    video_folder_name=f'green{i}/'
    #    npy_folder='./result/mask_npy/'+video_folder_name
    #    save_folder = './result/mask/'+video_folder_name
    #    result_mask(npy_folder, save_folder)
    for i in range (1, 2):
       video_folder_name='right_blue/'#f'floor_new_val{i}/'
       npy_folder='./result/mask_npy/'+video_folder_name
       save_folder = './result/mask/'+video_folder_name
       result_mask(npy_folder, save_folder)
if __name__ == '__main__':
    main()