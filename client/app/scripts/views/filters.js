window.Boom = window.Boom || {}

window.Boom.FiltersView = Backbone.View.extend({
  template: _.template($('#filters').html()),
  render: function() {
    var $category,
        $neighborhoods;
    this.$el.html(this.template());
    $category = this.$('#category');
    _.each(Boom.Data.tags, function(tag) {
      $category.append($('<option value="' + tag + '">' + tag + '</option>'));
    });
    $neighborhoods = this.$('#neighborhood');
    _.each(Boom.Data.neighborhoods, function(neighborhood) {
      $neighborhoods.append($('<option value="' + neighborhood + '">' + neighborhood + '</option>'));
    });
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
