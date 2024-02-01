


var Citations = {
    
    citation : '',
    data : [],
    found_errors : 0,
    total_errors : 0,
    
    construct : function(){
        console.log('Citations');
        this.load();
        this.attach();
        this.pattern();
        this.finished();
    },

    finished : function() {
        var self = this;
        $('#finished').click(function(){
            if (self.found_errors >= self.total_errors)
                $('#citation-results-perfect').show();
            else {
                $('#citation-results-okay .error-found').html(self.found_errors);
                $('#citation-results-okay .error-total').html(self.total_errors);
                $('#citation-results-okay').show();
            }
            $('#finished').hide();
            $('#next-citation').css('display','inline-block');
            
        });
    
    },
    
    pattern : function() {
        var self = this;
        $('.pat-citation').on({
            'click' : function() {
                $(this).addClass('active');
                $('#citation-help').html($(this).data('message')).show();
                if ($(this).data('wrong') && !$(this).data('found')) {
                    self.found_errors++;
                    $(this).data('found', true).attr('data-found', true);
                    $('#finished').val('I found ' + self.found_errors + ' mistakes.')
                    if (self.found_errors == 1)
                        $('#finished').val('I found ' + self.found_errors + ' mistake.')
                }
            },
            'mouseout' : function() {
                $(this).removeClass('active');
                $('#citation-help').html('').hide();
            }
        });
    },
    
    attach : function(){
        for (var i in this.data){
            var o = this.data[i];
            var s = $('<span>').addClass('pat-citation').html(o.target)
                .attr('data-wrong', o.is_error)
                .attr('data-found', false)
                .attr('data-is_italic', o.is_italic)
                .attr('data-message', o.message);
            this.citation = this.citation.replace(o.target, $(s).prop('outerHTML'));
            if (o.is_error)
                this.total_errors++;
        }
        $('#citation-test').html(this.citation);
    },
    
    
    
    
    load : function() {
        this.citation = $('#citation-string').val();
        var data = $('#citation-data').val();
        if (data != '') 
            this.data = $.parseJSON(data);
    },
    
    
}



$(document).ready(function(){
    Citations.construct();    
});