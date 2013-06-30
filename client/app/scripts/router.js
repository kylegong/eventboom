window.Boom = window.Boom || {}

window.Boom.Router = Backbone.Router.extend({
  routes: {
    '': 'index',
    'create': 'create',
    'event/:id': 'show'
  },
  initialize: function() {
    if (!Boom.useMock) {
      this.events = new Boom.EventCollection();
      this.events.fetch({reset: true});
    }
    this.timeout = 1000;
  },
  index: function() {
    var self = this,
        collection;
    if (Boom.useMock) {
      collection = new Boom.EventCollection(window.Boom.Data)
    } else {
      collection = self.events
    }
    window.setTimeout(function() {
      var view = new window.Boom.IndexView({
        collection: collection
      });
      view.$el.fadeOut(300, function() {
        view.render();
        view.$el.fadeIn();
      });
      self.timeout = 0;
    }, this.timeout)
  },
  create: function() {
    var view = new window.Boom.EventCreateView();
    view.$el.fadeOut(300, function() {
      view.render();
      view.$el.fadeIn();
    });
  },
  show: function(id) {
    var model,
        view;
    if (Boom.useMock) {
      model = new Boom.EventModel(Boom.Data.get(parseInt(id, 10)))
    } else {
      model = this.events.get(id)
    }
    view = new Boom.EventView({
      model: model
    });
    view.$el.fadeOut(300, function() {
      view.render();
      view.$el.fadeIn();
    });
  }
})
