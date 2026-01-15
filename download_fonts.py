import urllib.request
import os

base_url = 'https://cdnjs.cloudflare.com/ajax/libs/remixicon/4.6.0/'
files = ['remixicon.css', 'remixicon.woff2', 'remixicon.woff', 'remixicon.ttf']
# Use relative path since we run from project root
dest_dir = os.path.join('static', 'home_files')

if not os.path.exists(dest_dir):
    print(f"Creating directory: {dest_dir}")
    os.makedirs(dest_dir)

print(f"Downloading to {dest_dir}...")
for f in files:
    url = base_url + f
    dest = os.path.join(dest_dir, f)
    print(f"Downloading {url} -> {dest}")
    try:
        urllib.request.urlretrieve(url, dest)
        print("Success.")
    except Exception as e:
        print(f"Error downloading {f}: {e}")
