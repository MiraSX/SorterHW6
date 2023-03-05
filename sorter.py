import shutil
from pathlib import Path


def normalize(name_file: str) -> str:
    translated = []
    translate_dict = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ы': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ь': '', 'ю': 'iu',
                      'я': 'ia', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ь': '', 'Ю': 'Yu', 'Я': 'Ya'}
    for i in name_file:
        if not i.isalnum() and i != '.':
            i = '_'
        i = translate_dict.get(i, i)
        translated.append(i)
    translated = ''.join(translated)

    return translated


def sorting(folder):

    img = ('JPEG', 'PNG', 'JPG', 'SVG')
    vid = ('AVI', 'MP4', 'MOV', 'MKV')
    doc = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
    muz = ('MP3', 'OGG', 'WAV', 'AMR')
    arch = ('ZIP', 'GZ', 'TAR')

    Path(folder + '/' + 'images').mkdir(exist_ok=True)
    Path(folder + '/' + 'video').mkdir(exist_ok=True)
    Path(folder + '/' + 'documents').mkdir(exist_ok=True)
    Path(folder + '/' + 'audio').mkdir(exist_ok=True)
    Path(folder + '/' + 'archives').mkdir(exist_ok=True)

    for i in Path(folder).glob('**\*'):

        if i.name == 'images' or i.name == 'video' or i.name == 'documents' or i.name == 'audio' or i.name == 'archives':
            continue
        if i.is_dir():
            continue
        if i.suffix.upper()[1:] in img:
            Path(i).rename(r'D:\trash\images'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in vid:
            Path(i).rename(r'D:\trash\video'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in doc:
            Path(i).rename(r'D:\trash\documents'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in muz:
            Path(i).rename(r'D:\trash\audio'+'\\' + normalize(i.name))
        elif i.suffix.upper()[1:] in arch:
            try:
                shutil.unpack_archive(
                    Path(i), r'D:\trash\archives' + '\\' + normalize(i.name))
            except:
                continue

    for empty in Path(folder).glob('**/*'):
        if empty.is_dir() and not list(empty.glob('*')):
            empty.rmdir()


sorting('')
