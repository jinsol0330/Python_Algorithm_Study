'''
캐시

LRU 알고리즘 : 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법

해당 값이 캐시 안에 있다면, 해당 값을 캐시의 가장 최근 위치로 넣어준다

해당 값이 캐시 안에 없다면, 캐시 길이 체크를 한다
 -> 캐시가 다 찼다면 가장 오래 전에 참조한 값을 빼고 현재 값을 캐시에 넣는다
 -> 캐시가 다 차지 않았다면 해당 값을 최근 위치로 넣어준다

'''

def solution(cacheSize, cities):
    answer = 0
    cities_upper = []
    cache = []

    if cacheSize == 0: 
        return len(cities) * 5

    # 대소문자 구분 X
    for city in cities:
        cities_upper.append(city.upper())

    for city in cities_upper:
        # 도시가 캐시 안에 있는 경우
        if city in cache:
            # cache hit
            answer += 1
            # 해당 도시를 꺼내
            cache.pop(cache.index(city))
            # 캐시의 가장 최근 위치로 넣어준다
            cache.append(city)
        # 도시가 캐시 안에 없는 경우
        else:
            # cache miss
            answer += 5
            # 캐시에 공간이 있다면
            if len(cache) < cacheSize:
                # 최근 위치로 넣는다
                cache.append(city)
            else:
                # 가장 오래된 값을 꺼내
                cache.pop(0)
                # 최근 위치로 넣어준다
                cache.append(city)

    return answer

cacheSize = 0 
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))