$(document).ready(function () {
    $('#rootwizard').bootstrapWizard({
        onTabShow: function (tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index + 1;
            var $percent = ($current / $total) * 100;
            $('#rootwizard').find('.bar').css({width:$percent+'%'});
        },
        onNext: function (tab, navigation, index) {
            console.log("next tab clicked");
        }
    });
});
