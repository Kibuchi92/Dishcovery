document.addEventListener("DOMContentLoaded", () => {
    console.log("scripts loaded");

    // attach ingredients form listener
    const form = document.getElementById("ingredients-form");
    if (form) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            document.getElementById("response").innerText =
                "Kick back and enjoy the jams 🎶, Your recipes are on the way ...";

            const prompt = document.getElementById("prompt").value;
            const res = await fetch("/prompt", {
                method: "POST",
                headers: { "Content-Type": "application/x-www-form-urlencoded" },
                body: new URLSearchParams({ prompt })
            });
            const data = await res;
            data = data.recipes;
            
            document.getElementById("response").innerText = data.response || data.error;
        });
    }
});

