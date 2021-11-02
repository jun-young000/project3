var tourspots = JSON.parse('"{{ tourspotJson|escapejs }}"');
console.log(tourspots)


var positions = [];
for (var i = 0; i < Object.keys(tourspots).length; i++) {
    var content = {
        name: tourspots[i].name,
        latlng: new kakao.maps.LatLng(tourspots[i].lng, tourspots[i].lat),
        address: tourspots[i].address,
    }
    positions.push(content);
};
console.log(positions);

// 마커 찍기
// 마커 이미지의 이미지 주소
var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
for (var i = 0; i < positions.length; i++) {
    // 마커 이미지의 크기
    var imageSize = new kakao.maps.Size(24, 35);
    // 마커 이미지 생성
    var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize);
    // 마커 생성
    var marker = new kakao.maps.Marker({
        map: map, // 마커를 표시할 지도
        position: positions[i].latlng, // 마커를 표시할 위치
        name: positions[i].name, // 마커의 타이틀, 마커에 마우스를 올리면 식당 명이 표시됨
        image: markerImage // 마커이미지
    })
}