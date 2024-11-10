let products = JSON.parse(localStorage.getItem('products')) || [];

function updateLocalStorage() {
    localStorage.setItem('products', JSON.stringify(products));
}

function renderProducts() {
    const productList = document.getElementById('productList');
    productList.innerHTML = '';
    products.forEach((product, index) => {
        const li = document.createElement('li');
        li.className = 'stock-item';
        li.innerHTML = `
            ${product.name} - Cantidad: ${product.quantity}
            <span>
                <button onclick="increaseQuantity(${index})">+</button>
                <button onclick="decreaseQuantity(${index})">-</button>
                <button onclick="deleteProduct(${index})">Eliminar</button>
            </span>
        `;
        productList.appendChild(li);
    });
}

function addProduct() {
    const name = document.getElementById('productName').value;
    const quantity = parseInt(document.getElementById('productQuantity').value);
    if (name && quantity) {
        products.push({ name, quantity });
        updateLocalStorage();
        renderProducts();
    }
}

function deleteProduct(index) {
    products.splice(index, 1);
    updateLocalStorage();
    renderProducts();
}

function increaseQuantity(index) {
    products[index].quantity++;
    updateLocalStorage();
    renderProducts();
}

function decreaseQuantity(index) {
    if (products[index].quantity > 0) {
        products[index].quantity--;
    }
    updateLocalStorage();
    renderProducts();
}

// Inicialización
renderProducts();
