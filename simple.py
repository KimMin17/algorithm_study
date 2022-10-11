from collections import deque

def solution(alp, cop, problems):
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    answer = 0
    
    max_alp = 0
    max_cop = 0
    
    for item in problems:
        max_alp = max(max_alp, item[0])
        max_cop = max(max_cop, item[1])

    q = deque()
    q.appendleft((max_alp, max_cop))
    worst_time = max_alp + max_cop

    cost_map = [[worst_time for j in range(max_cop+1)] for i in range(max_alp+1)]
    cost_map[max_alp][max_cop] = 0

    while True:
        cur = q.pop()
        if cur[0] == alp and cur[1] == cop: break

        for item in problems:
            cur_alp = cur[0]
            cur_cop = cur[1]
            alp_req = item[0]
            cop_req = item[1]
            alp_rwd = item[2]
            cop_rwd = item[3]
            cost = item[4]

            alp_idx = cur_alp - alp_rwd
            cop_idx = cur_cop - cop_rwd
            if (alp_idx >= alp_req and cop_idx >= cop_req) and (cost_map[alp_idx][cop_idx] > cost_map[cur_alp][cur_cop] + cost):
                cost_map[alp_idx][cop_idx] = cost_map[cur_alp][cur_cop] + cost
                q.appendleft((alp_idx, cop_idx))
    
    answer = cost_map[alp][cop]
    return answer

alp = 10
cop = 10
problems = 	[[10,15,2,1,2],[20,20,3,3,4]]

print(solution(alp, cop, problems))