window.Boom = window.Boom || {}

window.Boom.Data = [
  {
    id: 1,
    title: 'My event',
    description: 'This is awesome',
    date: new Date(2013, 6, 29),
    tags: ['sports']
  },
  {
    id: 2,
    title: 'Other event',
    description: 'No way!!!',
    date: new Date(2013, 6, 28),
    tags: ['food', 'fun']
  },
  {
    id: 3,
    title: 'I\'m not going',
    description: 'No way!!!',
    date: new Date(2013, 7, 3),
    tags: ['speed dating']
  }
]

window.Boom.Data.get = function(id) {
  return _.find(window.Boom.Data, function(event){
    return event.id === id;
  });
}
