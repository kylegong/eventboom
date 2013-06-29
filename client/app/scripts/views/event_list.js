window.Boom = window.Boom || {}

window.Boom.EventListView = Backbone.View.extend({
  tagName: 'ul',
  initialize: function() {
    this.collection.on('reset', this.render, this);
  },
  render: function() {
    var self = this;
    this.$el.empty();
    this.collection.each(function(event) {
      self.$el.append(new Boom.EventShortView({model: event}).render().el);
    });
    return this;
  }
});
