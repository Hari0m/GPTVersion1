import os
import lzma
from tqdm import tqdm


def xz_files_in_dir(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".xz") and os.path.isfile(os.path.join(directory, file)):
            files.append(filename)
    return files


folder_path = "D:/LLMs/openwebtext/openwebtext"
output_file = "output{}.txt"
vocab_file = "vocab.txt"
split_files = int(input("How many files to this split into? "))

files = xz_files_in_dir(folder_path)

total_files = len(files)

max_count = total_files // split_files if split_files != 0 else total_files
vocab = set()

for i in range(split_files):
    with open(output_file.format(i), "w", encoding="utf-8") as outfile:
        for count, filename in enumerate(tqdm(files[:max_count], total=max_count)):
            if count >= max_count:
                break
            file_path = os.path.join(folder_path, filename)
            with lzma.open(file_path, "rt", encoding="utf-8") as infile:
                text = infile.read()
                outfile.write(text)
                characters = set(text)
                vocab.update(characters)
        files = files[max_count:]
with open(vocab_file, "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char+"\n")