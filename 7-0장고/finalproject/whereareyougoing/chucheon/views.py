from django.shortcuts import render
import json

# Create your views here.

def main(request) :
    return render(request, "chucheon/index.html")
# chucheon / templates ... 어쩌구 안 쓰고 index.html 파일의 바로 위 디렉토리만 표시해줘야 함 (안 그러면 TemplatedoesnotExist 에러 발생)


def showtourspots(request) :
    with open('../static/json/tourspot_latlng.json', encoding='utf-8') as json_file:
        tourspots = json.load(json_file)['name']['address']['Latitude']['Longitude']

    tourspotdict = []
    # 불러온 json 객체들 중 필요한 데이터만 뽑기
    for tourspot in tourspots :
        # if tourspot.get('Latitude') :
        content = {
            "name": tourspot['name'],
            "address": tourspot['address'],
            "lat": str(tourspot['Latitude']), # y좌표
            "lng": str(tourspot['Longitude']), # x좌표
        }
        tourspotdict.append(content)
    tourspotJson = json.dumps(tourspotdict, ensure_ascii=False)
    print(tourspotJson)
    return render(request, 'chucheon/index.html', {'tourspotJson': tourspotJson})

