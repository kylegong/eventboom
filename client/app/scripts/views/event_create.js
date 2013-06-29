window.Boom = window.Boom || {}

window.Boom.EventCreateView = Backbone.View.extend({
  el: '#main',
  events: {
    'click .post-event': 'postEvent'
  },
  render: function() {
    var template = $('#event-create');
    $(this.el).html(template.html());
  },
  postEvent: function(e) {
    e.preventDefault();
    var form = $('#event-create-form')
    var data = {
      'title':        form.find('.title').val(),
      'description':  form.find('.description').val(),
      'time':         form.find('.time').val(),
      'location':     form.find('.location').val()
    }
    var event = new Boom.EventModel(data);
    window.Boom.Data.push(event.toJSON());
    window.router.navigate('/', { trigger: true })
  }
});
