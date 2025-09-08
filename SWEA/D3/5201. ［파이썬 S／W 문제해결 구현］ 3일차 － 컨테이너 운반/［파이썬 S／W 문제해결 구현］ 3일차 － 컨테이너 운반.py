T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))
    
    # wi, ti 역정렬
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    
    # 적재한 양 초기값
    result = 0
    # 컨테이너 순회
    for i in range(N):
        # 트럭 순회
        for j in range(M):
            # 컨테이너 용량이 트럭 용량보다 크면 트럭 순회 멈춤
            if wi[i] > ti[j]:
                break
            # 그게 아니면
            else:
                # 결과에 적재량 더해주고
                result += wi[i]
                ti[j] = 0   # 트럭 용량 0으로 초기화
                ti.sort(reverse=True)   # 다시 정렬
                break

    print(f"#{tc} {result}")