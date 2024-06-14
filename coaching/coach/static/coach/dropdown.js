
const dropDownBtn = document.querySelectorAll("[data-dropDown-btn]");

function toggleDropDown(dropDownId) {
  const dropDown = document.querySelector(
    `[data-dropDown-list="${dropDownId}"]`
  );
  const ishidden = dropDown.getAttribute("data-hidden")

  if(ishidden==="false"){


    anime({
      targets: dropDown,
      opacity: 1,
      duration:300,
      easing:'linear',
      direction:'normal',
      complete: function(anim) {
        dropDown.classList.remove("pointer-events-none")
      }
    
    });
    dropDown.setAttribute('data-hidden',true)

  } else{

    anime({
      targets: dropDown,
      opacity: 0,
      duration:300,
      easing:'linear',
      direction:'normal',

      complete: function(anim) {
        
        dropDown.classList.add("pointer-events-none")
        
      }
  
    });
    dropDown.setAttribute('data-hidden',false)
  }
}

function handleMouseleave(dropDownId){

  toggleDropDown(dropDownId)


}

const dropDownLists = document.querySelectorAll(`[data-dropDown-list]`);

dropDownLists.forEach((element) => {
  const dropDownId = element.getAttribute("data-dropDown-list");
  const dropDownItems = document.querySelectorAll(
    `[data-dropDown-item="${dropDownId}"]`
  );

  dropDownItems.forEach((el) => {
    el.addEventListener("click", (E) => select(E, dropDownId));
  });
 // element.addEventListener('mouseleave',() => handleMouseleave(dropDownId))
});

dropDownBtn.forEach((el) => {
  el.addEventListener("click", (e) => {
    const dropDownId = e.target.getAttribute("data-dropDown-btn");

    toggleDropDown(dropDownId);
  });
});

function select(e, id) {
  const dropDownItem = e.target;
   dropDownItems = document.querySelectorAll(
    `[data-dropDown-item="${id}"]`
  );
  dropDownItems.forEach((el) => el.removeAttribute("data-item-active"));
  dropDownItem.setAttribute("data-item-active", true);
  toggleDropDown(id);

}

