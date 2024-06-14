import universalCookie from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";
import Fuse from 'https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.mjs'

const cookies = new universalCookie(null, { path: "/" });

let products_list = []

window.onload=function(){
    async function fetchProducts() {
        const csrfToken = cookies.get("csrftoken");
        const headers = {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
    };
        const response = await fetch('/products_list',{
            method:"Get",
            headers
        });
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const products = await response.json();
        return products;
    }

    fetchProducts()
        .then(products => {products_list = products})
        .catch(error => console.error('There was a problem with the fetch operation:', error));

}


document.getElementById('searchButton').addEventListener('click', function() {
    
    const query = document.getElementById('searchInput').value;
    if (query) {
      alert('Searching for: ' + query);
      const fuse = new Fuse(products_list, {
        keys: ['name']
      })
      
      // 3. Now search!
      //fuse.search(query)
      console.log(fuse.search(query))
    } else {
      alert('Please enter a search term.');
    }
  });