window.Boom = window.Boom || {}

window.Boom.Router = Backbone.Router.extend({
  routes: {
    '': 'index',
    'create': 'create',
    'event/:id': 'show'
  },
  index: function() {
    new window.Boom.IndexView({
      collection: new Boom.EventCollection(window.Boom.Data)
    }).render();
  },
  create: function() {
    new window.Boom.EventCreateView().render();
  },
  show: function(id) {
    new Boom.EventView({
      model: new Boom.EventModel(Boom.Data.get(parseInt(id, 10)))
    }).render();
  }
})
