import Cookies from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const cookies = new Cookies(null, { path: "/" });
const delet_button = document.querySelectorAll(".delete_session_button")
delet_button.forEach((btn)=>{
    btn.addEventListener("click",()=>{
        const id=btn.getAttribute("data-session-id")
        deleteSession(id);
    });
})
export function deleteSession(sessionId) {
    const csrfToken = cookies.get("csrftoken");

    fetch(`/delete-session/${sessionId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({}),
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById(`session-${sessionId}`).remove();
        } 
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while deleting the session.');
    });
}
