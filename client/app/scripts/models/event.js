window.Boom = window.Boom || {}

window.Boom.EventModel = Backbone.Model.extend({});

window.Boom.EventCollection = Backbone.Collection.extend({
  comparator: function(event) {
    return event.get('date');
  },
  sortAndFilter: function(when, category) {
    var filtered,
        self = this;
    this.data = this.data || this.toJSON();

    if (when && category) {
      when = parseInt(when, 10);
      filtered = _.filter(this.data, function(event) {
        return self.isInTheNextXDaysWithCategory(when, category, event);
      });
      this.reset(filtered);
    } else if(when) {
      when = parseInt(when, 10);
      filtered = _.filter(this.data, function(event) {
        return self.isInTheNextXDays(when, event);
      });
      this.reset(filtered);
    } else if(category) {
      filtered = _.filter(this.data, function(event) {
        return self.isMatchingCategory(category, event)
      })
      this.reset(filtered);
    } else {
      this.reset(this.data);
    }
  },
  isInTheNextXDays: function(days, event) {
    var today = new Date(),
        limit = new Date();
    limit.setDate(today.getDate() + days);
    return event.date <= limit;
  },
  isInTheNextXDaysWithCategory: function(days, category, event) {
    var today = new Date(),
        limit = new Date();
    limit.setDate(today.getDate() + days);
    return event.date <= limit && _.indexOf(event.tags, category) !== -1;
  },
  isMatchingCategory: function(category, event) {
    return _.indexOf(event.tags, category) !== -1;
  }
});
