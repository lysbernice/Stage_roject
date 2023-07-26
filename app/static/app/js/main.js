$(function() {
    $('#province_id').on("change", function(){
        province_id = $(this).val();
        //alert("Salut");
        $.get(
            "/admin/templates/zones/getCommunes",
            {
                province_id: province_id
            },
            function(data, textStatus, jqXHR){
                $("#id_commune").html(data);
            }
        );
    });
});

///fonction js pour appeller les provinces,communes et zones dans la classe user
$(function() {
    $('#id_province').on("change", function(){
        province_id = $(this).val();
        alert(id_province);
        $.get(
            "/admin/templates/utilisateurs/getCommunes",
            {
                province_id: province_id,
            },
            function(data, textStatus, jqXHR){
                $("#id_commune").html(data);
            }
        );
    });
});


$(function() {
    $('#id_commune').on("change", function(){
        commune_id = $(this).val();
        //alert(id_commune);
        $.get(
            "/admin/templates/utilisateurs/getZones",
            {
                commune_id: commune_id
            },
            function(data, textStatus, jqXHR){
                $("#id_zone").html(data);
            }
        );
    });
});