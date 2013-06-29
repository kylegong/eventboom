window.Boom = window.Boom || {}

window.Boom.FiltersView = Backbone.View.extend({
  initialize: function() {
    this.data = this.collection.toJSON();
  },
  template: _.template($('#filters').html()),
  render: function() {
    this.$el.html(this.template());
    return this;
  },
  // events: {
    // 'change select': 'filter'
  // },
  // filter: {
    // var when = this.$('#when').val();
    // switch(when) {
      // case 'today':
        // this.collection.filter(function(event) {
          // return event.date.toString('yyyy-MM-dd') === new Date().toString('yyyy-MM-dd')
        // });
        // break;
      // default:
        // break;
    // }
  // }
});
