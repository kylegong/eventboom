window.Boom = window.Boom || {}

window.Boom.Data = [
  {
    id: 1,
    title: 'My event'
  },
  {
    id: 2,
    title: 'Other event'
  }
]

window.Boom.Data.get = function(id) {
  return _.find(window.Boom.Data, function(event){
    return event.id === id;
  });
}
