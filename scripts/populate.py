import os

image_folders = ["DigitalArt", "Minimal", "PixelArt", "Dynamic"]
image_folders.sort()
print(image_folders)

pre = """
# just a bunch of wallpapers.....
"""

post = """
</p>
"""
with open("./README.md", "w") as f:
    f.write(pre)

def image_embed(title,folder,img):
    return f"""<img src="{folder}/{img}" title="{title}"><br>\n"""

with open("./README.md", "a") as readme:
    for folder in image_folders:
        readme.write("\n\n## " + folder + "\n")
        readme.write("<details><summary></summary>\n")
        for file in os.listdir(folder):
            if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".gif") or file.endswith(".webp") or file.endswith(".webm"):
                readme.write(
                    image_embed(file[:-4], folder, file)
                )
        readme.write("</details>\n")
    readme.write(post)
