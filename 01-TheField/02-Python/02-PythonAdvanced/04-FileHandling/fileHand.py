import os

directory = 'data/'

txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

final_file_path = os.path.join(directory, 'final.txt')

with open(final_file_path, 'w') as final_file:
    for txt_file in txt_files:
        with open(os.path.join(directory, txt_file), 'r') as file:
            final_file.write(file.read() + '\n')

print(f"Content from all .txt files has been written to {final_file_path}")