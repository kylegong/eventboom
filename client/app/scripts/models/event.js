window.Boom = window.Boom || {}

window.Boom.EventModel = Backbone.Model.extend({
  defaults: {
    image: '/images/unknown.jpg',
    creator_name: ''
  },
  initialize: function() {
    if (typeof this.get('datetime') === 'string') {
      this.set('datetime', new Date(this.get('datetime')));
    }
    this.set('formattedDate', moment(this.get('datetime')).format('ddd, MMM Do HH:mm A'));
  }
});

window.Boom.EventCollection = Backbone.Collection.extend({
  initialize: function() {
    if (!Boom.useMock) {
      this.url = Boom.url + 'api/v1/events/'
    }
  },
  model: Boom.EventModel,
  comparator: function(event) {
    return event.get('datetime');
  },
  sortAndFilter: function(when, category, neighborhood) {
    var filtered,
        self = this,
        toRemove = [];
    this.data = this.data || this.toJSON();

    when = when && parseInt(when, 10);

    filtered = _.filter(this.data, function(event) {
      var result = true;
      if (typeof when === 'number') {
        result = self.isInTheNextXDays(when, event) && result;
      }
      if (result && category) {
        result = _.indexOf(event.tags, category) > -1 && result;
      }
      if (result && neighborhood) {
        result = event.neighborhood == neighborhood && result;
      }
      return result;
    });

    _.each(this.data, function(event) {
      toRemove.push(event.id);
    });

    _.each(filtered, function(event) {
      toRemove = _.without(toRemove, event.id);
      if (!self.get(event.id)) {
        console.log('adding ' + event.id)
        self.add(event);
      }
    });

    _.each(toRemove, function(id) {
      var model = self.get(id);
      if (model) {
        console.log('removing ' + id)
        self.remove(model);
      }
    });
  },
  isInTheNextXDays: function(days, event) {
    var today = new Date(),
        limit = new Date();
    limit.setDate(today.getDate() + days);
    return event.datetime <= limit;
  }
});
