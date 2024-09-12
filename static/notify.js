document.getElementById('scheduleForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Impede o envio imediato do formulário

    // vai captura os valores selecionados
    const name = document.getElementById('name').value;
    const date = document.getElementById('date').value;
    const selectedServices = Array.from(document.querySelectorAll('input[name="service"]:checked'));

    if (selectedServices.length === 0) {
        showNotification('Por favor, selecione pelo menos um serviço.', true);
        return;
    }

    // responsavel por construir a mensagem de notificação com os serviços selecionados
    let serviceDetails = selectedServices.map(service => service.value).join(', ');
    let message = `Você está agendando: ${serviceDetails} na data ${date}.`;

    //
    showNotification(message);

    // Envia o formulário após mostrar a notificação
    setTimeout(() => {
        document.getElementById('scheduleForm').submit();
    }, 2000); // delay de 2sec
});

// Função para exibir a notificação
function showNotification(message, isError = false) {
    const notification = document.getElementById('notification');
    const notificationMessage = document.getElementById('notificationMessage');
    notificationMessage.textContent = message;
    notification.classList.add(isError ? 'error' : '');
    notification.style.display = 'block';
}

// Função para fechar a notificação
function closeNotification() {
    const notification = document.getElementById('notification');
    notification.style.display = 'none';
}
