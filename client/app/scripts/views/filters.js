window.Boom = window.Boom || {}

window.Boom.FiltersView = Backbone.View.extend({
  template: _.template($('#filters').html()),
  render: function() {
    this.$el.html(this.template());
    return this;
  },
  events: {
    'change select': 'filter'
  },
  filter: function() {
    var when      = this.$('#when').val(),
        category  = this.$('#category').val(),
        neighborhood = this.$('#neighborhood').val();
    this.collection.sortAndFilter(when, category, neighborhood);
  }
});
