import Cookies from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const cookies = new Cookies(null, { path: "/" });
const button = document.getElementById("button1");
const imageinput = document.getElementById("session_img_input");
const image = document.getElementById("session_img");

let editor;
window.onload = function () {
  const Header = window.Header;
  const List = window.List;
  editor = new EditorJS({
    tools: {
      header: {
        class: Header,
        shortcut: "CMD+SHIFT+H",
      },
      list: {
        class: List,
        inlineToolbar: true,
        config: {
          defaultStyle: "unordered",
        },
      },
    },
    holder: "editorjs",
  });
};

imageinput.addEventListener("change", async function (e) {
  if (e.target.files[0]) {
    const formData = new FormData();
    formData.append("img", e.target.files[0]);

    formData.append("profileid", e.target.files[0]);

    const csrfToken = cookies.get("csrftoken");
    const headers = {
      "X-CSRFToken": csrfToken,
    };

    if (document.querySelector("html").getAttribute("data_session_id")) {
      update_session_img(headers, e.target.files[0]);
    } else {
      creat_session_with_img(headers, formData);
    }
  }
});

async function creat_session_with_img(headers, formData) {
  await fetch("http://127.0.0.1:8000/addimg", {
    method: "post",
    body: formData,
    headers,
  }).then(async (v) => {
    imageinput.value = null;
    const responce = await v.json();
    image.setAttribute("src", "http://127.0.0.1:8000/" + responce.url);
    document
      .querySelector("html")
      .setAttribute("data_session_id", responce.session_id);
  });
}

async function update_session_img(headers, file) {
  const formData = new FormData();
  formData.append("img", file);
  formData.append(
    "session_id",
    document.querySelector("html").getAttribute("data_session_id")
  );
  await fetch("http://127.0.0.1:8000/updateimg", {
    method: "post",
    body: formData,
    headers,
  }).then(async (v) => {
    imageinput.value = null;
    const responce = await v.json();
    image.setAttribute("src", "http://127.0.0.1:8000/" + responce.url);
    document
      .querySelector("html")
      .setAttribute("data_session_id", responce.session_id);
  });
}
const positive_numbers =(e) => {
  const excludedKeys = ['e', 'E', '-', '+'];

  if (excludedKeys.includes(e.key)) {
      e.preventDefault();
      return;
  }}
    document.getElementById('price_input').addEventListener('keydown', positive_numbers )
    document.getElementById('participent_input').addEventListener('keydown', positive_numbers )


button.addEventListener("click", async function (e) {
  const title = document.getElementById("title_input").value;
  const price = Number( document.getElementById("price_input").value);
  const location = document.querySelector(
    'p[data-dropDown-item = "location_dropdown"][data-item-active]'
  );
  const max_participent = Number( document.getElementById("participent_input").value);
  const description = await editor.save().then((v) => v);
  const start_time = document.getElementById("time").value;
  const end_time = document.getElementById("time2").value;
  const categorie = document.querySelector(
    'p[data-dropDown-item = "categorie_dropdown"][data-item-active]'
  );
  const categorie_2nd = document.querySelector(
    'p[data-dropDown-item = "categorie_dropdown2"][data-item-active]'
  );
  const selected_day = document
    .querySelector("html")
    .getAttribute("selected_day");
  console.log({ imageinput: imageinput.files[0] });
 
  if (
    title &&
    description &&
    end_time &&
    start_time &&
    categorie &&
    categorie_2nd &&
    selected_day &&
    price &&
    location &&
    max_participent 
  ) {
    const sessionId = document
      .querySelector("html")
      .getAttribute("data_session_id");
    if (!sessionId) {
      return;
    }
    const body = {
      sessionId: sessionId,
      title,
      description,
      categorie: categorie.textContent,
      categorie_2nd: categorie_2nd.textContent,
      start_time,
      selected_day: JSON.parse(selected_day),
      end_time,
      location:location.textContent,
      max_participent,
      price,
    };

    const csrfToken = cookies.get("csrftoken");
    const headers = {
      "X-CSRFToken": csrfToken,
    };
    console.log(JSON.stringify(body));
    await fetch("http://127.0.0.1:8000/update_session", {
      method: "POST",
      body: JSON.stringify(body),
      headers,
    }).then(async (v) => {
      const data = await v.json();
      console.log(data);
    });
  }
});
