window.Boom = window.Boom || {}

window.Boom.EventListView = Backbone.View.extend({
  tagName: 'ul',
  initialize: function() {
    this.collection.on('reset', this.render, this);
    this.collection.on('remove', this.remove, this);
    this.collection.on('add', this.add, this);
  },
  render: function() {
    var self = this;
    this.$el.empty();
    if (this.collection.length) {
      this.collection.each(function(event) {
        var subview = new Boom.EventShortView({model: event}).render().$el;
        subview.attr('id', 'event-' + event.id);
        self.$el.append(subview);
      });
    } else {
      this.$el.append('<h2>No events yet</h2');
    }
    return this;
  },
  remove: function(event) {
    var li = this.$('#event-' + event.id);
    li.slideUp(300, function() {
      li.remove();
    });
  },
  add: function(event) {
    var li = new Boom.EventShortView({model: event}).render().$el.hide();
    li.attr('id', 'event-' + event.id);
    this.$el.append(li);
    li.slideDown(300);
  }
});
