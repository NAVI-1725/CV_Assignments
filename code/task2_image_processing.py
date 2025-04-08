import cv2
import os

def add_watermark(img, text, position=(10, 30)):
    shadow_color = (0, 0, 0)
    text_color = (0, 255, 0)
    cv2.putText(img, text, (position[0]+2, position[1]+2), cv2.FONT_HERSHEY_SIMPLEX, 0.7, shadow_color, 2, cv2.LINE_AA)
    cv2.putText(img, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, text_color, 2, cv2.LINE_AA)
    return img

def process_image(input_path, output_dir, student_name="Baswa Tanusree Reddy", roll_no="CS22B1020"):
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    image = cv2.imread(input_path)
    if image is None:
        raise ValueError(f"Could not read image from {input_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hist_eq = cv2.equalizeHist(gray)
    blurred = cv2.GaussianBlur(hist_eq, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(edges, kernel, iterations=1)
    dilated_bgr = cv2.cvtColor(dilated, cv2.COLOR_GRAY2BGR)

    watermark_text = f"{student_name} {roll_no}"

    gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    hist_eq_bgr = cv2.cvtColor(hist_eq, cv2.COLOR_GRAY2BGR)
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    gray_bgr = add_watermark(gray_bgr, watermark_text)
    hist_eq_bgr = add_watermark(hist_eq_bgr, watermark_text)
    edges_bgr = add_watermark(edges_bgr, watermark_text)
    dilated_bgr = add_watermark(dilated_bgr, watermark_text)

    cv2.imwrite(os.path.join(output_dir, f"{base_name}_gray_{roll_no}.jpg"), gray_bgr)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_hist_{roll_no}.jpg"), hist_eq_bgr)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_edge_{roll_no}.jpg"), edges_bgr)
    cv2.imwrite(os.path.join(output_dir, f"{base_name}_final_{roll_no}.jpg"), dilated_bgr)

    print(f"[✓] All images saved to '{output_dir}' with watermark and shadow effect.")

if __name__ == "__main__":
    input_img = r"C:\Users\kumar\Navya_sree_ram_kumar_CVAssignment\input\sample.jpg"
    output_folder = r"C:\Users\kumar\Navya_sree_ram_kumar_CVAssignment\output"
    process_image(input_img, output_folder)
