import os.path

os.chdir("main")
answer = set()
for current_dir, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            answer.add(current_dir[2:])
print(output := "\n".join(sorted(answer)))
with open("out_file.txt", "w") as out_file:
    out_file.write(output)