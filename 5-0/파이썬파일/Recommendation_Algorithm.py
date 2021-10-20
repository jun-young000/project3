def make_review_data(data, area, percentile=0.6):
    # num >>cnt_review
    cnt_review = pd.DataFrame(data.value_counts('name'))
    avg_star = data.pivot_table('rating', index='name', aggfunc='mean')

    # 평점/리뷰갯수 정보를 가지는 temp 변수 생성
    temp = avg_star.merge(cnt_review, left_index=True, right_index=True, how='left')
    temp.columns = ['rating', 'num']

    temp = temp.fillna(0)

    m = temp['num'].quantile(percentile)
    C = temp['rating'].mean()

    # 가충치 함수를 람다함수로 처리
    temp['weighted_rating'] = temp.apply(
        (lambda x: (x['num'] / (x['num'] + m) * x['rating']) + (m / (m + x['num']) * C)), axis=1)

    # 음식점 이름 + 지역을 기준으로 그룹화 시켜서
    name_area = pd.DataFrame(data.groupby(['name'])['category'].first())

    # 평점/리뷰갯수에 음식점 이름 + 지역 병합
    temp = temp.merge(name_area, left_index=True, right_index=True)

    # 사용자 위치에 해당되는 정보만 정리
    temp = temp[temp['category'] == area]

    # 정렬후 반환
    return temp[['rating', 'weighted_rating', 'num', 'category']].sort_values('weighted_rating', ascending=False)[:10]


import pandas as pd

if __name__ == '__main__':

    data = pd.read_csv('./data/네이버맵음식점평점_최종.csv')
    print('사용자 위치를 입력해주세요')
    print()
    input_data_area = input()

    info = make_review_data(data, input_data_area)

    info.reset_index(inplace=True)

    print()
    print()

    for i in range(10):
        print(i, ' 순위')
        print('음식점 이름 : ', info['name'][i], '평균 평점 : ', info['weighted_rating'][i])
        print()