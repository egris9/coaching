import micromodal from "https://cdn.jsdelivr.net/npm/micromodal@0.4.10/+esm";
import Cookies from 'https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm'


const successToast = (text) =>
	Toastify({
		text,
		avatar:
			"https://api.iconify.design/material-symbols:done.svg?color=%234ade80",

		className:
			"bg-gradient-to-l from-neutral-800 to-neutral-800 text-sm w-full px-4 py-4 border-2 border-green-700 rounded-md max-w-fit capitalize flex items-center justify-between text-body text-neutral-300",
		close: true,
		gravity: "top", // `top` or `bottom`
		position: "right", // `left`, `center` or `right`
		stopOnFocus: true, // Prevents dismissing of toast on hover
	}).showToast();

const q = (id) => document.getElementById(id);
const review_btn=q('review_btn')
const cookies = new Cookies (null, { path: "/" });

micromodal.init();
const edjsParser = edjsHTML();

const button = document.querySelectorAll(".modal_button");



function render_review_list(res){
  let list=''
  const review_page =document.querySelector('.reviews_list')
  review_page.innerHTML = list;    // Optionally, reset the form 
  if (res.reviews.length<1) {
    return
    
  }
  res.reviews.forEach(el=>{
    let starsIcons = ""
    for(let i =0; i <  el.stars; i++) {
      starsIcons = starsIcons + ' <i class="fa-solid inline fa-star"></i> '
    }
    list=list+`<div class="flex flex-col">
    <!-- Icon -->
    <div class="flex items-center gap-x-2">
    <img class="flex-shrink-0 size-[46px] self-start rounded-full object-cover" src="${el.url}">
    <div class="">
    <p class="self-start font-medium text-lg block text-gray-500">${el.full_name}</p>
    <div class="space-x-1">
    ${starsIcons} 
    </div>
    </div>
    </div>
    <div class="">
    <h3 class="text-base sm:text-lg font-semibold text-gray-800 mt-2">
    ${el.title}
    </h3>
    <p class="mt-1 text-gray-600 ">
    ${el.comment}              </p>
    </div>
    </div>` 
    
  }) 
  
  review_page.innerHTML = list;    // Optionally, reset the form 
  }



function set_rating(res) {
  const reviews_count=q('reviews_count')
  const reviews_average=q('stars_average')
  const reviews_average_icon=q('stars_average_icon')
  
  reviews_count.textContent=res.reviews_count+' reviews'
  reviews_average.textContent=String(res.stars_average.toFixed(1))
  const star_element= '<i class="fa-solid fa-star text-2xl"></i>'
  const half_star_element='<i class="fa-solid fa-star-half-stroke text-2xl"></i>'
  let rating=''

  for (let index = 1; index <= 5; index++) {
    if (index <= res.stars_average) {
      rating= rating+star_element
    }
    if (index === 5 && res.stars_average < 5 && Number.isInteger(res.stars_average) === false) 
      {
        rating= rating+half_star_element
      }
  }
  reviews_average_icon.innerHTML=rating
}
button.forEach((btn) => {
  btn.addEventListener("click", async function (e) {
    const sessionId=btn.getAttribute('data-id');
    review_btn.setAttribute( "data-id", sessionId )
    const csrfToken = cookies.get("csrftoken");
    const headers = {
      "X-CSRFToken": csrfToken,
    };

    await fetch("http://127.0.0.1:8000/comments/"+sessionId,{
      method: 'get',headers
     }).then(async(v)=>{
    const res=await v.json()
    render_review_list(res)
    set_rating(res)
  })
    
    
    
   await fetch("add_to_cart_popup/"+sessionId,{
    method: 'get',headers
   }).then(async(v)=>{
    const res=await v.json()

    const location=q('location')
    location.textContent=res.location

    const title=q('modal-1-title')
    title.textContent=res.name

    const price=q('price')
    price.textContent=res.price

    const participent=q('participent')
    participent.textContent=res.participent

    const time=q('time')
    time.textContent=`${res.start_time} - ${res.end_time}`

    const date=q('date')
    date.textContent=`${res.first_date} - ${res.last_date}`

    const coach=q('coach')
    coach.textContent=res.coach

    const type=q('type')
    type.textContent=res.type

    const categorie=q('categorie')
    categorie.textContent=res.categorie

   const img=q('img_mod')
   const card_img=document.querySelector(`img[data-session-id='${sessionId}']`)
   img.setAttribute('src',card_img.getAttribute('src'))
    const description=q('mod_description')
    
    let html = edjsParser.parse(res.description);    
    html=html.reduce((sum, el) => {
      return sum + el
    }, '')
    description.innerHTML=html
  micromodal.show("modal-1"); // [1]
   })
  });
});


review_btn.addEventListener('click',async(v)=>{
  const stars= document.querySelector('.star:checked').value
  const title= q('title_review').value
  const description= q('review_cmnt').value

  if (!stars) {
    alert('Please select a star rating.');
    return
  }

  const sessionId=review_btn.getAttribute("data-id");
  const csrfToken = cookies.get("csrftoken");
  const headers = {
    'Content-Type': 'application/json',
    "X-CSRFToken": csrfToken,


  };

  await fetch("reviews/"+sessionId+ "/" ,{
    method: 'post',
    headers: headers,
    body: JSON.stringify({stars,title,description})
   }).then(async v=>{
    const res= await v.json()
    let starsIcons = ""
    const url= res.img 
    const full_name= res.full_name
  for(let i =0; i <  stars; i++) {
     starsIcons = starsIcons + ' <i class="fa-solid inline fa-star"></i> '
}
   const review=`<div class="flex flex-col">
                  <!-- Icon -->
                   <div class="flex items-center gap-x-2">
                    <img class="flex-shrink-0 size-[46px] self-start rounded-full object-cover" src="${url}">
                    <div class="">
                    <p class="self-start font-medium text-lg block text-gray-500">${full_name} </p>
                    <div class="space-x-1">
                    ${starsIcons} 
                   </div>
                    </div>
                   </div>
                  <div class="">
                    <h3 class="text-base sm:text-lg font-semibold text-gray-800 mt-2">
                    ${title}
                    </h3>
                    <p class="mt-1 text-gray-600 ">
                     ${description}  </p>
                  </div>
                </div>` 
    const review_page =document.querySelector('.reviews_list')
    review_page.insertAdjacentHTML('afterbegin', review);    // Optionally, reset the form
   })
   
    document.getElementById('title_review').value = '';
    document.getElementById('review_cmnt').value = '';
    const checkedStar = document.querySelector('.star:checked');
    if (checkedStar) {
      checkedStar.checked = false;
    }
    successToast('review submitted')
  });

