window.Boom = window.Boom || {}

window.Boom.EventModel = Backbone.Model.extend({});

window.Boom.EventCollection = Backbone.Collection.extend({
  comparator: function(event) {
    return event.get('date');
  },
  sortAndFilter: function(when) {
    var filtered,
        self = this;
    this.data = this.data || this.toJSON();
    if(when) {
      when = parseInt(when, 10);
      filtered = _.filter(this.data, function(event) {
        return self.isInTheNextXDays(when, event.date);
      });
      this.reset(filtered);
    } else {
      this.reset(this.data);
    }
  },
  isInTheNextXDays: function(days, date) {
    var today = new Date(),
        limit = new Date();
    limit.setDate(today.getDate() + days);
    return date <= limit;
  }
});
