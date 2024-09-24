let deleteButtons = document.querySelectorAll('.deleteBtn');

deleteButtons.foreach(button => {
    button.addEventListener('click', function(e){
        e.preventDefault();

        let product = this.dataset.name;
        let productID = this.dataset.id;

        let response = confirm("Do you want to delete the product " + product + "?");

        if (response){
            fetch('../utils/deleteProduct.php?id=' + productID, {
                method: 'GET'
            })
            .then(response => response.text())
            .then(data => {
                if(data === 'success'){
                    window.location.href = '../views/product.php';
                }
            })
        }
    });
});