import cv2
import os
import numpy as np
from tqdm import tqdm

def extract_frames(video_path, output_dir, max_frames=1000):
    """Extrae frames de videos y los guarda en carpetas clasificadas"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_count = 0
    
    for _ in tqdm(range(min(total_frames, max_frames)), desc=f"Processing {video_path}"):
        ret, frame = cap.read()
        if not ret:
            break
            
        frame_path = os.path.join(output_dir, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    
    cap.release()
    return frame_count

def prepare_dataset(violent_dir, non_violent_dir, output_dir, frames_per_video=300):
    """Prepara el dataset a partir de los directorios de videos"""
    violent_output = os.path.join(output_dir, "violent")
    non_violent_output = os.path.join(output_dir, "non_violent")
    
    # Procesar videos violentos
    for video_file in os.listdir(violent_dir):
        if video_file.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(violent_dir, video_file)
            extract_frames(video_path, violent_output, frames_per_video)
    
    # Procesar videos no violentos
    for video_file in os.listdir(non_violent_dir):
        if video_file.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(non_violent_dir, video_file)
            extract_frames(video_path, non_violent_output, frames_per_video)