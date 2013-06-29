window.Boom = window.Boom || {}

window.Boom.IndexView = Backbone.View.extend({
  el: '#main',
  template: _.template($('#index').html()),
  render: function() {
    this.$el.html(this.template());
    this.$('.event-list').append(
      new Boom.EventListView({collection: this.collection}).render().el
    );
    this.$('.filters').append(
      new Boom.FiltersView({collection: this.collection}).render().el
    );
    return this;
  }
});
