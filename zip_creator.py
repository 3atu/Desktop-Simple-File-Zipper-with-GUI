import zipfile
import pathlib

def make_archive(filepaths, dest_dir):#function will iterate over filepaths provided by user and place them in the destination directory folder
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        filepath = pathlib.Path(filepath)
        for filepath in filepaths:
            archive.write(filepath, arcname=filepath.name)

#testing the function (anyhting below if name == main is ignored if file is imported into another file)
if __name__ == "__main__":
    make_archive(filepaths=[""])
