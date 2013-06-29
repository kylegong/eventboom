window.Boom = window.Boom || {}

window.Boom.EventShortView = Backbone.View.extend({
  className: 'event',
  tagName: 'li',
  template: _.template($('#event-short').html()),
  render: function() {
    this.$el.html(
      this.template(this.model.toJSON())
    );
    return this;
  }
});
