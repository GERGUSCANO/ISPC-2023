const ProductosFarmacia = {
    
    
}
fetch('vademecum.json', {
    mode: 'cors',
    credentials: 'include'
  })
    .then(response => response.json())
    .then (data =>console.log(data));