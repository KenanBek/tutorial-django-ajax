/**
 * Created by kenanbek on 8/5/14.
 */

$(document).ready(function () {
    $('#rootwizard').bootstrapWizard({
        onTabShow: function (tab, navigation, index) {
            var $total = navigation.find('li').length;
            var $current = index + 1;
            var $percent = ($current / $total) * 100;
            $('#form-progress').css({width: $percent + '%'});
        }
    });
});