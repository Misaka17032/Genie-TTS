import os
import sys

os.environ["GENIE_DATA_DIR"] = r"./GenieData"
src_path = os.path.abspath(os.path.join(os.getcwd(), "src"))
if src_path not in sys.path:
    sys.path.append(src_path)

import genie_tts as genie
import time
import glob

base_path = "./models/emma"

genie.load_character(
    character_name='emma',
    onnx_model_dir=os.path.join(base_path, "out"),
    language='jp',
)

refer = glob.glob(os.path.join(base_path, "*.wav"))[0]
genie.set_reference_audio(
    character_name='emma',
    audio_path=refer,
    audio_text=os.path.splitext(os.path.basename(refer))[0],
)

t1 = time.time()
genie.tts(
    character_name='emma',
    text='どうしようかな……やっぱりやりたいかも……！',
    split_sentence=False,
    play=False,
    save_path="./out.wav"
)
t2 = time.time()
print(f"Time taken: {t2 - t1} seconds")