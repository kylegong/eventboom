window.Boom = window.Boom || {}

window.Boom.Data = [
  {
    id: 1,
    title: 'My event',
    description: "Hi Everyone, <br><br> I’m looking to put together a dinner for 6 at my house in Potrero. Aenean vel tellus mattis, mollis tortor sit amet, interdum tellus. Suspendisse sollicitudin, orci vitae condimentum adipiscing. Maecenas vitae hendrerit arcu, sit amet cursus nulla. Nam faucibus lorem quis risus bibendum, eu placerat arcu bibendum. Sed ornare cursus tellus ac blandit. Praesent malesuada eleifend turpis a laoreet. Proin non leo ultrices lacus sagittis consectetur non non sapien. Nunc ut porttitor ipsum, id auctor augue. Aliquam erat volutpat.",
    datetime: new Date(2013, 5, 30),
    tags: ['sports'],
    location: 'Lolinda',
    neighborhood: 'soma'
  },
  {
    id: 2,
    title: 'Other event',
    description: 'No way!!!',
    datetime: new Date(2013, 5, 29),
    tags: ['food', 'fun'],
    location: 'Sushi place',
    neighborhood: 'soma'
  },
  {
    id: 3,
    title: 'I\'m not going',
    description: 'No way!!!',
    datetime: new Date(2013, 6, 3),
    tags: ['speed dating'],
    location: 'Ice cream place',
    neighborhood: 'mission'
  }
]

window.Boom.Data.get = function(id) {
  return _.find(window.Boom.Data, function(event){
    return event.id === id;
  });
}
