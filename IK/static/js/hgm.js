$.fn.extend({
// HG ToolTip
HGTooltip : function(options){

    /* HG ToolTip Patterns of Use
        // ToolTip Options Parameters
        position: {"top","right","bottom","left"}
        title: {""}
        color: {"default","success","info","primary","warning","danger"}
    */

    var thisObject = $(this)
    var thisObjectOptions = options
    if(thisObjectOptions == undefined){thisObjectOptions = {}}

    if(thisObject.length > 1){
        thisObject.each(function(){
            $(this).HGTooltip(thisObjectOptions)
        });
        return false;
    }
        if (thisObjectOptions.functionType == undefined){
            if (thisObject.data('hg-tooltip-functionType') == undefined){
              thisObjectOptions.functionType = "mouseover"
            }
            else{
                thisObjectOptions.functionType = thisObject.data('hg-tooltip-functionType')
            }
        }
        if (thisObjectOptions.position == undefined){
            if (thisObject.data('hg-tooltip-position') == undefined){
              thisObjectOptions.position = "top"
            }
            else{
                thisObjectOptions.position = thisObject.data('hg-tooltip-position')
            }
        }
        if (thisObjectOptions.title == undefined){
            if (thisObject.data('hg-tooltip-title') == undefined){
                thisObjectOptions.title = "Uyarı !"
            }
            else{
                thisObjectOptions.title = thisObject.data('hg-tooltip-title')
            }
        }
        if (thisObjectOptions.bgColor == undefined){
            if (thisObject.data('hg-tooltip-bgcolor') == undefined){
                thisObjectOptions.bgColor = "warning"
            }
            else{
                thisObjectOptions.bgColor = thisObject.data('hg-tooltip-bgcolor')
            }
        }
        if (thisObjectOptions.effect == undefined){
            if (thisObject.data('hg-tooltip-effect') == undefined){
                thisObjectOptions.effect = "default"
            }
            else{
                thisObjectOptions.effect = thisObject.data('hg-tooltip-effect')
            }
        }

        var thisObjectOptionsFunctionType = thisObjectOptions.functionType.toLowerCase()
        var thisObjectOptionsPosition = thisObjectOptions.position.toLowerCase()
        var thisObjectOptionsTitle = thisObjectOptions.title
        var thisObjectOptionsColor = thisObjectOptions.bgColor.toLowerCase()
        var thisObjectOptionsEffect = thisObjectOptions.effect.toLowerCase()

        if(thisObjectOptionsColor == "default"){thisObjectOptionsColor = "#bdc3c7"}
        else if(thisObjectOptionsColor == "success"){thisObjectOptionsColor = "#2ecc71"}
        else if(thisObjectOptionsColor == "info"){thisObjectOptionsColor = "#3498db"}
        else if(thisObjectOptionsColor == "primary"){thisObjectOptionsColor = "#2980b9"}
        else if(thisObjectOptionsColor == "warning"){thisObjectOptionsColor = "#e67e22"}
        else if(thisObjectOptionsColor == "danger"){thisObjectOptionsColor = "#e74c3c"}

        var HGToolTipid = Math.floor((Math.random() * 10000))
        var toolTipObject;

        var HGTooltipOperation = function(object){
            if(object != undefined){
                thisObject = object
            }

            $('html').append('\
            <div id="id_HGToolTip'+HGToolTipid+'" class="hg-tooltip fade '+thisObjectOptionsPosition+' in" role="hg-tooltip" style="display: block;">\
                <div class="hg-tooltip-arrow"style="border-'+thisObjectOptionsPosition+'-color:'+thisObjectOptionsColor+';"></div>\
                <div class="hg-tooltip-inner" style="background-color:'+thisObjectOptionsColor+';">'+thisObjectOptionsTitle+'</div>\
            </div>\
            ')

            var thisObjectPositions = thisObject.position()
            toolTipObject = $('#id_HGToolTip'+  HGToolTipid)

            if(thisObjectOptionsPosition == 'top'){
                var thisObjectPositionsTop = thisObjectPositions.top - thisObject.outerHeight()
                var thisObjectPositionsLeft = thisObjectPositions.left + (thisObject.outerWidth() / 2 - (toolTipObject.outerWidth() / 2))
            }
            else if(thisObjectOptionsPosition == 'right'){
                var thisObjectPositionsTop = thisObjectPositions.top + (thisObject.outerHeight() / 2 - toolTipObject.outerHeight()+2)
                var thisObjectPositionsLeft = thisObjectPositions.left + thisObject.outerWidth()
            }
            else if(thisObjectOptionsPosition == 'bottom'){
                var thisObjectPositionsTop = thisObjectPositions.top + thisObject.outerHeight()
                var thisObjectPositionsLeft = thisObjectPositions.left + (thisObject.outerWidth() / 2 - (toolTipObject.outerWidth() / 2))
            }
            else if(thisObjectOptionsPosition == 'left'){
                var thisObjectPositionsTop = thisObjectPositions.top - (thisObject.outerHeight() / 2 - toolTipObject.outerHeight()+2)
                var thisObjectPositionsLeft = thisObjectPositions.left - toolTipObject.outerWidth() 
            }
            if(thisObjectOptionsEffect != "default"){
                toolTipObject.css({'left':thisObjectPositionsLeft+'px','top':thisObjectPositionsTop+'px'}).effect( thisObjectOptionsEffect, {}, 500);
            }
            else{
                toolTipObject.css({'left':thisObjectPositionsLeft+'px','top':thisObjectPositionsTop+'px'})
            }
            
        }

    if(thisObjectOptionsFunctionType == "manuel"){
        HGTooltipOperation(thisObject)

        $(document).mouseup(function (e){
             var container = thisObject; 
             if (!container.is(e.target)){ 
                $('.hg-tooltip').remove()
            } 
        });
    }
    else if(thisObjectOptionsFunctionType == "mouseover"){
        thisObject.on('mouseover',function () {
            HGTooltipOperation()
            thisObject.mouseout(function() {
                toolTipObject.remove()
            })
        });
    }
    else if(thisObjectOptionsFunctionType == "click"){
        thisObject.on('click',function(){
            $('.hg-tooltip').remove()
            HGTooltipOperation()
        });
        $(document).mouseup(function (e){
             var container = thisObject; 
             if (!container.is(e.target)){ 
                $('.hg-tooltip').remove()
            } 
        });
    }
    else if(thisObjectOptionsFunctionType == "dblclick"){
        thisObject.on('dblclick',function(){
            $('.hg-tooltip').remove()
            HGTooltipOperation()
        });
        $(document).mouseup(function (e){
             var container = thisObject; 
             if (!container.is(e.target)){ 
                $('.hg-tooltip').remove()
            } 
        });
    }
}
// HG ToolTip \\
});