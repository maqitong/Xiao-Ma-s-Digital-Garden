
import os
import imghdr

STATIC_DIR = 'static'

def detect_and_rename():
    for root, dirs, files in os.walk(STATIC_DIR):
        for f in files:
            filepath = os.path.join(root, f)
            # Skip if already has extension
            if '.' in f:
                continue
            
            # Detect type
            ext = imghdr.what(filepath)
            if not ext:
                # Try to read first bytes manually if imghdr fails (e.g. svg)
                with open(filepath, 'rb') as tmp:
                    header = tmp.read(10)
                if b'<svg' in header or b'<?xml' in header:
                    ext = 'svg'
                else:
                    print(f"Could not detect type for {filepath}")
                    continue
            
            if ext == 'jpeg': ext = 'jpg'
            
            new_name = f"{f}.{ext}"
            new_path = os.path.join(root, new_name)
            os.rename(filepath, new_path)
            print(f"Renamed {f} to {new_name}")

if __name__ == '__main__':
    detect_and_rename()
