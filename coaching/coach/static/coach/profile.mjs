import micromodal from "https://cdn.jsdelivr.net/npm/micromodal@0.4.10/+esm";
import Cookies from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const q = (id) => document.getElementById(id);
const edit_profil_btn = q("edit_profil_btn");
const cookies = new Cookies(null, { path: "/" });
const edit_profile_form_btn = q("edit_profile_form_btn");

micromodal.init();

edit_profil_btn.addEventListener("click",()=>{
    micromodal.show("modal-1");

})

