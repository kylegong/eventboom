window.Boom = window.Boom || {}

window.Boom.EventView = Backbone.View.extend({
  el: '#main',
  className: 'event',
  template: _.template($('#event').html()),
  events: {
    'click .show-form':   'showForm',
    'click .join-event':  'joinEvent'
  },
  render: function() {
    this.$el.html(
      this.template(this.model.toJSON())
    );
    return this;
  },
  showForm: function(e) {
    e.preventDefault();
    $('div#event-join-status').hide();
    $('div#event-join-form-div').show();
  },
  joinEvent: function(e) {
    e.preventDefault();

    var form = $('form#event-join-form');
    if (this.validateJoin()) {
      $('div#event-join-form-div').hide();
      $('div#event-join-success').show();
    }
  },
  validateJoin: function() {
    var form = $('form#event-join-form');
    return true;
  }
});
