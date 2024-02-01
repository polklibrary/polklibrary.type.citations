
var CitationsEdit = {
    
    selected : '',
    data : [],
    
    construct : function(){
        console.log('CitationsEdit');
        this.controller();
        this.load();
        this.selected_handler();
        this.add_handler();
        this.validator();
    },

    add_handler : function() {
        var self = this;
        $('#form-buttons-addsection').click(function(){
            self.add_field(self.selected,'',false, false);
            self.selected = '';
        });
    },
    
    add_field : function(snippet, message, is_wrong, is_italic) {
        $('#citation-template input[name="cite.target"]').val(snippet);
        $('#citation-template input[name="cite.message"]').val(message);
        $('#citation-template input[name="cite.is_error"]').prop('checked', is_wrong);
        $('#citation-template input[name="cite.is_italic"]').prop('checked', is_italic);
        var html = $('#citation-template .dynamic-field').clone(true);
        $('#citation-template-section').append(html);
    }, 
    
    controller : function() {
        var self = this;
        $('input[name="cite.target"], input[name="cite.message"]').on('keyup', function(){
            self.update();
        });
        $('input[name="cite.is_error"], input[name="cite.is_italic"]').on('click', function(){
            self.update();
        });
    }, 
    
    update : function() {
        var self = this;
        self.data = [];
        $('#citation-template-section .dynamic-field').each(function(i,t){
            self.data.push({
                'target': $(t).find('input[name="cite.target"]').val(),
                'message': $(t).find('input[name="cite.message"]').val(),
                'is_error': $(t).find('input[name="cite.is_error"]').is(':checked'),
                'is_italic': $(t).find('input[name="cite.is_italic"]').is(':checked'),
            });
        });
    
        $('#form-widgets-json_data').val(JSON.stringify(this.data));
    },
    
    load : function() {
        var data = $('#form-widgets-json_data').val();
        if (data != '') {
            this.data = $.parseJSON(data);
            for (var i in this.data){
                var o = this.data[i];
                this.add_field(o.target, o.message, o.is_error);
            }
        }
    },
    
    selected_handler : function() {
        var self = this;
        $('#form-widgets-title').select(function(e) {
            var start = e.target.selectionStart;
            var end = e.target.selectionEnd;
            self.selected = $(e.target).val().substring(start,end);
        });
    },
    
    validator : function() {
        var self = this;
        setInterval(function(){
            var o = $('#form-widgets-title').val();
            $('.dynamic-field input[name="cite.target"]').each(function(){
                if (o.indexOf($(this).val()) == -1)
                    $(this).addClass('citation-error');
                else
                    $(this).removeClass('citation-error');
            });
        }, 500);
        
        
        $('.dynamic-field input[name="cite.target"]').select(function(e) {
            var start = e.target.selectionStart;
            var end = e.target.selectionEnd;
            self.selected = $(e.target).val().substring(start,end);
        });
    },
    
}



$(document).ready(function(){
    CitationsEdit.construct();    
});