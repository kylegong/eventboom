window.Boom = window.Boom || {}

window.Boom.Router = Backbone.Router.extend({
  routes: {
    '': 'index',
    'create': 'create',
    'event/:id': 'show'
  },
  index: function() {
    new window.Boom.EventListView({
      collection: new Boom.EventCollection(window.Boom.Data)
    }).render();
  },
  create: function() {
    $('body').text('create event')
  },
  show: function(id) {
    $('body').text('show: ' + id)
  }
})
