window.Boom = window.Boom || {}

window.Boom.Router = Backbone.Router.extend({
  routes: {
    '': 'index',
    'create': 'create',
    'event/:id': 'show'
  },
  initialize: function() {
    this.events = new Boom.EventCollection();
    // this.events.fetch({reset: true});
  },
  index: function() {
    new window.Boom.IndexView({
      collection: new Boom.EventCollection(window.Boom.Data)
      // collection: this.events
    }).render();
  },
  create: function() {
    new window.Boom.EventCreateView().render();
  },
  show: function(id) {
    new Boom.EventView({
      model: new Boom.EventModel(Boom.Data.get(parseInt(id, 10)))
      // model: this.events.get(id)
    }).render();
  }
})
