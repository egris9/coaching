import Cookies from "https://cdn.jsdelivr.net/npm/universal-cookie@7.0.1/+esm";

const cookies = new Cookies(null, { path: "/" });
const delete_button = document.querySelectorAll(".delete_session_button");
delete_button.forEach((btn) => {
    btn.addEventListener("click", () => {
        const id = btn.getAttribute("data-order-id");
        deleteSession(id);
    });
});
export function deleteSession(orderId) {
    const csrfToken = cookies.get("csrftoken");

    fetch(`/delete-session-order/${orderId}/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.status === "success") {
                document.getElementById(`order-${orderId}`).remove();
            }
        })
        .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred while deleting the session.");
        });
}