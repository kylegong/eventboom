window.Boom = window.Boom || {}

window.Boom.EventView = Backbone.View.extend({
  className: 'event',
  template: _.template($('#event').html()),
  render: function() {
    this.$el.html(
      this.template(this.model.toJSON())
    );
    return this;
  }
});
