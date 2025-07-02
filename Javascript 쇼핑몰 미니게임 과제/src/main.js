// Fetch the items from the Json file
function loadItems(){
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}


loadItems()
    .then(items => {
        console.log(items);
        //displayItems(items);
        //setEventListner(items)
    })
    .catch(console.log)