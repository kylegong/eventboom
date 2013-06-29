window.Boom = window.Boom || {}

window.Boom.EventCreateView = Backbone.View.extend({
  el: '#main',
  events: {
    'click .post-event': 'postEvent'
  },
  render: function() {
    var template = $('#event-create');
    $(this.el).html(template.html());

    var form = $('#event-create-form');

    // Select today's date by default
    var today = new Date();
    form.find('.month').val(today.getMonth()).attr('selected', true);
    form.find('.day').val(today.getDay()).attr('selected', true);
    form.find('.year').val(today.getFullYear()).attr('selected', true);
  },
  postEvent: function(e) {
    e.preventDefault();
    if ( !this.validateEvent() ) return;

    var form = $('#event-create-form');
    var event_date =  new Date(
                        form.find('.year').val(),
                        form.find('.month').val(),
                        form.find('.day').val()
                      );
    var data = {
      'id':             99999,
      'title':          form.find('.title').val(),
      'date':           event_date,
      'location':       form.find('.location').val(),
      'neighborhood':   form.find('.neighborhood').val(),
      'description':    form.find('.description').val(),
      'category':       form.find('.category').val(),
      'min_attendees':  form.find('.min_attendees').val(),
      'max_attendees':  form.find('.max_attendees').val(),
      'tags':           []
    }
    var event = new Boom.EventModel(data);
    window.Boom.Data.push(event.toJSON());
    window.router.navigate('/', { trigger: true });
  },
  validateEvent: function() {
    var validated_fields = [
      this.validateField('.title'),
      this.validateField('.neighborhood'),
      this.validateField('.description'),
      this.validateField('.category')
    ];
    var all_valid = _.indexOf(validated_fields, false) === -1;
    return all_valid;
  },
  validateField: function(field_class) {
    var valid = true;
    var form = $('#event-create-form');
    var field_value = form.find(field_class).val();
    if (field_value == '' || field_value == 'null') {
      valid = false;
      form.find(field_class).css({'border': "1px solid #c00"})
    } else {
      form.find(field_class).css({'border': "1px solid #ccc"})
    }
    return valid;
  }
});
