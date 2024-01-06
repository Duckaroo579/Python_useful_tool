import os
import subprocess

def compress_video(input_path, output_path):
    """
    If an error occurs during execution, 
    please first confirm that ffmpeg is installed on your computer,
    and then restart the computer.
    """
    command = f'ffmpeg -i "{input_path}" -s vga -preset veryslow -r 20 -b:v 1M -crf 28 "{output_path}"'
    print(command)
    result = subprocess.run(command, shell=True, stderr=subprocess.PIPE)

    if result.returncode == 0:
        print(f"Compressed: {input_path}")
    else:
        print(f"Error compressing: {input_path}")
        print("Error message: ")
        print(result.stderr)

def batch_compress(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith(".mp4"):
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_folder, os.path.relpath(input_path, input_folder))
                
                # Create output directory if it doesn't exist
                output_dir = os.path.dirname(output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                    
                # do not override
                if os.path.exists(output_path):
                    continue
                compress_video(input_path, output_path)

if __name__ == "__main__":
    input_folder = r"C:\Users\user\Desktop\Song"  # 替換為你的輸入資料夾路徑
    output_folder = "Song"  # 替換為你的輸出資料夾路徑

    batch_compress(input_folder, output_folder)