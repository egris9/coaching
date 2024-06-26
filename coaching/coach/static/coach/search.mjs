import universalCookie from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";
import Fuse from 'https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.mjs'

const cookies = new universalCookie(null, { path: "/" });

let products_list = []

window.onload= async function(){
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

    await fetchProducts()
        .then(  p => {
          products_list = p.products
          console.log(p)
        
        })
        .catch(error => console.error('There was a problem with the fetch operation:', error));

}

const container = document.getElementById("product_container")

document.getElementById('searchButton').addEventListener('click', function() {
    
    const query = document.getElementById('searchInput').value;
    if (query) {
      const fuse = new Fuse(products_list, {
        keys: ['name']
      })
      const result = fuse.search(query)
      console.log(result)
      let content = ""
      result.forEach(element => {
        content=content+`
        <a
          href="http://127.0.0.1:8000/products/${element.item.id}"
          class="w-full max-w-[320px] bg-emerald-900 rounded-[36px] flex flex-col items-center p-3"
        >
          <img
            src="${element.item.url}"
            class="rounded-3xl w-full object-top mb-1 min-h-[300px] object-cover"
          />
          <div class="mt-2 w-full flex items-center justify-center gap-x-4">
            <div class="mb-2">
              <p class="text-emerald-300 font-medium capitalize">${element.item.name}</p>
            </div>
          </div>
          <div class="mb-2 mt-2">
            <p class="text-emerald-300 thick-font text-2xl">${element.item.price} $</p>
          </div>
        </a>
        
        `
      });
      
      container.innerHTML=content

    } else {
      alert('Please enter a search term.');
    }
  });