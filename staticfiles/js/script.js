document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById('search-input');

    if (searchInput) {
        searchInput.addEventListener('input', function () {
            let query = this.value;

            if (query.length > 1) {
                fetch(`/search/?q=${query}`)
                    .then(response => response.json())
                    .then(data => {
                        let container = document.getElementById('search-results');
                        container.innerHTML = '';
                        data.forEach(seed => {
                            container.innerHTML += `
                                <div class="col-lg-3 col-md-4 col-sm-6">
                                    <div class="product-item">
                                        <div class="position-relative bg-light overflow-hidden">
                                            <img src="${seed.img_s}" class="img-fluid w-100" style="height: 350px;" />
                                        </div>
                                        <div class="text-center p-4">
                                            <h5>${seed.name_s}</h5>
                                        </div>
                                    </div>
                                </div>
                            `;
                        });
                    });
            } else {
                document.getElementById('search-results').innerHTML = '';
            }
        });
    }
});


function loadMore(category) {
    fetch(`/product/${category}/?show=all`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const container = document.querySelector('.tab-content .row.g-4');
        container.innerHTML = '';  // امسح المنتجات القديمة

        data.seeds.forEach(seed => {
            container.innerHTML += `
                <div class="col-lg-3 col-md-4 col-sm-6">
                    <div class="product-item">
                        <div class="position-relative bg-light overflow-hidden">
                            <img src="${seed.img_url}" alt="${seed.name_s}" style="width: 100%; height: auto;">
                        </div>
                        <div class="text-center p-4">
                            <a class="d-block h5 mb-2" href="#">${seed.name_s}</a>
                        </div>
                    </div>
                </div>
            `;
        });

        // أخفي الزر بعد عرض الكل
        document.getElementById('show-more-btn').style.display = 'none';
    });
}

function showDetails(name, imageUrl, description) {
    document.getElementById("modalImage").src = imageUrl;
    document.getElementById("modalName").textContent = name;
    document.getElementById("modalDescription").textContent = description || "لا يوجد وصف متاح";
}


