jQuery(document).ready(function() {

    // 실시간 위치정보를 loc 변수에 저장한 뒤 해당 내용을 web console창에 띄움
    navigator.geolocation.getCurrentPosition(function(position) {
    var lat = position.coords.latitude
    var long = position.coords.longitude;

    console.log(lat, long)
    var state = [lat, long]
    });

    // 위치정보를 가져오지 못했을 경우 실행되는 함수
    navigator.geolocation.getCurrentPosition(success, function(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                // 사용자가 위치정보 사용을 허용하지 않았을 때
                break;
            case error.POSITION_UNAVAILABLE:
                // 위치 정보 사용이 불가능할 때
                break;
            case error.TIMEOUT:
                // 위치 정보를 가져오려 시도했지만, 시간이 초과되었을 때
                break;
            case error.UNKNOWN_ERROR:
                // 기타 알 수 없는 오류가 발생하였을 때
                break;
            }
    });


    // 사용자의 현재 위치정보를 가져와 모델과 비교한 후 웹(result_rest.html 및 result_tour.html)에 띄우기
    $.ajax({
    url: "/tmp_location",
    data: {state}, // 사용자가 현재 위치한 위도와 경도 받아오기
    type: "GET",
    dataType: "json"
    })

        // HTTP 요청이 성공하면 요청한 데이터가 done() 메소드로 전달됨
        .done(function(json) {
        $("<div class=\"name\">").html(json.html).appendTo("body");
         })

        // HTTP 요청이 실패하면 오류와 상태에 관한 정보가 fail() 메소드로 전달됨
        .fail(function(xhr, status, errorThrown) {
            $("#text").html("오류가 발생했습니다.<br>")
                .append("오류명: " + errorThrown + "<br>")
                .append("상태 :" + status)
        })

        // HTTP 요청이 성공하거나 실패하는 것에 상관없이 언제나 always() 메소드가 실행됨
        .always(function(xhr, status) {
            $("#text").html("요청이 완료되었습니다!");
        })
});









