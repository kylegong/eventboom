window.Boom = window.Boom || {}

window.Boom.EventListView = Backbone.View.extend({
  tagName: 'ul',
  initialize: function() {
    this.collection.on('reset', this.render, this);
  },
  render: function() {
    var self = this;
    this.$el.empty();
    if (this.collection.length) {
      this.collection.each(function(event) {
        self.$el.append(new Boom.EventShortView({model: event}).render().el);
      });
    } else {
      this.$el.append('<h2>No events yet</h2');
    }
    return this;
  }
});
