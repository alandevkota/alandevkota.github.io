import cv2
import os
from PIL import Image

# Define the video files to convert
video_files = [
    "./MultimodalTransformerAcceleration/object-detected-video.mp4",
    "./MultimodalTransformerAcceleration/object-detected-webcam.mp4"
]

# Convert each video to GIF using OpenCV and PIL
for video_path in video_files:
    if os.path.exists(video_path):
        print(f"Processing: {video_path}")
        
        # Create output GIF path
        gif_path = video_path.replace(".mp4", ".gif")
        
        # Open the video file
        cap = cv2.VideoCapture(video_path)
        
        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Read frames (sample every N frames to reduce size)
        frames = []
        frame_skip = max(1, fps // 10)  # Target ~10 fps
        frame_num = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Only keep every Nth frame
            if frame_num % frame_skip == 0:
                # Convert BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                
                # Resize to reduce file size (width=640)
                height, width = frame_rgb.shape[:2]
                new_width = 640
                new_height = int(height * (new_width / width))
                frame_resized = cv2.resize(frame_rgb, (new_width, new_height))
                
                # Convert to PIL Image
                pil_img = Image.fromarray(frame_resized)
                frames.append(pil_img)
            
            frame_num += 1
        
        cap.release()
        
        # Save as GIF
        if frames:
            duration = int(1000 / 10)  # 10 fps in milliseconds
            frames[0].save(
                gif_path,
                save_all=True,
                append_images=frames[1:],
                duration=duration,
                loop=0,
                optimize=True
            )
            print(f"Successfully converted: {video_path} -> {gif_path}")
            print(f"  Created GIF with {len(frames)} frames")
        else:
            print(f"No frames extracted from {video_path}")
    else:
        print(f"File not found: {video_path}")