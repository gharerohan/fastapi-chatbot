async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const userMessage = input.value.trim();

    if (!userMessage) return;

    chatBox.innerHTML += `<div class="user-message"><b>You:</b> ${userMessage}</div>`;
    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: userMessage })
    });

    const data = await response.json();
    chatBox.innerHTML += `<div class="bot-message"><b>Bot:</b> ${data.response}</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;
}
