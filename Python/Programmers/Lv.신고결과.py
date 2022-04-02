
def solution(id_list, report, k):
    answer = []
    a = list(set(report))
    dict1 = {name : 0 for name in id_list}
    dict2 = {name : [] for name in id_list}
    
    for i in a:
        dict2[i.split()[1]].append(i.split()[0])
        
    for i in dict2:
        if len(dict2[i]) >= k:
            for j in dict2[i]:
                dict1[j] += 1
                
    for i in dict1:
        answer.append(dict1[i])
        
    return answer
