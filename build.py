# build.py

import platform
import subprocess
import sys

def detect_library_extension():
    """Detect the shared library extension based on the operating system."""
    system = platform.system()
    if system == "Darwin":
        return "dylib"  # macOS
    elif system == "Linux":
        return "so"     # Linux
    elif system == "Windows":
        return "pyd"    # Windows
    else:
        raise RuntimeError(f"Unsupported operating system: {system}")

def build_shared_library():
    """Compile the shared library using Make."""
    print("Cleaning previous build artifacts...")
    try:
        subprocess.run(["make", "clean"], cwd="board", check=True)
    except subprocess.CalledProcessError:
        print("Error during cleanup. Please check your setup.")
        sys.exit(1)

    print("Building shared library...")
    try:
        subprocess.run(["make"], cwd="board", check=True)
    except subprocess.CalledProcessError:
        print("Error during compilation. Please check your setup.")
        sys.exit(1)

if __name__ == "__main__":
    build_shared_library()
