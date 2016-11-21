'use strict';

$(document).ready(function() {
    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    function event_click_snmp_tab() {
        $(activeNow).removeClass("active");

        $(".message").load("/interfaces/snmp");

        activeNow = "#snmp-tab";
        $(activeNow).addClass("active");

        clearTimeout(timeout);
        timeout = setTimeout(function(){event_click_snmp_tab();}, 3000);
    };

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    function event_click_file_tab() {
        $(activeNow).removeClass("active");

        $(".message").load("/interfaces/filedata");

        activeNow = "#file-tab";
        $(activeNow).addClass("active");

        clearTimeout(timeout);
        timeout = setTimeout(function(){event_click_file_tab();}, 30000);
    };

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    function event_click_database_tab() {
        $(activeNow).removeClass("active");

        $(".message").load("/interfaces/database");

        activeNow = "#database-tab";
        $(activeNow).addClass("active");

        clearTimeout(timeout);
        timeout = setTimeout(function(){event_click_database_tab();}, 30000);
    };

    /*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
    $('#snmp-tab').bind('click', event_click_snmp_tab);
    $('#file-tab').bind('click', event_click_file_tab);
    $('#database-tab').bind('click', event_click_database_tab);

    var activeNow = "#file-tab";
    var timeout = setTimeout(function(){event_click_file_tab();}, 500);
});