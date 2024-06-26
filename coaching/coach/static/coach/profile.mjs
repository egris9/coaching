import micromodal from "https://cdn.jsdelivr.net/npm/micromodal@0.4.10/+esm";
import Cookies from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const q = (id) => document.getElementById(id);
const edit_profil_btn = q("edit_profil_btn");
const become_coach_btn = q("become_coach_btn");
const cookies = new Cookies(null, { path: "/" });
const edit_profile_form_btn = q("edit_profile_form_btn");

micromodal.init();

edit_profil_btn.addEventListener("click",()=>{
    micromodal.show("modal-1");

})

become_coach_btn.addEventListener("click",()=>{
    console.log('hibitch')
    micromodal.show("modal-2");

})
