window.Boom = window.Boom || {}

window.Boom.EventModel = Backbone.Model.extend({
  initialize: function() {
    if (typeof this.get('datetime') === 'string') {
      this.set('datetime', new Date(event.get('datetime')));
    }
    this.set('formattedDate', moment(this.get('datetime')).format('ddd - MMM Do HH:mm A'));
  }
});

window.Boom.EventCollection = Backbone.Collection.extend({
  model: Boom.EventModel,
  comparator: function(event) {
    return event.get('datetime');
  },
  sortAndFilter: function(when, category, neighborhood) {
    var filtered,
        self = this;
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

    this.reset(filtered);
  },
  isInTheNextXDays: function(days, event) {
    var today = new Date(),
        limit = new Date();
    limit.setDate(today.getDate() + days);
    return event.datetime <= limit;
  }
});
