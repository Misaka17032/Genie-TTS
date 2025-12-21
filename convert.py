import os
import sys
import shutil

os.environ["GENIE_DATA_DIR"] = r"./GenieData"
src_path = os.path.abspath(os.path.join(os.getcwd(), "src"))
if src_path not in sys.path:
    sys.path.append(src_path)

import genie_tts as genie

base_path = "./models/emma"
if os.path.exists(os.path.join(base_path, "out")):
    shutil.rmtree(os.path.join(base_path, "out"))
genie.convert_to_onnx(
    torch_pth_path=os.path.join(base_path, "raw", "emma_e20_s53400.pth"),
    torch_ckpt_path=os.path.join(base_path, "raw", "emma-e50.ckpt"),
    output_dir=os.path.join(base_path, "out")
)