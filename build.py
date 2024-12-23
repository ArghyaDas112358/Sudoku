import os
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
        return "dll"    # Windows
    else:
        raise RuntimeError(f"Unsupported operating system: {system}")

def build_shared_library(source_dir="cpp", output_dir="build"):
    """
    Compile the shared library using Make.
    
    Args:
        source_dir (str): Path to the directory containing the Makefile.
        output_dir (str): Path to the directory where the shared library will be placed.
    """
    library_ext = detect_library_extension()
    shared_lib_name = f"solver_lib.{library_ext}"
    shared_lib_path = os.path.join(output_dir, shared_lib_name)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    print(f"Cleaning previous build artifacts in {source_dir}...")
    try:
        subprocess.run(["make", "clean", f"OUTPUT_DIR={output_dir}"], cwd=source_dir, check=True)
    except subprocess.CalledProcessError:
        print("Error during cleanup. Please check your setup.")
        sys.exit(1)

    print("Building shared library...")
    try:
        subprocess.run(["make", f"OUTPUT_DIR={output_dir}"], cwd=source_dir, check=True)
    except subprocess.CalledProcessError:
        print("Error during compilation. Please check your setup.")
        sys.exit(1)

    # Check if the shared library was successfully built
    if not os.path.exists(shared_lib_path):
        print(f"Error: Shared library {shared_lib_name} was not found in {output_dir}.")
        sys.exit(1)

    print(f"Shared library successfully built: {shared_lib_path}")

if __name__ == "__main__":
    # Determine source and output directories
    source_dir = os.path.abspath("src/cpp")
    output_dir = os.path.abspath("build")

    build_shared_library(source_dir=source_dir, output_dir=output_dir)
