from datasets import load_dataset
import os

path = 'Lazy_RAG_test/rag/dataset'
dataset = load_dataset("cmrc2018")

context = list(set([i['context'] for i in dataset['test']]))
chunk_size = 10
total_files = (len(context) + chunk_size - 1)
dataset_path = os.path.join(path, "cmrc2018")

os.makedirs(dataset_path, exist_ok=True)

for i in range(total_files):
    chunk = context[i*chunk_size: (i+1)*chunk_size]
    file_name = f"{dataset_path}/part_{i+1}.txt"
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write("\n".join(chunk))