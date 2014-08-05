/**
 * Created by kenanbek on 8/5/14.
 */

$(document).ready(document_ready);
function document_ready() {
    $("button").click(function () {
        $.ajax({
            url: "/sample1/hello",
            type: "get",
            success: function (data) {
                alert(data);
            },
            error: function (data) {
                alert("Error. " + "Status: " + data.status + " Text: " + data.statusText);
            }
        });
    })
}
