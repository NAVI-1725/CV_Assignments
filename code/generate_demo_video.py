import cv2
import os

image_folder = r'C:\Users\kumar\Navya_sree_ram_kumar_CVAssignment\output'
video_name = r'C:\Users\kumar\Navya_sree_ram_kumar_CVAssignment\output\video_output.mp4'

if not os.path.exists(image_folder):
    raise ValueError(f"Folder {image_folder} does not exist.")

images = sorted([img for img in os.listdir(image_folder) if img.lower().endswith((".png", ".jpg"))])

if not images:
    raise ValueError(f"No images found in {image_folder}.")

first_frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_frame.shape

fps = 2 if len(images) > 5 else 1

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

for idx, img_name in enumerate(images):
    frame = cv2.imread(os.path.join(image_folder, img_name))
    if frame is not None:
        video.write(frame)
    print(f"[{idx+1}/{len(images)}] Writing frame: {img_name}")

video.release()
print("✅ Video Created Successfully Sir 👑!")
