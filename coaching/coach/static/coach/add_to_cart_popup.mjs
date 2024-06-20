import micromodal from "https://cdn.jsdelivr.net/npm/micromodal@0.4.10/+esm";
import Cookies from 'https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm'

const q = (id) => document.getElementById(id);

const cookies = new Cookies (null, { path: "/" });

micromodal.init();
const edjsParser = edjsHTML();

const button = document.querySelectorAll(".modal_button");
let toggle_modal = false;
button.forEach((btn) => {
  btn.addEventListener("click", async function (e) {
   
     
     
    
    const sessionId=btn.getAttribute('data-id');
    const csrfToken = cookies.get("csrftoken");
    const headers = {
      "X-CSRFToken": csrfToken,
    };
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

const review_btn=q('review_btn')
review_btn.addEventListener('click',async(v)=>{
  const stars= document.querySelector('.star:checked')
  const title= q('title_review').value
  const description= q('review_cmnt').value
})