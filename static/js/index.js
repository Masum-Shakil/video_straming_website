$("#searchVideos").keypress(function (e) { 
    
    if (e.keyCode == 13){
        
        if($("#searchVideos").val()) {
            
            $.ajax({                       
                url: ajax_search_url,                   
                
                data: {
                    'search_input': $("#searchVideos").val()     
                },
                
                success: function (data) {   
                    $("#videoList").html(data);
                }
            });
        }
    }
});