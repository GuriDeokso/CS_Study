import os
import zipfile

from collections import defaultdict


def search_zip_files(root_dir):
    try:
        files = os.listdir(root_dir)
        for file in files:
            full_filename = os.path.join(root_dir, file)
            if os.path.isdir(full_filename):
                search_zip_files(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.zip':
                    zip_files_by_dir_path[root_dir].append(full_filename)
                    print('target file:', full_filename)
    except PermissionError as e:
        print(e)


def extract_zip_file_with_renaming(dir_path, zip_file):
    global image_dir_path

    with zipfile.ZipFile(zip_file, 'r') as zip_obj:
        image_idx = 1
        for full_filename in zip_obj.namelist():
            file_name, ext = os.path.splitext(full_filename)
            keyword = file_name.split()[0]
            if ext == '.md':
                save_path = f"{os.path.join(dir_path, keyword)}{ext}"
                image_files_by_md_file.setdefault(save_path, [])
            else:
                save_path = f"{os.path.join(image_dir_path, keyword)}_{image_idx}{ext}"
                image_files_by_md_file[f"{os.path.join(dir_path, keyword)}.md"].append(save_path)
                image_idx += 1
            with open(save_path, "wb") as f:
                f.write(zip_obj.read(full_filename))
                print('extract path:', save_path)


def remove_zip_file(zip_file):
    if os.path.isfile(zip_file):
        print('remove zip file:', zip_file)
        os.remove(zip_file)


def update_image_path(md_file, image_files):
    global root_dir

    with open(md_file, 'r+') as f:
        idx = 0
        lines = []
        for line in f:
            if line.lstrip().startswith('!'):
                image_path = image_files.pop(0).replace(root_dir, '../')
                new_line = f'![image_{idx}]({image_path})\n'
                print('update image url:', new_line[:-1])
                lines = lines + [new_line]
            else:
                lines = lines + [line]
                pass
        f.seek(0)               # file pointer 위치를 처음으로 돌림
        f.writelines(lines)     # 수정한 lines를 파일에 다시 씀
        f.truncate()


if __name__ == '__main__':
    root_dir = './juoh/'
    image_dir_path = os.path.join(root_dir, 'image')
    zip_files_by_dir_path = defaultdict(list)
    image_files_by_md_file = defaultdict(list)
    search_zip_files(root_dir)
    for dir_path, zip_files in zip_files_by_dir_path.items():
        for zip_file in zip_files:
            extract_zip_file_with_renaming(dir_path=dir_path, zip_file=zip_file)
            remove_zip_file(zip_file)

    for md_file, image_files in image_files_by_md_file.items():
        update_image_path(md_file, image_files)
    print('finish')
