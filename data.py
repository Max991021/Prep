def separate(list_1,list_2):
    return [tuple(i) for i in zip(list_1,list_2)]
print(separate([12, 15, 18],[45, 48, 51]))

def occur(lis):
    return {x:lis.count(x) for x in lis}
print(occur(["Bafana", "Soccer", "Bafana", "Goals", "Soccer", "Bafana"]))

def common(dic):
    lis = []
    for key,value in dic.items():
        lis.append(value)
    print(lis)
    count = len(lis)
    for key,value in dic.items():
        lis.extend(value)
    
    
    return {item for item in lis if lis.count(item) == count}
    
            
print(common({
    "Lerato": ["Python", "SQL", "Git", "Docker"],
    "Thabo":  ["Python", "SQL", "Java", "Git"],
    "Nandi":  ["Python", "SQL", "Git", "React"]
}))

def flat(lis):
    new = []
    for i in lis:
        if isinstance(i, list):
            new.extend(flat(i))
        else:
            new.append(i)
    return new
print(flat([["Maths", "English"], ["Science", "History"], ["Art", "PE", "Coding"]]))

def slider(lis,k):
    new = []
    
    for i,e in enumerate(lis):
        new.append(sum(lis[:k]))
        lis.pop(i)
    return new
print(slider([2, 4, 6, 8, 10],3))
def group(provinces):
    new_dic = {}
    
    for items in provinces:
        new_dic.setdefault(items['province'], []).append(items['city'])
    return new_dic
print(group([
    {"city": "Durban",           "province": "KwaZulu-Natal"},
    {"city": "Pietermaritzburg", "province": "KwaZulu-Natal"},
    {"city": "Bloemfontein",    "province": "Free State"},
    {"city": "Welkom",          "province": "Free State"},
    {"city": "Polokwane",       "province": "Limpopo"}
]))
    