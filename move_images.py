import os; import tqdm

images: str = "./images/"
all_directory: str = os.path.join(images,"All")

archive1: str = f"{images}archive"
archive3: str = f"{images}archive3"
archive4: str = f"{images}archive4"
archive5: str = f"{images}archive5"

archive1_dirs: list[str] = [os.path.join(archive1,"images")]
archive3_dirs: list[str] = [os.path.join(archive3,"test/images"),os.path.join(archive3,"train/images"),os.path.join(archive3,"valid/images")]
archive4_dirs: list[str] = [archive4]
archive5_dirs: list[str] = [os.path.join(archive5,"BOTTLE")]

all_dirs: list[str] = []
for dir in archive1_dirs: all_dirs.append(dir)
for dir in archive3_dirs: all_dirs.append(dir)
for dir in archive4_dirs: all_dirs.append(dir)
for dir in archive5_dirs: all_dirs.append(dir)

for majorIndex, dir in enumerate(all_dirs):
    for index, file in tqdm.tqdm(enumerate(os.listdir(dir)),desc="chambeando"):
        file_name: str = os.path.join(dir,file)
        if file_name.lower().endswith(".php") or file_name.lower().endswith(".xml"):
            os.remove(file_name)
        extension: str = ""
        if file_name.lower().endswith(".png"): extension = "png"
        if file_name.lower().endswith(".jpg"): extension = "jpg"
        if file_name.lower().endswith(".jpeg"): extension = "jpeg"
        os.rename(file_name,f"{all_directory}/{majorIndex}-{index}.")
