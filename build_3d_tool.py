import base64
import os
import glob
import cv2
import json
import numpy as np

def main():
    """
    Pseudo-3D Image Augmentation App - Python Dataset Build Engine
    Packages custom images and labels into a standalone HTML application.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(current_dir, "dataset", "images")
    labels_dir = os.path.join(current_dir, "dataset", "labels")

    sample_items = []

    if os.path.exists(images_dir):
        image_files = glob.glob(os.path.join(images_dir, "*.[pP][nN][gG]")) + glob.glob(os.path.join(images_dir, "*.[jJ][pP][gG]"))
        for img_path in image_files:
            base_name = os.path.splitext(os.path.basename(img_path))[0]
            lbl_path = os.path.join(labels_dir, f"{base_name}.txt")

            img = cv2.imread(img_path)
            if img is None:
                continue

            bbox = [0.5, 0.5, 0.4, 0.4]
            cid = 0
            if os.path.exists(lbl_path):
                with open(lbl_path, "r") as f:
                    lines = f.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if parts:
                        cid = int(parts[0])
                        bbox = [float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])]
                        break

            _, buf = cv2.imencode(".png", img)
            b64_uri = "data:image/png;base64," + base64.b64encode(buf).decode("utf-8")

            h, w, _ = img.shape
            bx, by, bw, bh = bbox
            x1, y1 = max(0, int((bx - bw * 0.6) * w)), max(0, int((by - bh * 0.6) * h))
            x2, y2 = min(w, int((bx + bw * 0.6) * w)), min(h, int((by + bh * 0.6) * h))

            mask = np.zeros((h, w), dtype=np.uint8)
            cv2.rectangle(mask, (x1, y1), (x2, y2), 255, -1)
            clean_bg = cv2.inpaint(img, mask, 15, cv2.INPAINT_TELEA)

            _, bg_buf = cv2.imencode(".png", clean_bg)
            bg_b64_uri = "data:image/png;base64," + base64.b64encode(bg_buf).decode("utf-8")

            sample_items.append({
                "b64": b64_uri,
                "bgB64": bg_b64_uri,
                "name": base_name,
                "title": f"Custom Object ({base_name})",
                "bbox": bbox,
                "classId": cid,
                "className": "object"
            })

    print(f"✅ Successfully built dataset package with {len(sample_items)} items!")

if __name__ == "__main__":
    main()
