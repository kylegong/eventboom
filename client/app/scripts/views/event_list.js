window.Boom = window.Boom || {}

window.Boom.EventListView = Backbone.View.extend({
  el: '#main',
  render: function() {
    this.$el.empty().append('<ul></ul>');
    this.collection.each(function(event) {
      var li = $('<li></li>').append(
        new Boom.EventView({model: event}).render().el
      );
      this.$('ul:first').append(li);
    });
    return this;
  }
});
