window.Boom = window.Boom || {}

window.Boom.EventShortView = Backbone.View.extend({
  className: 'event',
  template: _.template($('#event-short').html()),
  render: function() {
    this.$el.html(
      this.template(this.model.toJSON())
    );
    return this;
  }
});
