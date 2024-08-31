import os

p = "C:\\Users\\turae\\Videos\\02. Quran\\02. Surahs\\02. DEEPER LOOK"
v = 'videos'
f = 'files'
t = 'list.txt'


def get_folder_id(p):
    folders = p.split(sep='C:\\Users\\turae\\Videos\\')[1].split(sep='\\')
    id = ''
    for fol in folders:
        id = id + fol.split(sep='.')[0]
    print(id)
    return id

def get_lists(path, folder):
    vl = os.listdir(os.path.join(path, folder, v))
    fl = os.listdir(os.path.join(path, folder, f))
    with open(os.path.join(path, folder, t), 'r') as file:
        tl = file.readlines()
    return vl, fl, tl



def main(p):

    folders = os.listdir(p)
    for folder in folders:
        id = get_folder_id(os.path.join(p, folder))
        vl, fl, tl = get_lists(path=p, folder=folder)
        for index, name in enumerate(tl):
            count = 0

            # changing video names
            oldVN = vl[index]
            if index < 10:
                NewVN = f"{id}.00{index}# {name.strip()}"
            elif 100 > index > 9:
                NewVN = f"{id}.0{index}# {name.strip()}"
            elif 200 > index > 99:
                NewVN = f"{id}.{index}# {name.strip()}"
            print(f"{oldVN} to {NewVN}")
            os.rename(src=os.path.join(p, folder, v, oldVN), dst=os.path.join(p, folder, v, NewVN))


            # # changing file names
            # for file in fl:
            #     if file.__contains__(name):
            #         count += 1
            #         if index < 10:
            #             NewFN = f"{id}.00{index}@0{count}# {name}"
            #         elif 100 > index > 9:
            #             NewFN = f"{id}.0{index}@0{count}# {name}"
            #         elif 200 > index > 99:
            #             NewFN = f"{id}.{index}@0{count}# {name}"
            #         print(f"{file} to {NewFN}")
            #


main(p)
