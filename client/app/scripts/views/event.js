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
    $('div#event-join-form-div').fadeIn();
  },
  joinEvent: function(e) {
    e.preventDefault();

    var form = $('form#event-join-form');
    if (this.validateJoin()) {
      $('div#event-join-form-div').hide();
      $('div#event-join-success').fadeIn();
    }
  },
  validateJoin: function() {
    var validated_fields = [
      this.validateField('.name'),
      this.validateField('.email'),
      this.validateField('.phone')
    ];
    var all_valid = _.indexOf(validated_fields, false) === -1;
    return all_valid;
  },
  validateField: function(field_class) {
    var valid       = true,
        form        = $('form#event-join-form'),
        field_value = form.find(field_class).val();

    if (field_value == '' || field_value == 'null') {
      valid = false;
      form.find(field_class).addClass("error");
    } else {
      form.find(field_class).removeClass("error");
    }
    return valid;
  }
});
