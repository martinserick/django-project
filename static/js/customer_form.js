let customer = document.getElementById("id_customer");
customer.addEventListener('change', function(){
    fetch(`/customer/get_type/?customer_id=${customer.value}`)
            .then(response => response.json())
            .then(data => {
                // Manipule os dados recebidos aqui
                alert(data); // Exemplo: Imprime os dados no console
                document.getElementById('output').innerText = JSON.stringify(data);
            })
            .catch(error => console.error('Erro:', error));
});