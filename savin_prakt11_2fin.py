pets_all={}
pets={}
zapros=0
index=0
command=""

# -- Функция формирования запроса --------------
def vvod_zapr(command):
        print("Какой ID Вас интересует? (0 для вывода всех)")
        zapros=int(input())
        if zapros==0:
                vyvod_all()
        else:
            if zapros in pets_all.keys():
                if command=="delete":
                    delete(zapros)
                    return
                elif command=="vyvod":
                    vyvod(zapros)
                    return
                elif command=="edit":
                    edit(zapros)
                    return pets
                else:
                    print("Команда не распознана")
                    return

            else:
                print("ID", zapros, " не найден в справочнике\n")
    

# -- Функция ввода и изменения данных ---------------------
def vvod():
    print("Нуге-с, батенька, как зовут больного?")
    name=input()
    print("И кто у нас",name,"?")
    vid=input()
    print("Сколько годиков исполнилось?")
    year=int(input())
    print("Представьтесь, пожалуйста")
    owner=input()
    pets_vn={"vid_k":vid,"year_k":year,"owner_k":owner}
    pets={name:pets_vn}
    return pets

# -- Функция определения суффикса возраста ----------------
def age(year):
    years=year-(year//10)*10
    if year>=5 and year<=14:
        years_n="лет"
    elif years==1:
        years_n="год"
    elif years==2 or years==3 or years==4:
        years_n="года"
    else:
        years_n="лет"
    return(years_n)

# -- Функция редактирования -------------------
def edit(zapros):
    vyvod(zapros)
    print("Отредактируйте данные")
    pets_all[zapros]=vvod()
    return

# -- Функция вывода всех -----------------------------------------
def vyvod_all():
    for key in pets_all:
        buff=("".join(list(pets_all[key].keys())))
        print("ID",key,pets_all[key][buff]["vid_k"],buff,". Владелец:",pets_all[key][buff]["owner_k"])
    return

# -- Функция удаления записи -----------------------------------------
def delete(zapros):
    del pets_all[zapros]
    print("Запись с ID",zapros," удалена\n")
    return

# -- Функция вывода данных -----------------------------------------
def vyvod(index):
    buff=("".join(list(pets_all[index].keys())))
    buff_year=pets_all[index][buff]["year_k"]
    print("ID",index,"Это",pets_all[index][buff]["vid_k"],"по кличке",buff,". Возраст питомца",buff_year,age(buff_year),". Владелец:",pets_all[index][buff]["owner_k"],"\n")
    return

# ------- Главное меню --------------------------------------------
# -- добавление, редактирование, удаление, список всех, вывод об одном ---
# -- create ---- update -------- delete -- list_all --- get_pet ----------

while command!="stop":
    print("Введите команду (vvod,vyvod,edit,delete,stop для выхода)")
    command=input()
    if command=="vvod":
        index+=1
        pets_all[index]=vvod() # добавление в словарь
        print("В словарь добавлен питомец с ID",index)
    elif command=="stop":
        exit()
    else: 
        vvod_zapr(command)
