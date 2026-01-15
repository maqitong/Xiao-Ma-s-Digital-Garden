
import requests
import sys
import time

BASE_URL = "http://127.0.0.1:8000"

ROUTES = [
    ("/", "Xiao Ma's Digital Garden"),
    ("/resume", "Resume"),
    ("/projects", "Projects"),
    ("/gallery", "Gallery"),
    ("/videos", "Videos"),
    ("/blog", "Blog"),
]

STATIC_FILES = [
    "/static/home_files/css2.css",
    "/static/projects_files/search-image.jpg"
]

def check_server():
    print("Checking server status...")
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            print("Server is up and running.")
            return True
    except requests.exceptions.ConnectionError:
        print("Server is NOT running.")
        return False
    return False

def verify_routes():
    print("\nVerifying routes...")
    all_passed = True
    for route, keyword in ROUTES:
        url = f"{BASE_URL}{route}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Check for keyword (case insensitive)
                if keyword.lower() in response.text.lower():
                    print(f"✅ {route}: OK")
                else:
                    print(f"⚠️ {route}: OK (200), but keyword '{keyword}' not found in content (might be okay if dynamic).")
            else:
                print(f"❌ {route}: Failed with status {response.status_code}")
                all_passed = False
        except Exception as e:
            print(f"❌ {route}: Error {e}")
            all_passed = False
    return all_passed

def verify_static():
    print("\nVerifying static files...")
    all_passed = True
    for path in STATIC_FILES:
        url = f"{BASE_URL}{path}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"✅ {path}: OK")
            else:
                print(f"❌ {path}: Failed with status {response.status_code}")
                all_passed = False
        except Exception as e:
            print(f"❌ {path}: Error {e}")
            all_passed = False
    return all_passed

if __name__ == "__main__":
    if not check_server():
        print("Please start the server first using 'uvicorn app.main:app --reload'")
        sys.exit(1)
    
    routes_ok = verify_routes()
    static_ok = verify_static()
    
    if routes_ok and static_ok:
        print("\n✨ All checks passed! The application is running correctly.")
    else:
        print("\n🚫 Some checks failed. Please review the errors above.")
